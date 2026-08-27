# Managing Context for AI Coding

**Sources:**
- [How to Manage Context in AI Coding](https://refactoring.fm/p/managing-context-for-ai-coding) - Luca Rossi, Nov 05, 2025
- [Dex Horthy on context engineering, loop engineering and software factories](https://www.youtube.com/watch?v=Usufn8IQJgw) - The Pragmatic Engineer Podcast

## Summary

Context engineering — the discipline of designing systems and workflows that reliably provide AI with the right information — is emerging as the foundational skill separating teams that succeed with AI from those that don't. Unlike prompt engineering, which focuses on tactical wording, context engineering treats AI assistance as a **multi-player, dynamic system**: shared across the team and capable of fetching what it needs automatically, rather than relying on humans to pass information every time.

## Context vs. Prompt

- **Prompt engineering** = nailing specific wording (tactical, often "magical incantations")
- **Context engineering** = grounding the model in accurate, exhaustive information (strategic, durable)
- Two qualities make context "engineered":
  - 👯 **Multi-player** — designed for the whole team, with shared workflows
  - ⚙️ **Dynamic** — AI fetches content itself rather than humans pasting it

## The What, How, and Why of Context

Good context separates three categories:

- ☑️ **Task-specific instructions (what)** — what needs to be done
- 🔄 **Procedures / principles (how)** — standards like testing, naming conventions, feature flags
- 🔭 **Strategic reasoning (why)** — values, business domain, quarterly goals, ADRs

**Key trend:** continuously *shrink the what and grow the how*. Standards like "write tests" should be embedded, not repeated in every prompt or ticket.

## Focus on Inputs, Not Outputs

When AI output is sub-par, the cause is usually missing context, not sloppiness. Nurture a feedback loop: every failure should improve the inputs, not just patch the result.

## Mandatory vs. Best-Effort Context

Borrowing from Andy Grove's *task-relevant maturity*, identify per task:

- 🟢 **Mandatory context** — must be fetched correctly 100% of the time
- 🟡 **Best-effort context** — nice-to-have, occasional retrieval failures acceptable

If AI misses mandatory context even occasionally, trust collapses and engineers stop using it for complex work.

### Co-locating Mandatory Context

Store critical info **alongside the code** in the repo:

- `CLAUDE.md` / `AGENTS.md` — how AI should write code
- `README.md` — build / test / run instructions
- `SYSTEM-DESIGN.md` — main design features of the repo
- `ROADMAP.md` (git-ignored) — agent-maintained plan files for tasks; useful for restarting after context rot and parallelizing agents

Avoid relying heavily on conversation threads/memories — consolidate useful info into files.

### Centralizing Best-Effort Context

Slack threads, ADRs, Notion, Linear, GitHub history aren't co-locatable. Individual MCPs cause "death by a thousand cuts":

- Too many MCPs confuse agents about when to use what
- Agents may skip MCPs or stop calling them prematurely
- Many MCPs are too simplistic and waste context window / reasoning
- Centralize access through a single tool (author plugs Unblocked) — also enables delivery in Slack/Teams for onboarding and code archaeology

## Keep Context Small

The simplest way to make context work — for humans and AI alike:

- **Low coupling** — componentized, isolated code requires less to fetch and update
- **Convention over configuration** — great defaults reduce cognitive load
- **Simple tech stack** — same language everywhere, buy over build, well-understood tooling

## The Smart Zone and the Dumb Zone

Dex Horthy (Human Layer) frames the same instinct in terms of where you sit in the context window:

- 🧠 **Smart zone** — roughly the first 100k tokens (up to ~200k on the beefiest models like Codex or Opus 4.8). Work done here holds together.
- 🌫️ **Dumb zone** — past that, attention spreads thin, instructions get half-attended, and results degrade.

The underlying rule from Jeff Huntley's Ralph Wiggum work: *the less context window you use, the better outcomes you'll get, always.* Longer context windows let you talk for longer; they don't make the model smarter. Bigger windows also don't move the ceiling — a 1M-token variant of a model isn't a smarter model, just a roomier one.

The thresholds are training wheels, not laws — with good intuition you can push to 250–300k for certain work. The reliable tell that you've crossed over: the model starts flailing on a failing test, trying increasingly extreme things ("let me just delete this file and try again"). At that point, dump what you've learned to a file and start a fresh session at 30–50k.

### Two Budgets, Not One

- 📚 **Information budget** — what facts are in the window (the RAG framing most people default to)
- 📋 **Instruction budget** — how many directives the model can actually follow. Frontier models circa 2025 held ~150–250 instructions before compliance dropped off; conflicting instructions are worse than merely numerous ones, since the model burns computation noticing it must ignore an earlier path you abandoned mid-conversation.

### Four Dimensions That Matter

When diagnosing a degrading session, check all four:

1. **Size** — how many tokens are in the window
2. **Correctness** — is there incorrect information (e.g. a thinking trace where the model concluded something false)
3. **Completeness** — is context missing that it should have
4. **Trajectory** — the *history of what the agent has actually done*

Trajectory is the subtle one. Models are autoregressive: they predict the next message given the conversation so far. If the agent made a change, ran the tests, saw a break, and fixed it, it will likely repeat that pattern next turn. If it made a change and skipped the tests, you're now on a worse trajectory that reinforces itself.

### "You're absolutely right" as a Restart Signal

That phrase is what the model says when you've expressed frustration or pointed out a mistake — and most of us have watched it say that and then continue doing the wrong thing. Read it as evidence of a poisoned trajectory: the conversation now contains a pattern of *model errs → human corrects → model errs again*, and the model will keep predicting the next entry in that sequence. Don't argue it back on course; compact what's worth keeping and start a new session.

## Core Insight

The winning teams aren't writing better prompts — they're building **shared, dynamic context systems**. Mandatory context lives in the repo (100% reliable retrieval); best-effort context is centralized through one tool rather than scattered MCPs. Treat every AI failure as a context bug to fix at the input layer, and aggressively shrink the *what* in favor of embedded *how*. Simplicity in code architecture compounds directly into AI effectiveness.
