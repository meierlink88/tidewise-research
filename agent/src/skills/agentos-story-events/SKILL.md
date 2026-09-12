---
name: agentos-story-events
description: Read a supplied AgentOS geopolitical storyline's newly created daily Events, associated variable signals and supporting Evidence via MCP. Supplements existing research sources.
category: tool
---
# AgentOS Storyline Events

Use only the real `story_id` and `research_date` supplied in the task. Without both, report missing input;
never guess an identity/date or replace the scope with a keyword search. "New" means graph Event `created_at`
on that Asia/Shanghai calendar date, not occurrence time, article publication or late storyline association.

1. Call `mcp_agentos_query_story_events(story_id, research_date, limit=1)`.
2. Review each Event's title, summary, semantic fields and time, and its `variable_signals`.
3. Pass `next_after_event_id` as `after_event_id` until null. Deduplicate Event/Signal IDs across pages.
   Keep the received unique IDs and query timestamps. `total` is live and can change; report mismatch or restart
   the scan rather than claiming complete coverage. This is not a frozen snapshot.
4. For a key fact, contradiction or missing supporting detail, call
   `mcp_agentos_get_story_evidence(story_id, research_date, event_id, evidence_id)` using returned IDs.
   Evidence is atomic semantic source material, not necessarily a complete news article.
5. Continue existing external news, quantitative data and calculation tools normally. Internal data is an
   additional source, not a replacement for independent research. Record external sources separately.

## Evidence discipline

- Event = reported occurrence/plan/expectation with explicit modality. Signal = previously analyzed Variable
  change on a named anchor, not a new research conclusion and not automatically bullish/bearish for a stock.
- Preserve variable and anchor identities, source Event IDs, invalidation and timing. Do not rewrite a Signal
  into a stronger fact, silently re-anchor it or count duplicate reports as independent confirmations.
- `usable_as_complete_fact=false` means a signal depends on Events outside this day/story scope; do not use
  its complete assertion or expand history. Record the missing IDs as a gap.
- Missing signals are not evidence of no impact. Missing provenance or unfinished publication is a data gap.
- Old tool results may be cleared by the worker. Keep a compact reference ledger in your working files and
  re-query key supporting Evidence before finalizing. Do not rely on remembered numeric values.
- Include a daily Event review ledger in report.md: Event ID, used / not relevant / evidence gap, reason,
  and related Signal/Evidence IDs. Unsupported causal transmission remains a hypothesis.
- Chief: inspect this same scope, compare upstream references, and re-read Evidence for key conclusions.
  Do not assume upstream report text is identical to original observations.

## Errors

If a tool is absent, denied or fails, explicitly report the integration failure; external research can continue,
but do not claim the AgentOS input was reviewed. Do not send internal URLs or credentials through read_url.
Use small pages; if a result is truncated, do not mark its unseen content as reviewed.
