# Critical Thinking When Agents Do the Work

**Source:** [Critical thinking when agents do the work](https://x.com/addyosmani/status/2117512471930167377) - Addy Osmani, 2026-11-03

## Summary

Addy Osmani argues that agentic workflows remove the friction that used to make us think. Most cognitive work used to happen between asking a question and getting an answer, and that gap is now a few seconds. As models improve, outputs are more often polished and mostly correct, so fewer of them prompt a second look. Running many agents doesn't help, because you still have only one pair of eyes on the results. **You have to build critical thinking into your day, because by default nothing will do it for you.** He isn't arguing for less agent use. He's arguing that you should stay deliberately in charge of the parts you'll be held accountable for.

The guide lays out a spectrum running from healthy **offloading** down to **cognitive surrender**. It then gives questions to ask before and after delegating, treats verification as a habit (a green check proves one thing only), asks you to review the agent's *decisions* as well as its diff, and treats the prompt as a test of your own understanding. It explains why better models won't remove human accountability, and it closes with small routines against skill atrophy.

## Offloading, Deferral and Surrender

A spectrum of how much ownership you keep:

- **Cognitive offloading** (top): you delegate the task but **keep ownership of the result**. This is healthy, and you should do it all day.
- **Deferral** (middle): the tool's output becomes your new input. It has stopped being a hypothesis.
- **Cognitive surrender** (bottom): the AI's output quietly becomes yours and you feel no need to check it. The term comes from Steven Shaw and Gideon Nave at Wharton.

**How the drift happens.** Each step is gradual and seems reasonable. You read the last answer well, so you skim the next one, then you only scan the skeleton of the one after that. Eventually someone asks you about a line and you can't explain it, even with the agent's help.

- Surrender is how **cognitive debt** builds up (Margaret-Anne Storey describes it in teams as an eroding shared theory of the system). In code it shows up as **comprehension debt** (Jeremy Twei's term). It's invisible at the time: the code looks clean and the tests pass, until a change reveals that nobody understands the system. Signing off on a strategy doc after reading its table of contents is the same failure.
- **You don't need the full mental model.** The Claude Code team rebuilds understanding on demand by asking Claude to explain the slice they need. This debt is more recoverable than people expect, *as long as you know what you don't have*.
- **The ownership test:** if you can't explain the answer, even by way of your agent, you've ceded ownership.
- **Delegate by stakes.** Osmani let an AI pick between three similar hotels and would do it again. He wouldn't do that for investments, career advice for his kids, or decisions about what to build or whether it's safe to ship. *Take the handoff where being wrong is cheap; keep the reasoning where others will live with the consequences.*

## The Questions to Ask Yourself

These are updated versions of the classic who/what/where/why/when/how prompts, which agents make easy to skip:

- **Did I form a hypothesis before asking?** Write down your guess first, even a bad one, because a well-written answer makes other possibilities hard to imagine. If you truly have no starting point, ask for a **blind spot pass** (Thariq Shihipar's term): give the model what you know and have it find your unknown unknowns.
- **Am I asking it to help me think, or to think for me?** Both are fine, as long as you know which one you're doing.
- **What would have to be true for this to be wrong?** Then go and check. A real test is worth more than the model's own confidence.
- **Have I heard the counter-argument from another angle?** On open-ended positions, ask more than one model to argue the opposite side, then form your own view.
- **Would I bet on this in front of the person who has to maintain it?** This is the bar for being answerable, and it applies to code and to anything else you deliver.
- **What am I no longer practicing?** Letting some skills go is fine, as long as it's a choice you made.

## Verification as a Habit

The bottleneck has moved from writing code to **being sure you're right**. Give agents ways to verify their own work (end-to-end tests, property tests, real app interactions; Boris Cherny's "give Claude a way to verify its work"). Then your job becomes building those loops and reviewing the evidence, instead of reading every line.

You can surrender verification too:

- "Is there evidence for my conclusion?" quietly turns into "Did the check go green?" Agents make tests cheap, so you'll see a lot of green. A test written with the same mistake as the feature will pass.
- **When a check goes green, ask what it proved. Then ask what it didn't.** A green check confirms one property and is easy to read as confirming everything.
- **Define "verified" up front.** After the fact, you'll rationalise any outcome.
- **The finish line should be tangible:** a passing test, a screenshot, a log or a trace, not "it looks done."
- **Evidence before summary.** When an agent reports it's finished, read the command it ran and its output *before* reading its summary.
- Build in a self-critique by a **subagent in a fresh context** so it runs every time, and still ask "**Did I miss anything?**" at the end. On complex work it often turns up two or three more items.
- A rule of thumb from the Claude Code team's code-review write-up: *"If you can't say what the checks would miss, ask for a real review rather than a quick approval."*
- **The same applies beyond code.** If an agent synthesised fifty customer calls or a competitive analysis, spot-check a few of the sources, and recompute any number your recommendation depends on.

**Agents have made verification cheap to set up. The hard part is knowing what good verification looks like.**

## Review the Decisions, Not Just the Diff

Picture a 600-line PR that you skim: the structure looks right, the names look reasonable, the tests pass. Somewhere in the middle there's an ordering change in a transaction boundary, or a flipped default on an edge case. *You reviewed it, but only for what you already knew to look for.* Writing code and reviewing it are different skills, and at some point reviewing turns into rubber-stamping.

- **Read the diff as if the AI didn't write it**, then look past it at what the agent *decided*: defaults, what it treated as out of scope, and which requirement it reinterpreted when two clashed. None of this shows up in an "everything went well" summary.
- **Ask it to list the decisions and assumptions it made.**
- **Quiz yourself.** Pick random lines and explain them. For a document, close it and write out its main argument from memory. For long sessions, have Claude write a report with a quiz at the end: *"I only merge after I pass the quiz perfectly."*
- **Use agents to guard your attention.** Osmani has agents triage incoming PRs on his open-source project to flag guideline violations and show where he's needed. He doesn't let them make the final call, but they free up attention for "is this the right problem, solved the right way?"
- **The orchestration tax** is the gap between what your agents produce and what you'd put your name on. If finished work piles up faster than you can review it, another session won't help. Tighten the checks so less of it needs you, or slow down.

**When you're producing more than you can stand behind, you're no longer reviewing. You're hoping.**

## The Prompt as a Test of Understanding

Human judgment has moved from the middle of the work to its **front (the brief and context) and back (the review)**. That makes prompting a critical-thinking skill.

- A colleague used to push back on a vague request, which is how you'd find out you hadn't thought it through. An agent fills the gaps and hands back something that *looks* done while the idea behind it is still fuzzy. That's **intent debt**: implicit goals, constraints and rationale missing from the artifacts. Only you can pay it down.
- **If you can't express the problem clearly in a prompt, it probably isn't clear in your head.**
- **Write the brief in your own words** before asking: the audience, what's out of scope, and the definition of done. If a second round of corrections hasn't got you there, stop tweaking and rewrite the prompt.
- **Collaborate rather than delegate** (Andy Clark's distinction). Each prompt sharpens the output, which sharpens your next prompt and your model of the problem. Have the agent **interview you** about what it doesn't understand. If you end the session with a sharper mental model, that's success.
- **Watch the input chain.** When agents pass each other summaries, the third agent may never have read the original document.
- **Polish is no longer a signal**, since everything comes out confident and well formatted. Keep your own bar: *if I wouldn't feel comfortable attributing the output to myself, I won't put it out.*
- When something misses the bar, record why in shared config, a hook or a test. That's how **taste compounds**.

## "But the Models Will Be Better at This Than Me"

The models may well take over much of the *detection*, and Osmani supports pushing it to them. What doesn't move:

- **Someone is responsible for what ships.** However much AI helped, a human has to take responsibility.
- **How much to trust an agent on a given task is itself a judgment call**, and staying calibrated means reviewing work, because what models get wrong keeps changing.
- Anthropic's internal research calls this the **paradox of supervision**: "supervising Claude requires the very coding skills that may atrophy from AI overuse."
- A better model won't answer these for you: *what are you building, why is it worth it, who does it affect, what are you willing to sacrifice?* An agent can help you work through them, but they remain yours.

**You may offload the work and much of the auditing, but not the accountability.**

## Everyday Practices Against Skill Atrophy

- **Weekly:** write some code without an agent, or do one real thing it would hurt to forget how to do. Osmani calls this a calibration exercise, not a moral one.
- **Monthly:** list what you've stopped doing and decide which of those you're fine giving up.
- Keep asking: **How lost would you be if AI didn't exist?**
- **If something is beyond your understanding, go and learn it** rather than pasting in a one-line explanation, so you see where it fits.
- **Schedule verification as a line item.** Checking the machine is real work, and teams that pretend it's free end up not doing it.
- **Skills you stop exercising fade faster than you'd guess.** Keep practicing the ones you're not willing to lose.

## Core Insight

Agents haven't taken critical thinking away. They've removed the friction that used to force it on you, so now it has to be **deliberate**. The danger isn't delegation, which is fine where being wrong is cheap. The danger is drifting unnoticed from offloading to surrender. The defences are concrete and cheap:

- **Before:** form a hypothesis, and write a brief clear enough to prove you understand the problem.
- **During:** know whether you're asking for help thinking or asking it to think for you.
- **After:** read the evidence before the summary, ask what the green check *didn't* prove, have the agent list the decisions it made, and quiz yourself until you could defend the result to whoever has to maintain it.

Osmani's own one-line exercise: *before you ask, write down what you think will happen; after the agent is done, write down one thing it didn't check.* You can hand off the work and much of the auditing, but you keep the accountability. **Think independently. Ask better questions. Take responsibility for the outcome.**
