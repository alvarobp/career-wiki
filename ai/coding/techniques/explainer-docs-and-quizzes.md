# Explainer Docs and Comprehension Quizzes

**Source:** [Understanding is the new bottleneck — Geoffrey Litt, Notion](https://www.youtube.com/watch?v=WkBPX-oDMnA) - AI Engineer, 2026-07-10

**Companion piece:** [Understanding to Participate](../../ai-engineering/principles/understanding-to-participate.md)

## Summary

When an agent writes code, the diff is the rawest possible explanation of what happened. Geoffrey Litt's `explain-diff` skill treats the moment after a change as a teaching opportunity instead: the agent produces a structured explainer doc that builds background first, conveys intuition before details, adds interactive figures where they help, and presents the code as a *literate diff* with prose ordering rather than a file list.

The doc ends with a five-question quiz. Litt's rule is that he doesn't send code to teammates for review unless he can pass the quiz on what his agents wrote. The quiz exists because reading is easy to fake — you can finish a document and still not be able to answer a basic question about it.

## The structure of a good explainer doc

Ask the generative question: *if you sent a team away for a year to build a personalized curriculum explaining this one code change to me, what would it look like?* The skill's answer has four parts, in order:

- **Background first.** Not "what changed" but "here's how the system works" — the engine, the coordinate system, the subsystems. Lead the reader to the point where the change is even legible. Personalize: skip what they already know.
- **Intuition before details.** A one-line essence before any code. Litt's example: *"the goal of this commit is to make the garden feel three-dimensional using only 2D drawing tricks."* Think of it as a well-written commit message, a little deeper. This is what good math teachers do.
- **Interactive figures.** Where it makes sense, give something to fiddle with — dragging rocks around a simulation to watch coordinates and Z-layers change. **Use tastefully**: interactivity can be a crutch and can be slop, but done well it delivers understanding static pictures can't.
- **Literate code diffs.** Only now show code, and not as an ordered file dump. Give prose, explain in the right order, say what's coming before each file.

Output format is flexible — HTML, markdown, or a Notion page (collaborative, so teammates can comment). Litt prints them out and reads them at a coffee shop: AI turned code review from IDE-bound work into reading a textbook about your own PR.

## The quiz as speed regulator

The motivating failure: Litt sent a PR he believed he'd read and understood, and a coworker asked the most basic question about it. He didn't know. He had fooled himself.

- Inspiration is **Andy Matuschak's "Books don't work"** — it's trivially easy to read something and not notice you didn't understand it. With Michael Nielsen, he embedded spaced-repetition quizzes directly in essays so you can't get through without retaining the content.
- Applied to code: **five questions, medium difficulty**, at the bottom of every explainer doc.
- **The rule:** don't send code out for human review unless you can pass the quiz about what your agents wrote.
- It sounds silly, and it catches you a shocking number of times.

The framing that matters: everything about AI is an incentive to go faster. Correctness checking is increasingly automatable, so **the loop can run at the speed of correctness while your understanding falls behind**. The quiz is a deliberate **speed regulator** — a mechanism that forces the human's pace of understanding back into the loop, preventing the cognitive debt that leaves you unable to participate.

## Practical implications

- **Make explanation an artifact, not a conversation.** A doc that lives in a shared space can be commented on, revisited, and read away from the keyboard; an ephemeral chat explanation can't.
- **Order is the whole trick.** Background → intuition → figures → literate diff inverts the default (diff first, context never). The default order is what makes agent output hard to keep up with.
- **Self-assessment beats self-report.** "I read it" is not evidence. A quiz you can fail is.
- **Pair with hands-on tooling.** Docs and quizzes cover the reading path; [Microworlds: Agent-Built Environments for Understanding Code](./microworlds.md) covers the intuitive, inhabited path for understanding that resists prose.
- The `explain-diff` skill is public, in HTML-output and Notion-output variants, and is deliberately simple — worth adapting rather than adopting verbatim.

## Core insight

Agents can explain their own work far better than a diff can — but explanation alone is unverified. The quiz closes the loop by making understanding *testable*, converting a vague intention to stay in the loop into a gate you either pass or don't. That gate is what keeps the human's speed of understanding tethered to the agent's speed of production.
