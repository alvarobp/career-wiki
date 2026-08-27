# Token Harder vs Token Smarter

**Source:** [Context engineering with Dex Horthy](https://www.youtube.com/watch?v=Usufn8IQJgw) - The Pragmatic Engineer, 2026-07-15

## Summary

Dex Horthy (founder of HumanLayer, who coined **context engineering**) built a "lights-off software factory" in July 2025 — agents shipping code from tickets, support requests, and crash reports with no developer reading a line — and shut it down by November. The failure mode wasn't dramatic: the codebase quietly degraded until a single bug took weeks to trace by hand, because nobody had read the code in three months. His conclusion is that the constraint on agentic development isn't token throughput but **program design**, and models aren't trained to optimise for it.

Out of this comes his framing of two competing strategies. **Token harder** means maximising utilisation — more agents, more parallel sessions, more tokens through the pipe, humans removed from every checkpoint that slows the flow. **Token smarter** means finding the few leverage points where an hour of human judgement saves four hours of implementation and rework, keeping the lights on while still moving 2–3x faster.

## The Lights-Off Software Factory

The term **software factory** predates AI by decades — it comes from a NATO conference in **1968**, was picked up by Toshiba and others, ran through the DevOps era (CI/CD, Chef, Puppet, Nagios feedback loops), and was formalised for the US Air Force in a 2018 essay on the "DevSecOps factory."

The pre-AI factory was a loop: planning → tickets → build → PR review → CI → prod → user complaints and crashes → back into the tracker. The agentic version replaces each stage in turn:

- **Replace the builder** with an agent (sandbox, LLM, inner harness, outer harness) — build time drops from hours to minutes
- **The bottleneck moves to code review** — so throw agentic review and agentic testing at it
- **Close the outer loops** — support queue feeds agents directly, Sentry/Datadog crashes become PRs automatically
- **Turn the lights off** — remove human review entirely, treat the system as a black box: "if users complain it's broken, if they don't it's working"

The name comes from automated car factories with no lights, because there are no humans. "Raw materials go in, cars come out."

## Why It Failed

- **Three to six months** of shipping without anyone reading the code before you notice it's getting worse — and by then rewriting is easier than fixing
- The team hit a bug that **Opus 4.1 could not root-cause** no matter how sophisticated the prompting. It took several days of manual digging to find a primary key that needed to be a different object type
- Recovery cost **three weeks of onboarding back into their own codebase**
- At the time Dex judged it worth it: occasional two-week manual fixes in exchange for never reading code. He no longer believes that, because output volume has 10x'd or 100x'd and the problem scales with it

## The Training Gap

The core argument for why this isn't a temporary limitation:

- Models got good at coding through **RL on SWE-bench-shaped problems** — here's a Django commit, here's an issue, reproduce the human's fix. Claude Code was good because the model and harness were trained *together*
- That optimised one dimension. The dimension nobody trains for is: **will this code make the codebase better or worse in three months?**
- The reason is structural: **the cost function of bad architecture can't be evaluated by running the unit tests.** It hits you 3–6 months later when the software has become hard to change
- Newer benchmarks (frontier-code from Cognition, marathon) add judge models checking functional equivalence to a golden patch plus code-quality review — better, but not sufficient
- **Agentic code review has the same problem**: ask a model if its own code is good and it says "yes, comprehensive, has unit tests." Ask it to review a coworker's PR and it finds problems. Sycophancy makes models untrustworthy as quality evaluators
- Dex's proposed benchmark: have a model build 20 features in a row without knowing what's coming next, like a real product team, and see if it degrades by issue six

This is the pre-AI tech debt story replayed at speed — the reason it took years to make a senior engineer is that the small mistake that snowballs into disaster only teaches you when it hits you.

## Token Harder

Dex's example: a group chat called **hyperengineering**, "all people trying to max out their Claude subs" — six Claude Code accounts, all maxed every 5-hour window, timed so usage restarts the instant limits reset.

His critique routes through **Eli Goldratt's *The Goal***: this is optimising **utilisation of one node** in the factory rather than end-to-end throughput of value. Removing humans from code review does push more tokens through the system. It doesn't ship more working software.

The underlying belief: *my job is to extract as much intelligence out of the machine god as I can.*

## Token Smarter: Seeking Leverage

Three options in the agentic factory world:

1. **Lights off** — let everything flow, pray the next model generation arrives before the slop does
2. **Read every line** — safe, but caps you at roughly **30–50% productivity lift**, which is what Dex sees when working with teams
3. **Seek leverage** — find the points where human judgement multiplies. Target: **2–3x faster at ~99% of hand-written quality**

The leverage argument in concrete terms: spend an hour on planning and design discussion up front so the PR takes 20 minutes to read because the code is right — versus piping every support ticket straight to a PR that takes six hours of back-and-forth. Once an agent has committed to a direction, steering it is harder than starting over.

**Where the lights can stay off**: micro-loops with tight verification. Code review agent finds a problem → builder agent fixes → back around. No human needed for that cycle.

**Where humans stay in**: designing the end state, architecture and program design, and the ordering of implementation steps. Models produce **horizontal plans** (database layer → services → API → frontend) which leave you unable to test anything until 2,000 lines in. A human would go vertical: mock endpoint → frontend → wire the services → migration → business logic → error handling, verifying at each slice.

The model to imitate is Google **SRE**: the goal was never zero engineers. It was scaling from 5 to 50 data centres with the team growing logarithmically while output grew linearly — achieved through good architecture, not by removing humans.

## Slop In, Slop Out

"AI can write your code, but it can also write your specs and PRDs. Same rule always: **slop in, slop out**. If you outsource your thinking, you're going to get garbage."

The escalation Dex recommends instead — each step reviewed before the next:

- Two sentences or a voice-note ramble
- → a one-pager (check it's right)
- → a three-pager (check it's right)
- → a 10-page detailed outline
- → 100 pages of code

Each review step **collapses the uncertainty** in the set of end states the agent can land in. Don't sweat over making the documents perfect — the point is narrowing the probability distribution, not producing artefacts.

## Core Insight

**The thing loops optimise is not the thing that constrains you.** Loops maximise token throughput; what actually determines whether you can keep shipping in six months is program design — and program design is precisely the dimension models aren't trained on, because its cost function is invisible to any test suite you can run today.

So the discipline isn't choosing between agents and humans, it's placing the human checkpoints where they buy the most: at the design and planning stage where taste compounds, not spread evenly across every PR where it just becomes a queue. Turning the lights off maximises utilisation of one node while starving the one that matters.

## Related notes

- [Harness Engineering](./harness-engineering.md) — the discipline of optimising the environment an agent runs in (commands, skills, MCPs, codebase layout), and the inner/outer harness distinction
- [Research, Plan, Implement (RPI)](./techniques/research-plan-implement.md) — the three-phase workflow with intentional compaction between stages that puts the leverage argument into practice
