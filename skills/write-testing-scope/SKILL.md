---
name: write-testing-scope
description: Write the QA testing scope for a Linear ticket, a PRD section or a PR, the way a frontend developer hands work over to QA. Reads the ticket or PRD (and the code diff when there is one), works out what problem it solves and what could break, then writes short, plain-English bullets QA can run. Use this whenever someone asks for a testing scope, QA scope, test plan, "what should QA test", "QA notes", smoke test list, regression list or the QA section of a PR, or pastes a Linear ticket (APP-123, BUG-456), a Linear/Notion PRD section or a PR link and wants it ready for QA, even if they never say "testing scope". Also use it when filling the [FE] Testing Scope doc of a flight. Not for writing unit or E2E test code.
---

# Write Testing Scope

The reader is a QA engineer who did not build this and will test it on staging. They need to know what to click and what they should see. They don't need to know how the code works.

A good scope is short. Each bullet is one thing to check, written so QA can do it without asking the developer.

## Workflow

### 1. Gather the input

Get everything that explains the change. Use what's available, skip what isn't:

- **Linear ticket:** the description, the comments (often hold the real repro or a decision) and any linked PR. Look at screenshots or recordings if the steps depend on them.
- **PRD section:** the section text, plus the parts of the PRD it relies on (non-scope items, known limits, changelog).
- **Code:** if there's a PR, branch or diff, read it. When you're in the app's repo, `gh pr view <n>` and `gh pr diff <n>` work. The code is where the useful gotchas come from (see step 3).

If you only have a ticket ID or a link and can't fetch it, ask for the text. Don't guess what a ticket says.

### 2. Work out what it's about

Before writing anything, answer these for yourself in a sentence each. They decide what goes in the scope:

- **What's the problem or requirement?** For a bug: what broke, for whom, and when. For a feature: what the user can now do.
- **What's the user-facing change?** The screens, buttons, messages and flows that behave differently now.
- **What did the fix or feature touch that other places also use?** A shared component, store, util, API call or dialog means other screens can break. Those become regression checks.

### 3. If there's code, look for what the ticket or PRD won't tell QA

This is the most valuable part of the scope. Read the diff for:

- **Where the code differs from the PRD or ticket.** Limits, defaults, things only checked on one environment, fallbacks, cases it doesn't handle.
- **Every entry point.** List each way a user can reach the changed code: buttons, dialogs, drawers, AI assistant actions, keyboard shortcuts, API or MCP paths. Each one the diff touches gets a case, even if the ticket only mentions one of them.
- **Shared code.** Find the other callers of anything changed (grep for the component, function or store). List the screens a QA should smoke test.
- **Edge cases the code handles on purpose.** Loading or failed states, empty lists, a value deleted in another tab, throttled network, pagination, permissions.
- **Things QA can't test manually.** Say so and say why (staging limit, can't force a 401, deprecated channel), and name what covers it instead if you know (unit test, E2E spec).
- **Known behaviour that looks like a bug but isn't.** Same as master, a platform limit, agreed with PM. Write it down so QA doesn't file it.
- **Open questions.** Behaviour the PRD doesn't define. Turn it into "check with PM" or "raise with BE" instead of guessing the answer.

Leave implementation detail out of the scope (file names, function names, refactor notes) unless QA needs it to find a screen or set something up.

### 4. Write the scope

Pick the shape from what you're scoping.

**A bug fix or tech improvement ticket.** There's no PRD to lean on, so cover the fix and the regression around it:

```
>>> APP-318 Customers table flashes "No customers yet" on page refresh

* Ensure refreshing Customers doesn't flash the empty state while the table loads
* Ensure existing behaviour still works:
  * Search, and search kept after a page refresh (query in the URL)
  * Saved view, and view kept after a page refresh
  * Rows per page
  * Pagination

>>>
```

**A PRD section.** QA already tests the PRD. Only add what the PRD doesn't cover or where the code behaves differently from what it says. End with "Others as per PRD." If there's nothing to add, the whole section is "As per PRD.":

