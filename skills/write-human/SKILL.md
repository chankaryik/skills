---
name: write-human
description: House writing standard for anything a person will read. Makes drafts sound human, short, direct and easy to scan, with no em dashes. Use this whenever you write or rewrite text meant for people, such as a Slack message or reply, a Linear issue or comment, a Notion page, a proposal, analysis, plan, error troubleshooting write-up, announcement, status update, PR description, email or DM. Trigger even when the user doesn't mention style, for example "reply to this thread", "write up the RCA", "draft the announcement", "turn this into a Linear ticket", "tighten this", "make this sound less AI", or when another skill asks you to post or write a doc. Don't use it for code, code comments or commit messages.
---

# Write Human

Write the way a sharp colleague talks when they respect the reader's time. Every draft should pass this test: a busy teammate from another team reads it once, on their phone, and knows what you mean and what you need from them.

## The six standards

1. **Sound human, without padding.** Use plain words, contractions, "I" and "we", and real names, numbers and dates. Write it the way you'd say it out loud to a teammate. Curt is a failure too. A reply to a person should sound like a colleague talking, not a status bot. A short, natural touch of warmth is good ("Almost there!", "Good timing, I was about to post this"), as long as the answer still lands in the first line. What to avoid is stock filler ("Great question!", "Hope this helps!") and friendly sentences that say nothing.
2. **Lead with the point.** The first line holds the answer, the decision, the ask or the result. Context comes after, and only as much as the reader needs to act. If a reader stops after one line, they should still have the main thing.
3. **Short, but it has to land.** Cut every sentence that doesn't change what the reader knows or does. Keep the specifics (numbers, names, links, before and after) because they are what make a short message meaningful. A vague short message is worse than a clear longer one.
4. **Long content becomes lists.** Readers scan lists far faster than paragraphs, so lean toward lists whenever there's more than a couple of points.
   - If a paragraph carries 3 or more separate points, or a sentence chains "and... which... so...", turn it into a list with one point per item. This includes the summary or TL;DR (a TL;DR with four facts becomes four bullets) and the opening of a ticket or doc.
   - On Linear and Notion, bullets are the default everywhere, including ticket descriptions. Prose is only for a section that's one or two sentences long.
   - Use numbered lists for steps, order and priority, and bullets for parallel items. Numbering starts at 1.
   - Keep one idea per item, about a line long.
   - When an item has a name and an explanation (an option, a finding, a risk, a change), bold the name as the parent bullet and nest the explanation under it. Keep nesting to one level:
     ```
     - **Run a smoke subset per PR.**
         - Cheaper and faster, but we don't know how many of the 14 regressions it would have caught.
     ```
5. **No em dashes. Ever.** This also covers en dashes (–) and hyphens or double hyphens used as dashes (" - ", "--"). Use a period, comma, colon or parentheses instead, or rewrite the sentence. Hyphens inside words (follow-up, on-call), ranges in data, code, paths and URLs are fine. This rule beats everything else, including the user's own samples.
6. **Promoting a result? Summary first.** When the text exists to show impact (a launch, a win, a proposal, a postmortem with good news, a performance gain), open with a short summary of the outcome: one line, or a few bullets if there are several facts. Give the concrete payoff (what changed, by how much, for whom) so the reader knows what's coming and wants to keep reading. Skip it for plain replies and quick questions, where it just becomes noise.

## Workflow

1. **Pin down the reader, the platform and the type.** Who is reading (engineers, PMs, leadership, customers), where it will live (Slack, Linear, Notion, GitHub, email), and what kind of piece it is. Infer this from context. Ask one short question only if you can't tell and the answer would change the output.
2. **Write the first line first.** Decide what the reader must take away and put it on top. For an impact piece, that's the summary from standard 6.
3. **Draft to the platform and type.** Read `references/platforms.md` for format rules on each platform, and `references/doc-types.md` for the skeleton of each kind of piece (proposal, analysis, plan, troubleshooting, reply, announcement, status update). The skeletons are starting points. Drop any section that would be empty or obvious.
4. **Audit the draft.** Check it against `references/ai-tells.md`, the patterns that make text read as machine-written. If you can run scripts, run `python3 scripts/lint_draft.py <file>` (or pipe the text in on stdin). It flags dashes, overused AI words and chatbot phrases. A flag isn't automatically wrong, but each one needs a reason to stay.
5. **Rewrite, don't patch.** When something reads as AI, restate the point the way you'd say it. Swapping one word for a synonym usually leaves the stiff shape behind. Then cut once more. Most drafts get better at 70% of their first length.

## Facts stay exact

Shortening must never change the meaning. Keep every number, name, ticket ID, link, date and caveat the source gives you, and add none it doesn't. If something is uncertain, say so once, in plain words ("not confirmed yet", "I think"). Don't spread hedges across every sentence.

## Voice

If `references/voice.md` contains samples of the user's own writing, match their sentence length, word choice, openings and sign-offs. The samples win over the generic guidance here, except for the dash rule. If the user pastes a message they wrote earlier in the conversation, treat it as a sample too.

## Handing over the draft

- Give the draft itself first, ready to paste. Put it in a fenced code block when the user will copy it somewhere (Slack, Linear, Notion), so the formatting survives. Don't use `>` blockquotes for drafts.
- Don't add a preamble ("Here's a draft...") or a postscript explaining your choices. Add one line after the draft only when it changes what the user should do, like a placeholder they need to fill in or a fact you couldn't confirm.
- Mark anything you had to guess with `[brackets]` so it's obvious what to fill in.
- When writing straight into a tool (a Linear issue, a Notion page, a Slack draft), the same standards apply to the text you send.

## A quick example

Before:
> I wanted to reach out and give everyone a quick update on the recent issues we've been experiencing with the login flow — after a thorough investigation, our team has identified that the root cause was related to a misconfigured session timeout, which has now been addressed and deployed, so users should no longer experience unexpected logouts going forward.

After:
```
Login logouts are fixed. The session timeout was set to 5 min instead of 5 h. Fix is live as of 14:20 today.

If anyone still gets logged out, send me the workspace ID and time.
```

The second version leads with the result, keeps the real numbers, drops the run-up ("I wanted to reach out"), has no em dash, and ends with the one thing readers can do.
