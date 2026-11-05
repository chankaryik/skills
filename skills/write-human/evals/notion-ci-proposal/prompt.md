---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

need a notion proposal to convince my eng manager we should run E2E tests on every PR into release branches instead of only nightly. context: last release cycle, nightly runs caught 14 regressions, on average 2 days after the PR merged, and each one took about half a day to trace back to the PR. full suite takes 38 min but we can shard it across 4 runners to get it down to about 11 min. CI cost goes up roughly 300 USD a month. flaky rate is around 3% right now which might annoy people.
