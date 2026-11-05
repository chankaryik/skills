---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

reply to this in the thread for me. PM asked: 'hey is the campaign scheduling fix going out this week? customers are asking and CS wants a date'. the fix is merged into release/campaigns-v2 but QA found one more bug with timezones (campaigns scheduled in GMT+13 shift by one day). i think we can ship thursday if QA passes it wednesday, otherwise it goes in next tuesday's release
