# PRD: Inbox: Ticket priorities (excerpt)

## Overview

Agents can't tell urgent tickets from routine ones today, so urgent issues wait in the same queue as everything else. This PRD adds a priority to every ticket (Urgent, High, Normal, Low), shows it across the Inbox, lets automations set and read it, and exposes it to integrations.

## Scope summary (Must have)

- Inbox: set, change and clear a ticket's priority; show it on the ticket and in the ticket list; filter and sort by priority
- Automations: new **Set priority** step; priority available as a condition
- Integrations/Webhook: expose priority to the API, MCP, webhooks and Zapier/Make
- Reports: break down ticket volume and response time by priority
- Data export: include priority in ticket exports

## Non-scope items / known limits

- Custom priority levels or renaming the four levels
- SLA timers per priority (separate PRD)
- Tickets created before release have no priority. They show as "No priority" until someone sets one. No backfill.
- Priority on merged tickets: the surviving ticket keeps its own priority.

## Section 1 (summary): Set and show priority > Inbox

- Agents set priority from the ticket header dropdown or the ticket list's bulk actions.
- Priority can be cleared back to "No priority".
- Ticket list shows a coloured priority badge; list can be filtered and sorted by priority.

## Section 5: Integrations/Webhook

### Overview

Expose ticket priority everywhere ticket data leaves Relay, so customers' own tools can route and report on it.

### Requirement

#### Ticket data

Add a `priority` field to the ticket object in:

- Developer API
- MCP
- Zapier and Make actions

Applicable actions/endpoints:

- `Get Ticket`
- `List Tickets` (also accepts `priority` as a filter)
- `Update Ticket` (accepts `priority`)

Values: `urgent`, `high`, `normal`, `low`.

#### Webhook events

- New event: `Ticket Priority Changed`, sent when a ticket's priority is set or changed. Payload includes the ticket, the old priority and the new priority.
- Existing event `Ticket Updated`: include `priority` in the ticket object.
- Add `Ticket Priority Changed` to the event list in Settings → Integrations → Webhooks, and as a trigger in Zapier and Make.

> Tech to confirm if any other endpoints or integration actions need the field.