```
>>> ### Section 3: Connect a phone number

* **Staging vs production:** the "verified numbers only" filter only runs on production. On staging every number shows. Verify the filter again on production.
* An account with more than 100 numbers: only the first 100 load, and there is no paging
* New: the leave warning shows as soon as anything is typed. `Back` has no warning.
* Others as per PRD.

>>>
```

**A bigger ticket with setup or several flows.** Group with short italic labels, only the ones you need: *Setup*, *Main cases*, *Regression*, *Known, not a bug*. Numbered steps are fine when order matters, with the expected result nested under the step:

```
*Setup*

* Test on staging, all in one browser tab
* Repeat case 1 in Safari (stricter popup blocking)

*Main cases*

1. Settings → Integrations → Calendar → Connect. Don't log in. Click Back, then connect again. Do this 3 times, then log in on the last popup
   * Expected: exactly one calendar connection
```

**A PR body.** Same bullets under a `## QA testing scope` heading, no `>>>` block.

For more samples in this style, read `references/examples.md`.

## How to write each bullet

- **Keep each bullet to one short line.** Aim for about 20 words. A bullet that runs to two or three lines is a paragraph in disguise, and QA will skim past half of it.
- **Nest instead of chaining.** When a check has steps, variants or several expected results, put the action in the parent bullet and each step, variant or result in its own child bullet. Go up to three levels deep when it helps. For example, instead of one long bullet:

  ```
  * Validate that leaving the email channel setup after step 1 by clicking a sidebar item shows the "Setup in progress" dialog, that Cancel keeps you on the flow with step 1 still filled, that Leave navigates away once, and that refreshing shows the browser's leave prompt
  ```

  write:

  ```
  * Email channel setup → finish step 1 → click a sidebar item:
    * "Setup in progress" dialog shows
    * Cancel → stays on the flow
      * Step 1 fields are still filled
    * Leave → navigates away once
  * Refresh mid-connection → browser's leave prompt shows
  ```

- **Start with what to check.** "Validate that...", "Ensure...", or the path and action followed by the result: `Inbox → filter by Unassigned → open a ticket → Back → filter is kept`.
- **Show QA how to get there.** Give the navigation path with `→` (`Settings → Channels → Add channel → Email`). Add the URL too when it saves QA time: a page that's only reachable by URL, a deep link to a specific tab or record, a staging or preview link, or a test account or workspace ID they need. Use real routes from the code, and put a guessed URL in `[brackets]`.
- **Use the app's own words.** Real button and dialog names, real error text in quotes. Bold a name only when it helps QA spot it.
- **Say what "good" looks like.** "No toast", "exactly one connection", "stays on page 1". Avoid "works correctly" on its own, because QA can't check it.
- **Tag what's new or known.** "(new)" for behaviour that didn't exist before. "Known, same as master, not a regression" for an old quirk QA will run into.
- **Plain English, no filler.** Short words, no intro paragraph, no "This testing scope covers...". A one-line note at the top is fine only when QA needs it before starting (test on Safari, test before a date, needs a specific account).
- **No em dashes or en dashes.** Use a colon, a comma or a full stop.

## Keep it tight

- Most bug fixes need 3 to 8 top-level bullets, often under 150 words. A PRD section often needs 0 to 5 extra bullets beyond "Others as per PRD." If a scope passes about 300 words, cut before handing it over.
- Merge checks that differ only in a value ("sort by Name, Date, and flip direction") into one bullet instead of one each.
- Cut anything QA would test anyway without being told (that the page loads, that a button exists), unless it's a real regression risk.
- Notes after the scope block are for the developer, not QA. Keep them to the few things the user must act on.
- Order by risk: the actual fix first, then the edge cases, then regression.
- Don't invent requirements. If you're not sure how something should behave, write it as a question for PM rather than an expected result.

## Handing it over

1. Give the scope first, in a fenced markdown block so it pastes cleanly into Linear or GitHub. No preamble.
2. After the block, add at most a few lines for what the user should know: open questions for PM or BE, things you couldn't verify, and anything you guessed (mark guesses in the scope with `[brackets]`).
3. Then offer to put it where it belongs: a new `>>>` block in the flight's [FE] Testing Scope Linear doc (under Flight, Bug Fix or Tech Improvements), or the PR's QA section. Only write to Linear or GitHub after the user says yes.
