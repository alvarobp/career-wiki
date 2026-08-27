# Microworlds: Agent-Built Environments for Understanding Code

**Source:** [Understanding is the new bottleneck — Geoffrey Litt, Notion](https://www.youtube.com/watch?v=WkBPX-oDMnA) - AI Engineer, 2026-07-10

**Companion piece:** [Understanding to Participate](../../ai-engineering/principles/understanding-to-participate.md)

## Summary

A **microworld** is a small piece of software an agent builds for you whose only purpose is to let you *feel* how a system works. It is not meant to ship. You inhabit it for an afternoon, extract intuition, and throw it away. Geoffrey Litt's framing: agents can write code to help us understand code.

The technique borrows from Seymour Papert's idea of **Mathland**. Kids learn French by living in France — so where do they go to learn math? Papert's answer was to give them a programmable turtle robot to draw with. The robot was never the point; the changed kids were the point. Applied to software: build a place where the system's behaviour is directly perceivable, and live in it.

## Example: A Timeline Debugger for an Interpreter

Litt was implementing a Prolog interpreter for his own learning. The algorithms read as forbidding on Wikipedia, but felt obvious once they clicked — the difficulty was in the presentation, not the idea.

So he had Claude build a bespoke debugger:

- **Ephemeral UI** built specifically to visualise the internals of *his* interpreter — not a general-purpose tool
- **Scrubbable timeline** stepping through interpreter execution, with all internal state rendered at every step
- **Comments pinned to the timeline**, so he could leave notes to himself about what he was thinking at each point

He used it to fix narrow bugs, but the real payoff was **peripheral vision**: while chasing a bug he was building a feel for the machine. Hand the same bug to an agent and the fix lands, but the peripheral vision never accrues.

## Example: A Migration You Play Through

Migrating a personal website between frameworks, the first attempt was the obvious one — "Claude, write me a script." It ran, files moved, it seemed correct. But reading the script produced no feel for what had happened.

The second attempt: **"make me a video game where I do the port myself."**

- Old site on the left, new site on the right
- Click **next** repeatedly; each step shows the exact commands being run
- The new site comes to life incrementally; file trees below show files relocating

The result is *as if* he had done the migration by hand — the same sequence of small comprehensible steps — but the labour is one button. **The iterative understanding without the iterative pain.**

## Design Notes

- **The artefact is disposable, the understanding is not.** Judge a microworld by what it leaves in your head, not by its code quality.
- **Specificity is the feature.** These are built for one system, one commit, one migration. Generality would dilute them.
- **Prefer inhabiting over reading.** A microworld gives an intuitive, richer grasp than a written document can — this is the same instinct behind interactive figures in [Explainer Docs and Comprehension Quizzes](./explainer-docs-and-quizzes.md), taken further.
- **Interactivity can be slop.** Used as a crutch or as decoration it adds nothing; the bar is whether it conveys something static pictures can't.
- **Reframe the ask.** When an agent hands you a working-but-opaque script, the useful follow-up isn't "explain this" — it's "build me something I can operate that does this step by step."

## Core Insight

Now that code is effectively free, software you write purely to understand something is suddenly rational — debuggers, playgrounds, dynamic simulations, all built for an audience of one and discarded after use. This isn't a novel AI affordance so much as the original promise of personal computing finally becoming cheap: Alan Kay's kids modifying game code to learn physics, Papert's Mathland. **The point was never the computer, and it isn't the agent — it's you, changed by having been there.**
