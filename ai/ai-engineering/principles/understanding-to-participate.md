# Understanding to Participate

**Source:** [Understanding is the new bottleneck — Geoffrey Litt, Notion](https://www.youtube.com/watch?v=WkBPX-oDMnA) - AI Engineer, 2026-07-10

## Summary

Geoffrey Litt (design engineer at Notion) argues that it still matters for humans to understand how their code works, even as agents write most of it — but for a different reason than most people assume. The common mental model is that we understand in order to **verify**: agents do dumb things, and the human's job is correctness checking. Litt accepts that this role is genuinely shrinking, and says he doesn't hate that. Given a good verification loop, agents increasingly catch their own mistakes.

The deeper reason is **understanding to participate**. Development isn't one loop; it's loop after loop. Each time you actually engage with what happened, you come away changed, and that changed understanding is what you bring to the next loop. Rich conceptual structures in your head — recombinable fluently, without a round trip to an agent or a colleague — are what let you take creative leaps and have the *next* idea. That's the part better agents don't absorb. The rest of the talk is a set of education-inspired techniques for keeping that understanding current at agent speed.

## Verify vs. Participate

- **Understanding to verify** — "Is this correct?" Correctness has many definitions (matches the spec, doesn't take down prod, well architected), but all of them reduce to thumbs up / thumbs down decisions.
- Thumbs up/down judgments are exactly what agents get better at with the right verification loop. So the human share of correctness checking is **decreasing** — and that's fine.
- The wrong extrapolation: "as agents get smarter, we don't need to understand at all — get out of the loop."
- **Understanding to participate** — your accumulated model of the system is the foundation for being an active creative participant. Even pre-AI, people who deeply understood a system had qualitatively different ideas than people a few layers removed.
- This is the reason that *cannot* be engineered away by better agents.

## Cognitive Debt

- Term popularized by scholar Margaret-Anne Storey; also blogged about by Simon Willison.
- Analogy to technical debt: you can get away with degraded understanding for a while, but at some point you get burned.
- The recognizable failure mode: vibe coding is going well, then you realize you have no idea what's going on and **can't participate anymore**.
- Implication: understanding needs its own **speed regulator**. Everything about AI incentivizes going faster; Litt's framing is that we shouldn't move only at the speed of correctness, but at the speed of understanding.

## Borrowing From Education

Rather than inventing from scratch, Litt looks to the best ideas in education — a field that has already asked "how do humans understand things?"

- **Explanations** — treat every agent change as a teaching opportunity. Not a raw diff, but the explanation a dedicated team would produce if given a year to teach you this one change. Generative prompt: *what would the best possible explanation look like?*
- **Microworlds** — Seymour Papert's "Mathland": kids learn French by living in France, so build a place where you learn a system by inhabiting it. Have agents build ephemeral debuggers, visualizers, and simulations of your own code.
- **Shared spaces** — understanding is often a team property, not an individual one. Shared vocabulary for parts of a system is what makes communication possible. Notion is exploring multiplayer chat threads where several humans and several agents participate in one visible conversation (Slack channels vs. one-on-one DMs), and collaborative plan documents you can comment on with teammates. Notion recently shipped bringing coding agents (Claude, Cursor) into Notion itself.

## The Bigger Frame: Alan Kay

- Litt escalates the claim: it's important for humans to keep understanding how *everything* works, not just code — and this is now something we have to actively fight for.
- Not a new battle. Alan Kay's 1972 essay *A Personal Computer for Children of All Ages* pictured kids on tablet-like devices — not consuming media, but **modifying the code of a video game while playing it to learn physics**.
- "The point isn't the computer, it's the kids." Computers were meant to level humans up; somewhere they detoured from that.
- AI makes code effectively free, so ephemeral UIs, dynamic simulations, debuggers, and playgrounds-on-demand are suddenly cheap. That's not a new idea — it was the goal all along.

## Core Insight

Correctness checking is being automated; **participation cannot be**. Understanding is worth defending not because agents are unreliable but because your internal model of the system is the raw material for your next idea. Cognitive debt is the failure mode, and the counter is to deliberately spend agent capacity on your own comprehension — explanations, quizzes, microworlds, shared spaces — rather than spending all of it on shipping. With the right tools and mindset, AI can put us *more* deeply in the loop than ever, not less.

## Related notes

- [Explainer Docs and Comprehension Quizzes](../../agentic-coding/techniques/explainer-docs-and-quizzes.md) — Litt's `explaindiff` skill: background-first, intuition-before-details explainer docs with literate code diffs, closed out by a five-question quiz you must pass before sending code for review.
- [Microworlds: Agent-Built Environments for Understanding Code](../../agentic-coding/techniques/microworlds.md) — having agents build throwaway debuggers, timeline scrubbers, and click-through simulations of your own system so you develop a feel for the machine.
