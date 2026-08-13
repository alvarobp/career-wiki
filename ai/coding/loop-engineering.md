# Loop Engineering

**Sources:**
- [Loop Engineering](https://x.com/addyosmani/status/2064127981161959567) - Addy Osmani, 2026
- [Dex Horthy on context engineering, loop engineering and software factories](https://www.youtube.com/watch?v=Usufn8IQJgw) - The Pragmatic Engineer Podcast, 2026

## Summary

Loop engineering is replacing yourself as the person who prompts the agent: instead of typing a turn, reading the reply, and typing the next turn, you build a small system that finds the work, hands it out, checks it, records what's done, and decides what's next — and let *that* poke the agents. A loop is a recursive goal: you define a purpose and the AI iterates until it's complete.

> "You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents." — Peter Steinberger

> "I don't prompt Claude anymore. I have loops running that prompt Claude and figuring out what to do. My job is to write loops." — Boris Cherny, head of Claude Code

Osmani's own position is enthusiastic but hedged: he thinks this may be the future of working with coding agents, but it's early, token costs vary wildly depending on whether you're token-rich or token-poor, and the slop concerns are legitimate.

The claim that makes it worth writing down: **this stopped being a tool problem**. A year ago a loop meant a pile of bash you maintained forever; now the pieces ship inside the products, and the same building blocks exist in both Codex and Claude Code. Loop engineering sits one floor above agent harness engineering — the harness, but it runs on a timer, spawns helpers, and feeds itself.

## Five Building Blocks, Plus Memory

1. **Automations** — scheduled runs that do discovery and triage by themselves
2. **Worktrees** — so parallel agents don't step on each other
3. **Skills** — project knowledge written down instead of guessed
4. **Plugins & connectors** — the loop touching the tools you already use
5. **Sub-agents** — one has the idea, a different one checks it

Then the sixth thing: **memory**. A markdown file, a Linear board, anything living outside the single conversation that holds what's done and what's next. It sounds too dumb to matter, but the model forgets everything between runs, so the memory has to be on disk and not in the context. **The agent forgets, the repo doesn't.**

## What Each Block Is Actually For

**Automations are the heartbeat** — what makes a loop a loop rather than one run you did once. Findings come to you (Codex archives empty runs and routes the rest to a triage inbox); you stop being the one going around checking. Point an automation at a *skill* rather than a wall of pasted instructions, or the schedule becomes something nobody ever updates.

Worth separating two in-session primitives: `/loop` re-runs on a cadence, while **`/goal` runs until a condition you wrote is actually true** — and a separate small model grades completion after each turn, so the agent that wrote the code isn't the one deciding it's done. Both tools have `/goal`.

**Worktrees** remove the mechanical collision. A git worktree is a separate working directory on its own branch sharing repo history, so one agent's edits literally cannot touch another's checkout. But they only fix the mechanical half — **your review bandwidth still decides how many agents you can actually run**, not the tool (the orchestration tax).

**Skills are where intent stops costing you over and over.** An agent starts every session cold and fills any hole in your intent with a confident guess. A skill is that intent written on the outside — conventions, build steps, the "we don't do it like this because of that one incident" — written once, read every run. Without skills the loop re-derives your project from zero every cycle; with skills it compounds. Keep straight that the **skill is the authoring format and the plugin is how you ship it**.

**Connectors** (built on MCP, so one usually works in both tools) are the difference between an agent that says *"here is the fix"* and a loop that opens the PR, links the ticket, and pings the channel once CI is green.

**Sub-agents** are, per Osmani, the most useful structural piece: the model that wrote the code is far too nice grading its own homework. A second agent with different instructions — often a different model, different reasoning effort — catches what the first talked itself into. The usual split is one explores, one implements, one verifies against the spec. It matters *inside a loop specifically* because the loop runs while you aren't watching: **a verifier you trust is the only reason you can walk away**. Sub-agents burn more tokens, so spend them where a second opinion is worth paying for.

## Tool Equivalence at a Glance

| Building block | Codex | Claude Code |
|---|---|---|
| Automations | Automations tab, triage inbox, local-or-worktree runs | `/loop`, cron tasks, hooks, GitHub Actions |
| Stop-condition loop | `/goal` (pause/resume/clear) | `/goal` (separate small model grades completion) |
| Worktrees | Built-in multi-thread isolation | `git worktree`, `--worktree`, `isolation: worktree` |
| Skills | `SKILL.md`, invoked via `$` or `/skills`, or by description match | `SKILL.md`, same invocation model |
| Connectors | MCP | MCP |
| Sub-agents | `.codex/agents/*.toml` | `.claude/agents/`, agent teams |

Once you notice the shape is the same, you stop arguing about which tool and design a loop that works in either.

## One Loop, Assembled

A morning **automation** runs a **triage skill** over yesterday's CI failures, open issues, and recent commits, writing findings to a state file. Each finding worth doing gets an isolated **worktree** and a **sub-agent** to draft the fix, plus a **second sub-agent** to review that draft against the project skills and tests. **Connectors** open the PR and update the ticket; anything the loop can't handle lands in the triage inbox for you. The **state file is the spine** — what got tried, what passed, what's still open — so tomorrow's run picks up where today stopped.

You designed it once. You prompted none of those steps.

## Slow Loops: The Boring Version That Works

Dex Horthy's team runs the least ambitious loop imaginable, and it's the one he actually recommends: a cron job in GitHub Actions each night runs a linter, **fixes one thing, commits, pushes**. You wake up to a single small PR that makes the codebase a little better. A developer still reads it and approves it.

The reason to prefer this over the big-bang version is review-shaped: nobody merges a 60,000-line PR that fixed every lint error in the repo, so that loop produces nothing you can ship. One small PR a morning is a loop whose output actually clears the human gate.

It scales along two separate dimensions, and it's worth keeping them apart:

- **More feedback mechanisms** — add another checker and you get another PR. Their team runs React Doctor on the front end plus checks with no deterministic tooling at all, just a skill saying *here's what good looks like, here's what bad looks like, go fix one thing* (e.g. narrowing props that don't need to be optional). Four checkers, four PRs.
- **More scope per run** — as you gain confidence in a given checker, go from fixing one thing to fixing four.

Start at one thing on one checker and widen only where the output has earned it. Note what these loops are pointed at: **improving the codebase, not shipping the features users asked for** — the team reads all that code because they care how it's architected.

## What the Loop Still Doesn't Do For You

Three problems get *sharper* as the loop gets better, not easier:

- **Verification is still on you.** A loop running unattended is a loop making mistakes unattended. Splitting verifier from maker is what makes the loop's "it's done" mean something — and even then, *"done" is a claim, not a proof*.
- **Your understanding rots if you allow it.** The faster the loop ships code you didn't write, the wider the gap between what exists and what you grasp — comprehension debt, growing faster the smoother the loop runs.

- **The lights-off version has a shelf life.** Horthy's team built a fully automated factory in July 2025 and shut it down by November: roughly three to six months of shipping without anyone reading the code before it's easier to start over than to fix. When a bug finally needed a root cause no model could find, they spent weeks re-onboarding into their own codebase. Bad architecture is uniquely invisible to loops because *its cost function can't be evaluated by running the tests* — it hits months later, so nothing in the loop's feedback ever catches it.

- **The comfortable posture is the risky one.** When the loop runs itself it's tempting to stop having an opinion and take whatever comes back — cognitive surrender. Designing the loop is the cure when done with judgement and the accelerant when done to avoid thinking. Same action, opposite result.

## Core Insight

**The leverage point moved; the work didn't get easier.** Two people can build the exact same loop and get opposite results — one moves faster on work they understand deeply, the other avoids understanding the work at all. The loop doesn't know the difference; you do. That's what makes loop design *harder* than prompt engineering.

Practically: design the loop against the shape rather than the vendor, since both tools now have all the pieces. And don't retire direct prompting — it's still effective, and the balance is yours to find. Build the loop, but build it like someone who intends to stay the engineer, not just the person who presses go.

## Connections to Other Concepts

- **Orchestration tax** — worktrees remove file collisions, but your review bandwidth is the real ceiling on parallel agents
- **Intent debt** — skills are the mechanism that stops the loop re-deriving your intent every cycle
- **Comprehension debt** and **cognitive surrender** — the two failure modes a well-running loop accelerates
- **Long-running agents** — the on-disk memory trick loop engineering inherits
- **Compound engineering** — same compounding logic, applied to the loop's own state and skills rather than to individual work units

- **Verification** — slow loops work because linters and tests make the target verifiable; loops are only as good as the feedback you can automate