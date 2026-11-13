# The Home Repo Pattern

**Source:** [The Home Repo Pattern: Run agents across ALL your repos](https://www.youtube.com/watch?v=hWe-j78vNpc) - Matt Pocock, 2026-11-12

## Summary

Organisations with many repos struggle to give coding agents the same context everywhere. Shared skills, steering files and tooling either get copied into every repo, where they drift out of sync, or get hidden in each person's user directory, where they go stale. Matt Pocock's answer is the **home repo**: one ordinary repo that holds all the skills, steering files, versioned settings, a wiki and custom tooling. The agent **always runs from the home repo** and reaches the other repos through plain paths listed in its `AGENTS.md`/`CLAUDE.md`.

He thought the technique was too obvious to post about, but people reacted strongly when he showed it. It solves the multi-repo problem with no setup, and because everything lives in one place it gives a natural home for much more ambitious tooling that works across systems.

## The Problem: Context Across Many Repos

- A typical org has repos like a storefront, a payments API, an admin dashboard, and 20+ more you only touch now and then.
- **Working across repos is the easy part.** An agent can work in several directories in one session and open a PR in each one.
- **The hard part is shared context**: skills, tooling, `AGENTS.md`, wiki links. You want these available in every session.
- Both obvious answers fail:
  - **Duplicate them into every repo.** Now you have to keep 30–40 copies in sync. This is a massive pain.
  - **Put them in the user directory** (`~`). They are available everywhere, but nobody sees them, so they don't get updated and fall behind the team's setup. Pocock also thinks of the user directory as the place for *personal* preferences about how one person works, not for how the team wants them to work.

## The Home Repo

- **One repo holds everything shared**: skills, steering files, a wiki and custom tooling.
- **The agent is always started inside the home repo.** From there it reaches out to the storefront, the payments API and any other repo, and pulls in whatever context it needs.
- **Private skills** live in `.claude/skills/`. These are skills too sensitive to the business to publish, and they are available in every session. Org-wide skills belong here too.
- **Versioned settings**: a `settings.json` in the home repo applies the same settings across the whole org at once.
- **Navigation pointers** in `CLAUDE.md`/`AGENTS.md` are just paths to the repos he touches every day, e.g. `repos/ai-skills` for skill changes, plus the course video manager (his most active repo), the cohort project and the crash-course repo.

### Zero-setup mechanics

- On a fresh machine, if a listed repo doesn't exist at its path, the agent **clones it**.
- When several agents run at once, each uses a **worktree** of the same clone. The only upkeep is cleaning up old worktrees from time to time.
- To add a repo, you **edit `AGENTS.md`**. Nothing else changes.

## Scaling: Progressive Disclosure

- A flat list of paths works for roughly **20–40 repos**, but not for around 400.
- At that scale, add **progressive disclosure**: the top-level `AGENTS.md` points at groups (front-end repos, back-end repos, internal-tooling repos), and each group lists its own repos.
- The agent then finds the right repo by simply walking the file system.

## Relation to Monorepos

- Pocock (formerly Turborepo DevRel at Vercel) prefers monorepos: if everything can live in one repo, put it there.
- Often you can't, because some repos have to be public and others private, or because there isn't the **political will** to merge them.
- **Monorepo if you can; home repo if you can't.**

## Enabling More Ambitious Tooling

- Since adopting a home repo he has built **much more ambitious agent tooling**, because there is now one obvious place to put it.
- **Personal wiki**: his home repo *is* his personal wiki. It includes a Karpathy-style **LLM Wiki** of markdown files with business-sensitive material (what his audience finds interesting), which he queries for course and content creation.
- **Custom CLI tooling** (`wiki help`): integrations with Gmail, Slack, Discord, YouTube, GitHub, Google Calendar, AI Hero, Cold Turkey (for blocking), one-off HTML reports and Buffer. It all grew organically in one place.
- **Workflows across systems** become possible. For example: look up a Discord message, fix the crash-course repo using existing skills, then use the CVM skill in the course video manager to update the course itself.
- In this way the home repo becomes **the tooling that links the business together**. It connects not just the code but rich data sources and tools as well.

## Getting Started

- His article "The Home Repo Pattern" includes a setup prompt. It asks you about your setup, looks at the repos you care about, and starts moving shared material into a home repo.

## Core Insight

Shared agent context should live in **one visible, versioned place**, not be copied around or hidden in personal config. The fix is to change *where the agent runs*, not to copy context into every repo. Start every session from a home repo, and other repos are just paths it can reach. Once there is one centre the agent always works from, it also becomes the natural place to build up wikis, private skills and integrations, which lets the agent do work across code, data and services that no single repo could support.
