# Doc type skeletons

These are starting shapes, not forms to fill in. Drop any section that would be empty, obvious or a restatement. For short platforms (Slack, a Linear comment), squeeze the skeleton into a few lines and keep its order.

## Contents

- Proposal
- Analysis
- Plan
- Error troubleshooting
- Reply
- Announcement
- Status update

## Proposal

Goal: get a yes, or a clear decision.

1. **Summary.** What you propose and the payoff. This is an impact piece, so lead with the result. Use bullets, one fact per bullet.
2. **Problem.** What hurts today, with a number or a concrete example if you have one.
3. **Proposal.** What you'd do, as a short list.
4. **Why this option.** List the alternatives you actually considered as bold names, each with the reason you didn't pick it nested underneath. Skip any alternative nobody would seriously suggest.
5. **Cost and risks.** Effort, trade-offs and what could go wrong.
6. **Ask.** The specific decision you need, from whom, and by when.

## Analysis

Goal: help the reader understand something well enough to decide.

1. **TL;DR.** The conclusion in 1 to 3 lines.
2. **Key findings.** A numbered list, most important first. Give each finding its evidence (a number, an example or a link) in the same item.
3. **Implications.** What the findings mean for us.
4. **Recommendation or options.** If there's a choice, use a small table: option, pros, cons.
5. **Open questions.** Things you couldn't confirm, phrased as answerable questions.

Keep method and raw data in an appendix or toggle unless the reader asked for them.

## Plan

Goal: everyone knows what happens, in what order, and what depends on what.

1. **Goal.** What done looks like, in 1 to 2 lines.
2. **Steps.** A numbered list in execution order. Mark dependencies inline ("after 2").
3. **Out of scope.** What you're deliberately not doing.
4. **Risks.** The few that could change the plan, each with a mitigation.

Don't add time estimates, schedules or owners per item unless the user asks.

## Error troubleshooting

Goal: someone can understand the issue and act, whether they're fixing it or waiting on it.

1. **Status line.** Say what's broken, who is affected, and the current state (investigating, mitigated or fixed).
2. **Impact.** Scope in numbers if you have them (users, workspaces, requests, time window).
3. **Cause.** The root cause in one or two plain sentences. If it isn't known yet, say "cause not confirmed yet" and give the leading theory.
4. **Fix or workaround.** What was done or what to do now, as steps if there's more than one.
5. **Next steps.** Prevention or follow-up items.
6. **Details** (optional). Error messages, logs and repro steps, in a code block or a toggle.

For a Slack incident thread, items 1, 4 and 5 are often enough.

## Reply

Goal: answer what was asked.

- **Answer first, warmly.** The first line is the answer, the decision or "yes/no, because...". It can open with a short human touch ("Close!", "Not quite, but nearly"). Don't let it read like a bare status line.
- **Then the reason.** Add only the reasoning that changes the reader's view. Don't rebuild context they already have.
- **Close only if needed.** End with a question only if you genuinely need something back.
- **If you don't know yet,** say so and say when or how you'll find out.

## Announcement

Goal: people notice it, understand what changes for them, and know what to do.

1. **Headline.** What's new and the payoff, in one line. This is an impact piece.
2. **What changes for you.** 2 to 4 bullets, written from the reader's side.
3. **Action** (if any). What to do, and by when.
4. **More.** A link to docs or a contact for questions.

On Slack, give each part after the headline a `*bold*` label (for example `*What changed*`, `*Who gets it*`, `*Docs*`) so readers can jump to the part they care about.

## Status update

Goal: the reader knows where things stand in ten seconds.

1. **Overall.** On track, at risk or blocked, plus one line on why.
2. **Done.** Bullets.
3. **Next.** Bullets.
4. **Blockers or asks.** Who you need, and for what.
