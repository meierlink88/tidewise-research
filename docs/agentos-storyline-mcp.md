# AgentOS storyline MCP integration

Provider contract: meierlink88/tidewise-agent-os#245 (`story-events/v1`). Configure the existing Swarm
MCP loader with `VIBE_TRADING_SWARM_AGENT_CONFIG` pointing to an absolute deployment JSON file;
start from `agent/agentos-mcp.example.json`, replace host and configure deployment authentication.
Never commit credentials. Provider must expose `query_story_events` and `get_story_evidence`.
Use the exact server key `agentos` to match preset tool names. Existing MCP transport supports
Streamable HTTP, SSE and stdio. Production uses the existing AgentOS endpoint and auth.

Pass native `user_vars`: crisis, market, story_id (real GPR ID), research_date (YYYY-MM-DD Shanghai).
The two new variables are optional for backwards-compatible standalone research; with a storyline both
must be supplied by the caller. No data package, snapshot, scheduler or execution-layer replacement.
Verify all four workers actually register both tools before a coupled run; the registry otherwise warns
and drops unavailable remote tools. Keep the original tools/skills/DAG. New Skill explains pagination,
source closure, evidence checks, live consistency and per-Event review ledger.

Test provider first, then consumer allowlists/schema/variable rendering, then a real four-role run.
Record calls/results, per-role unique Event coverage and evidence use, report references and errors.
Task completion alone is not business validity. Rollback removes the appended Skill/tool/input entries
and MCP deployment configuration; no persisted AgentOS data is modified by these tools.

Set `compact_structured_results: true` for AgentOS. The MCP adapter then removes only exact duplicate
JSON aliases (data/structured_content/text blocks), retaining distinct text and media. Default false preserves
all existing servers. Without it a small Event page can exceed the Worker 10,000-character cap through duplication.
