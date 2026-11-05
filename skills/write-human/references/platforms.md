# Platform guide

Each platform has a different job. Match the length and format to that job, not to how much you know.

## Slack: conversation

Slack is read fast, often on a phone, between other things. Treat every message like it will be skimmed.

- **Length.** A reply is 1 to 4 lines. An announcement or update fits on one phone screen. Anything longer goes in a Notion page or Linear doc, with the link and a 2-line summary in Slack.
- **Format.** Slack uses mrkdwn, not full markdown: `*bold*`, `_italic_`, `~strike~`, `` `code` ``, ``` ``` ``` for blocks, `•` or `-` bullets, `1.` numbered lists, and `<url|text>` links (or a bare URL). There are no headings. Use one `*bold*` line as a section label if you really need sections. Keep lists flat unless nesting really helps, because nested bullets don't always survive pasting.
- **Threads.** Put the headline in the parent message and the details in the thread. In a thread reply, skip greetings and context everyone in the thread already has.
- **Mentions.** Only @ people who need to act or decide, and say what you need from them on the same line ("@Ana can you confirm the cutoff by Fri?").
- **Emoji.** One emoji where it does a job is fine (✅ done, ⚠️ risk, 🚀 launch). Don't decorate every line.
- **Section labels.** Announcements and updates with more than one part get a `*bold*` label line per part (`*What changed*`, `*Who gets it*`). Short replies don't.
- **Tone.** Conversational and warm, never curt. Use contractions, short sentences, "we" and "I". A brief natural opener in a reply is fine ("Close!"). No sign-off.

## Linear: work tracking

Linear is read by people who are about to do the work or check its status. They want scope, state and next action.

- **Issue titles.** Say the outcome or the problem in under ~70 characters, with no trailing period. "Contacts export drops rows over 10k", not "Investigation into export issue".
- **Issue descriptions.** Use full markdown and write in bullets, not paragraphs. That includes the opening: what's wrong, the symptom, the cause or theory, and when it started each get their own bullet. Then add the sections that apply: context, scope (in and out), acceptance criteria as a checklist (`- [ ]`), repro steps, links.
- **Comments.** Write them like a status line. Say what changed, what's blocked, and who you need. Don't restate the issue description.
- **Docs and project updates.** Use headings, but keep them flat (`##` and `###`). Put a TL;DR at the top of anything over a screen.
- **Plans.** Unless the user asks, don't add time estimates, schedules or per-item owners. Show order, dependencies and roles instead.

## Notion: reference

Notion holds the longer pieces people come back to: proposals, analyses, plans, specs, and the record of decisions.

- **Bullets over paragraphs.** Write the TL;DR as bullets, one fact per bullet. Write options, risks and findings as a bold name with the reason nested under it. A paragraph should be rare, and it should be short.
- **Structure.** Use a TL;DR or summary block at the top, then headings in sentence case. Use tables for comparisons, options and risk lists. Use callouts for the one thing a skimmer must not miss. Put long detail that most readers can skip in toggles.
- **Length.** It can be longer than Slack or Linear, but each section still opens with its point. A reader skimming only the first line of each section should get the whole argument.
- **Audience.** Team-facing docs should be quick to scan and avoid jargon. Keep file paths, line numbers and internals out of them unless the readers are engineers who need them. Plain tables beat paragraphs.
- **Questions.** Collect open questions in their own section near the end, phrased so someone can answer each one in a line.

## GitHub (PR descriptions, issues)

- **Opening.** The first line says what the change does and why.
- **Body.** Follow with short bullets on what changed, how it was tested, and anything a reviewer should look at closely.
- Follow the repo's own PR template or conventions where they exist.

## Email

- **Subject.** Put the point in the subject line.
- **Body.** Open with the ask or the news in the first sentence. A short greeting and sign-off are normal here and not filler.
