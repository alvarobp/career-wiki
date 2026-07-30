# The Orchestration Tax

**Source:** [The Orchestration Tax](https://x.com/addyosmani/status/2059844244907696186?s=12) - Addy Osmani

## Summary

Starting an agent is cheap; closing the loop on one is not. Every agent's output eventually needs someone to judge whether it's correct and reconcile it with what the other agents touched — and there is exactly one of you. **Running multiple agents does not mean there is more of you.** The **orchestration tax** is the structural gap between what your agents produce and what you can actually review and merge.

Osmani's framing (named by Richard Seroter on a Google I/O panel with Aja Hammerly and Ciera Jaspan) is that this is not a discipline problem but an **architecture problem**. You are a component inside a concurrent system — the slow, serial one — and the fix is to architect your own attention the way you'd architect any system with a known bottleneck.

## You Are the Single-Threaded Resource

Three borrowed intuitions from concurrent and performance engineering:

- **You are the GIL.** Python lets you spawn any number of threads, but only one executes bytecode at a time because they must acquire the lock. Agents run freely until their work needs genuine architectural understanding or merge-conflict resolution — that work must acquire the lock, and you hold the only one.
- **Amdahl's Law caps the payoff.** Speedup from parallelism is bounded by the fraction of work that stays serial. In agent development, **the serial fraction is the judgement.** Spawning 8 agents doesn't speed up your judgement; it just deepens the queue feeding into it.
- **Optimizing the non-bottleneck doesn't increase throughput.** It grows the pile of unfinished work in front of the bottleneck. Adding agents optimizes the part that was never the constraint. The constraint is review, and system throughput equals review throughput exactly.

## Why It Feels Like Tiredness

"I never felt more productive with my tools, but I'm also more tired than I've ever been." Both halves are real and share a cause: running a serial processor at 100% with no slack.

- Every check-in on an agent is a **context switch** — flush your brain, reload a different context cold. CPUs do this in microseconds and architects still design to avoid it; you do it in minutes and never reload perfectly.
- Five agents isn't 1x workload done five times. It's **five cold reloads plus a background process** constantly worrying about which agent you should be checking.
- You can't out-grind a structural limit. The tax gets paid regardless — it just resurfaces as shallow reviews or **cognitive surrender**, where you accept the agent's code because forming your own opinion costs attention you no longer have.

## Architecting Your Attention

- **Scale the fleet to your review rate, not the UI.** Concurrent systems use backpressure: the producer slows to match the consumer. Agent count is the producer, review rate is the consumer. The right number of parallel agents is how many you can properly code review — **for most people, low single digits.** The tool will happily let you spawn 20; that's a UI feature, not a capacity signal.
- **Sort the work into two piles.** *Isolated* work that can be delegated to background/cloud agents and only needs you at the final gate. *Complex* work where the judgement **is** the work — a weird bug, an architecture decision. The mistake is trying to parallelize the second pile: it thrashes the lock and everything comes out worse.
- **Batch your reviews.** Reviewing four agents in one sitting is far cheaper than checking one, leaving, and returning cold. Give agents a long leash and let work pile up a bit.
- **Spend the lock only on judgement.** Don't burn attention on what the machine can verify itself — make the agent write a passing test or produce a screenshot. Agents can prove the boring 80%; reserve your attention for the 20% that genuinely needs a human.
- **Protect your serial time.** The bottleneck deserves your best hours, not the leftover minutes between check-ins. Sometimes the highest-leverage move is to close the laptop full of agents and think hard about one problem with the lock held the whole time. **Orchestrating is overhead around the work, not the work.**

## Core Insight

**Feeling busy is not the same as being productive, and the failure mode is invisible from the inside.** Twenty running agents produce a full dashboard and a sensation of massive throughput that is fully decoupled from shipping good code to main.

Unpaid, the orchestration tax accrues as technical *and* cognitive debt simultaneously (per Margaret-Anne Storey's work, raised by Ciera Jaspan on the panel): you merge code you didn't read carefully, your mental model of the codebase goes stale, and none of it shows up until production breaks and you realize you no longer understand your own system.

Spawning agents is not the skill — anyone can run 20. The skill is designing the system around **the one serial resource that cannot be cloned or parallelized: your attention.** Either the system respects that number, or it routes around it by quietly lowering your standards.
