"""Consumer contract for AgentOS tools in the native geopolitical preset."""

from src.swarm.presets import build_run_from_preset
from src.swarm.worker import build_worker_prompt
from src.config.schema import AgentConfig, MCPServerConfig
from src.tools import _prune_agent_config_for_swarm_tools


def test_all_four_roles_receive_story_scope_and_keep_original_dag():
    run = build_run_from_preset("geopolitical_war_room", {
        "crisis": "美伊军事冲突", "market": "A股市场", "story_id": "GPRtest", "research_date": "2026-09-12"})
    names = {"mcp_agentos_query_story_events", "mcp_agentos_get_story_evidence"}
    for agent in run.agents:
        assert names <= set(agent.tools)
        assert "agentos-story-events" in agent.skills
        assert {"bash", "read_file", "write_file", "load_skill"} <= set(agent.tools)
        if agent.id != "chief_strategist":
            assert "read_url" in agent.tools
    for task in run.tasks:
        prompt = task.prompt_template.format_map(run.user_vars)
        assert "GPRtest" in prompt and "2026-09-12" in prompt
        assert "agentos-story-events" in prompt
    assert all(not t.depends_on for t in run.tasks[:3])
    chief = run.tasks[-1]
    assert set(chief.depends_on) == {t.id for t in run.tasks[:3]}
    assert set(chief.input_from.values()) == set(chief.depends_on)


def test_mcp_server_is_selected_by_actual_local_tool_prefix():
    config = AgentConfig(mcp_servers={"agentos": MCPServerConfig(
        type="streamableHttp", url="http://127.0.0.1:8000/mcp",
        enabled_tools=["query_story_events", "get_story_evidence"])})
    run = build_run_from_preset("geopolitical_war_room", {"crisis": "test", "market": "A股"})
    for agent in run.agents:
        selected, names = _prune_agent_config_for_swarm_tools(config, agent.tools)
        assert set(selected.mcp_servers) == {"agentos"}
        assert names["agentos"] == "agentos"
        assert "Data Citation Discipline" in build_worker_prompt(agent, {}, "")


def test_compact_mcp_json_keeps_data_and_preserves_distinct_content():
    import json
    from fastmcp.client.client import CallToolResult
    from mcp.types import TextContent
    from src.tools.mcp import _normalize_call_tool_result

    data = {"events": [{"id": "E1", "summary": "fact"}], "next_after_event_id": None}
    result = CallToolResult(content=[TextContent(type="text", text=json.dumps(data))],
        structured_content=data, data=data, is_error=False, meta=None)
    compact = _normalize_call_tool_result(result, compact=True)
    assert compact == {"status": "ok", "data": data}
    assert "structured_content" in _normalize_call_tool_result(result)
    result.content.append(TextContent(type="text", text="Additional warning"))
    compact = _normalize_call_tool_result(result, compact=True)
    assert "Additional warning" in compact["text"]
    assert len(compact["content"]) == 2
