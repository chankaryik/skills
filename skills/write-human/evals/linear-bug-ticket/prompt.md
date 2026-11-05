---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

write up a linear ticket for this pls. agents opening tickets with more than 2000 replies in the helpdesk get 'Something went wrong'. sentry RELAY-WEB-4821, ~340 events in the last 24h, 57 users affected. looks like the reply list request times out after 30s and backend returns 504. started after release 2026.10.28. workaround: open the ticket from the customer profile, that only loads the last 50 replies. need BE to check pagination on GET /tickets/:id/replies
