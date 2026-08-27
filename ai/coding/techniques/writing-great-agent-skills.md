# The Missing Manual: How to Write Great Agent Skills

**Source:** [Building Great Agent Skills: The Missing Manual](https://www.youtube.com/watch?v=UNzCG3lw6O0) - AI Engineer, 2026-06-29

## Summary

The proliferation of freely available agent skills has created "skill hell" — a state where developers accumulate skills they can't evaluate, piece together, or get real results from, because there's no shared rubric for distinguishing a good skill from a bad one. Matt Pocock (author of the popular "Matt Pocock skills" repo) offers that missing rubric: a four-part checklist covering the skill's **trigger**, **structure**, **steering**, and **pruning**.

The through-line is minimalism and predictability: keep the `skill.md` as small as possible, control how skills get invoked, use precise language to steer agent behavior, and aggressively cut anything that doesn't change what the agent does. The entire framework is itself encoded as a skill ("writing great skills") in his repo, so it can be applied to author new skills or audit community-authored ones.

## 1. Trigger — How the Skill Is Invoked

Every skill can be invoked manually by the user. Some can additionally be invoked by the model itself. The distinction is the **description** field, which acts as a **context pointer**.

- **Model-invoked skills:** The description sits in the agent's context window. The agent reads it and decides whether to pull the full `skill.md` into context. More flexible — the model *or* the user can trigger it.
- **User-invoked skills:** The description is hidden from the agent (e.g. `disable model invocation: true`). Only the user can trigger it. The context pointer is optional, and here it's removed.

**Tip #1 — Decide if your skill is user-invoked or model-invoked.** Both choices carry a cost:

- **Context load** (model-invoked): every model-invoked skill adds a description that costs tokens on *every request* and gives the agent one more thing to reason about. 100 model-invoked skills = 100 descriptions in context.
- **Cognitive load** (user-invoked): the more user-invoked skills, the more the user must keep in their head — "more skill required from the pilot."

**Matt Pocock skills vs. Superpowers:** Superpowers is primarily *model-invoked* (gives the agent superpowers). Pocock prefers *user-invoked* to stay in full control, minimizing context load at the cost of his own cognitive load. His rationale: model invocation buys **unpredictability** — the model may skip a perfectly relevant skill — which then forces you to *eval* your skills to confirm they fire correctly. User invocation removes that entire class of problem.

## 2. Structure — The Internal Layout

Think of most skills as composed of two units:

- **Steps:** the step-by-step procedure the skill walks through.
- **Reference:** supporting information that helps execute those steps.

A skill can be all steps, all reference, or a mix. Example — the `2 PRD` skill (creates a Product Requirements Document from context): **3 steps** (find relevant context → confirm test seams with the user via a human-in-the-loop checkpoint → write the PRD) supported by **2 reference pieces** (a note on "what is a test seam" and a PRD markdown template).

**Tip #3 — Make the main `skill.md` file as small as possible.** Smaller skills are easier to maintain, easier to audit, fewer words to reason about, and every word shaved is tokens saved.

**Hide branching reference material behind context pointers.** Identify the skill's **branches** (different ways it can be used):

- If reference material is needed on *every* branch, keep it in `skill.md` (e.g. `2 PRD` has one branch — the PRD template and test-seam note are always needed).
- If reference material is only used on *one* branch, move it out. Example — `domain modeling` has 2–3 branches (update a `context.md` glossary, and/or create Architectural Decision Records, or neither). The ADR template and `context.md` template are pushed into **external references** — separate markdown files in the skills folder, reached via a context pointer that says "if you need X, go to this file."

## 3. Steering — Getting the Agent to Do What You Want

Fixes the core failure: *"I specified something clearly and the agent just didn't do it."*

**Leading words** (the key technique of the talk): certain words pack a lot of meaning into a small space. Put a leading word in the skill text; the agent repeats it back in its thinking tokens and output, re-emphasizing it, which changes its behavior.

- **Example:** Agents tend to "code layer by layer" (all DB, then all schemas, then all APIs, then frontend) instead of getting a small thing working and iterating. Rather than a wordy instruction, use the leading phrase **"vertical slice"** — well-known dev terminology that triggers the agent's priors. Repeat it throughout the skill.
- **You can verify it worked:** watch the reasoning traces for the agent saying "we'll do this as a thin vertical slice," followed by better implementation plans.
- English is "a pretty wide API" — hunt for more powerful, more consistent leading words. Agents are good at helping you brainstorm them.

**Legwork — make the agent do enough work per step.** Agents often under-invest in a step when they can see a more attractive future goal.

- **Classic case — plan mode:** its two steps (ask clarifying questions → create a plan) always shortchange the clarifying-questions step because the agent races toward the plan.
- **Solution — split steps into separate skills so the agent sees only one at a time.** Pocock split clarifying questions into a `grill with docs` skill; after it completes, `2 PRD` runs. Hiding the future goal forces more legwork on the current step. Not always needed, but unmatched when you need an extra chunk of effort on one phase.

## 4. Pruning — Failure Modes to Cut

Massive skills are usually a *symptom* of these failure modes:

- **Don't repeat yourself:** every part of the skill should have a **single source of truth** — no duplicating reference material (like the PRD template or test-seam note) across steps or sections.
- **Sediment:** shared markdown files accrete cruft as many people add material and nobody feels brave enough to delete others' contributions. Fix via **structure** — move added material to the correct branch, or delete it if irrelevant or stale.
- **No-ops:** text that *appears* to instruct but doesn't actually change behavior — common when an agent writes the skill. Example: a paragraph telling the agent to "write a long detailed commit message" — delete it and the agent still writes a good commit message. Use **deletion tests**: remove a chunk and see if behavior changes.

## Core Insight

The full sweep, as a repeatable audit:

- **Trigger:** Is it firing at the right times? Are you paying in context load (model-invoked) or cognitive load (user-invoked)?
- **Structure:** Split into steps and reference; keep branch-specific material out of the main `skill.md` behind context pointers.
- **Steering:** Condense instructions into consistent leading words and watch them surface in reasoning traces; break skills down to increase legwork on the current phase by hiding future phases.
- **Pruning:** A final pass for duplication, sediment, and — especially — no-ops.

The unifying principle: **a great skill is a small, predictable skill.** Skills stay small not by accident but by deliberately compacting instructions into leading words, enforcing a single source of truth, and deleting anything that doesn't demonstrably change the agent's behavior. The framework is available as the "writing great skills" skill in the Matt Pocock skills repo — usable both to author new skills and to audit community-authored ones before you trust them.
