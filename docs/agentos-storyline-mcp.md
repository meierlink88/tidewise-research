# AgentOS storyline MCP integration

Provider contract: meierlink88/tidewise-agent-os#245 (`story-events/v1`). Configure the existing Swarm
MCP loader with `VIBE_TRADING_SWARM_AGENT_CONFIG` pointing to an absolute deployment JSON file;
start from `agent/agentos-mcp.example.json`, replace host and configure deployment authentication.
Never commit credentials. Provider must expose `query_story_events` and `get_story_evidence`.
Use the exact server key `agentos` to match preset tool names. Existing MCP transport supports
Streamable HTTP, SSE and stdio. Production uses the existing AgentOS endpoint and auth.

Pass native `user_vars`: `crisis` (storyline name only), `market`, real GPR `story_id`,
`event_window_start` and `event_window_end` (timezone-aware ISO timestamps, [start,end)),
and `agentos_workflow_run_id` for tracing. Leave `research_date` empty in window mode.
Do not embed Event/Signal bodies in crisis: research workers obtain them using MCP.
Legacy callers may supply a Shanghai `research_date` instead of both window values.
These are live queries, not frozen Event/Signal snapshots; keep scope identical across pages.
Do not change the original team roles, DAG, research method or report format.
Verify all four workers actually register both tools before a coupled run; the registry otherwise warns
and drops unavailable remote tools. Keep the original tools/skills/DAG. New Skill explains how to query daily Events and associated signals when the original research needs
news/event context, including pagination and data meaning. Preserve the original report structure; no
AgentOS verification chapter, evidence-quality assessment, per-Event ledger or mandatory chief re-query.

Test provider first, then consumer allowlists/schema/variable rendering, then a real four-role run.
Integration diagnostics may record calls/results, delivered Event/Signal counts and tool errors outside
the research report. These diagnostics are not an additional analyst task or report section.
Task completion alone is not business validity. Rollback removes the appended Skill/tool/input entries
and MCP deployment configuration; no persisted AgentOS data is modified by these tools.

Set `compact_structured_results: true` for AgentOS. The MCP adapter then removes only exact duplicate
JSON aliases (data/structured_content/text blocks), retaining distinct text and media. Default false preserves
all existing servers. Without it a small Event page can exceed the Worker 10,000-character cap through duplication.

AgentOS Event/Evidence tool results now receive a 30,000-character budget in both the main Agent and Swarm Worker. Exact names only; all other tools retain 10,000. Provider default limit=100 fits whole Events within 28,000 characters and returns a continuation when necessary; no one-Event cap.
