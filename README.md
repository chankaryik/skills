# skills

My agent skills, packaged as a Claude Code plugin marketplace.

## Install

```bash
claude plugin marketplace add chankaryik/skills
claude plugin install write-human@chankaryik-skills
claude plugin install write-testing-scope@chankaryik-skills
```

Inside Claude Code you can run the same thing as `/plugin marketplace add chankaryik/skills`, then pick a plugin from `/plugin`.

## Skills

- **write-human**: house writing standard for anything a person will read. Short, direct, easy to scan, no em dashes.
- **write-testing-scope**: QA testing scope for a Linear ticket, PRD section or PR. Plain-English bullets, only what QA needs.

## Adding a skill

1. Put it in `skills/<name>/` with a `SKILL.md` at the root.
2. Add a plugin entry for it in `.claude-plugin/marketplace.json` (copy the `write-human` one and change the name, description and `skills` path).
3. Run `claude plugin validate .`, then commit and push.
4. Pick it up locally with `claude plugin marketplace update chankaryik-skills`.
