---
name: agentos-story-events
description: Query AgentOS daily storyline Events and variable signals when the original research needs news or event context. Supplements existing sources without changing the research method or report structure.
category: tool
---
# AgentOS Storyline Events

## Purpose

Use AgentOS Events and associated variable signals as additional input wherever the original research
method calls for news or event information. Combine relevant information with existing external research
and make your own analytical judgment. Preserve the original role responsibilities and report structure.
Do not add an AgentOS verification section, Event/Signal inventory, evidence-quality assessment,
or a separate chief verification step. Incorporate useful information naturally into the existing analysis;
use the original report's citation conventions when citing a source.

## Query

Use only the real `story_id` and `research_date` supplied in the task. If either is missing, continue
original research without AgentOS; never guess an identity/date. "New" means graph Event `created_at`
on that Asia/Shanghai calendar date, not occurrence time, article publication or late storyline association.

1. When news or event context is needed, call
   `mcp_agentos_query_story_events(story_id, research_date, limit=100)`.
2. Read the Event titles, summaries, semantic fields and times, together with their `variable_signals`.
   Use relevant information in the original analysis; no separate review deliverable is required.
3. If `next_after_event_id` is non-null, pass it as `after_event_id` until null to finish this query.
   Deduplicate Event/Signal IDs across pages. This is a live query, not a frozen snapshot.
4. If the research needs further source detail, optionally call
   `mcp_agentos_get_story_evidence(story_id, research_date, event_id, evidence_id)` with returned IDs.
   Evidence is source material, not necessarily a complete news article.
5. Continue existing external news, quantitative data and calculation tools normally.

## Data meaning and availability

- Events describe reported occurrences, plans or expectations; retain that distinction.
- Signals describe previously analyzed changes to a named variable on a named anchor. They can inform
  further reasoning; they do not automatically determine a stock's bullish/bearish direction.
- Preserve the meaning, timing and target of the supplied data when using it. A signal marked
  `usable_as_complete_fact=false` has incomplete source coverage in this query; its full assertion is unavailable.
  Do not expand the query into historical Events or invent missing information.
- Old tool results may be cleared by the worker. Keep useful working notes or re-query when the analysis
  needs the original details again. No separate reference ledger is required.
- If a tool fails, continue available research without pretending the unavailable data was obtained.
  Do not send internal URLs or credentials through read_url.
- The provider fits complete Events and associated Signals within 28,000 characters, up to limit=100.
  These two AgentOS tools have a 30,000-character consumer budget; other tools retain their original limits.
  A null cursor with the unique Event count matching total means this query has returned all current Events.
