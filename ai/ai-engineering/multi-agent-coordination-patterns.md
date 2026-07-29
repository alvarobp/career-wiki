# Multi-Agent Coordination Patterns

**Sources:**
- [Multi-Agent Coordination Patterns](https://claude.com/blog/multi-agent-coordination-patterns) - Anthropic
- [Interview with Boris, creator of Claude Code](https://www.youtube.com/watch?v=qyPCVqFUyDo) - YouTube

## Summary

Five coordination patterns define how multiple AI agents can work together on complex tasks. Each pattern makes different tradeoffs around communication overhead, task decomposition, and failure modes. The key insight is to start with the simplest viable pattern — orchestrator-subagent — and evolve toward more complex patterns only when you hit specific limitations.

## The Five Patterns

### 1. Generator-Verifier

A **generator** produces output while a separate **verifier** evaluates it against explicit criteria, looping feedback back for revision when rejected.

- Best for **quality-critical output** with clear evaluation criteria (code generation, compliance checking)
- Fails when verification criteria are vague or when generation and evaluation require similar skills

### 2. Orchestrator-Subagent

A **lead agent** decomposes tasks, delegates to specialized subagents, and synthesizes results.

- Works well for **clear task decomposition** with bounded, mostly independent subtasks
- Becomes an **information bottleneck** when subagents need to share intermediate discoveries or when sequential execution is required
- **Recommended default** — handles the widest range of problems with the least coordination overhead

### 3. Agent Teams

Multiple **persistent workers** claim tasks from a queue and work autonomously over extended periods.

- Ideal for **parallel, independent, long-running subtasks** where agents benefit from accumulated context (e.g., codebase migrations)
- Requires careful task partitioning since teammates can't easily communicate intermediate discoveries

### 4. Message Bus

Agents **publish and subscribe** to events through a central router.

- Excels in **event-driven pipelines** with a growing, unpredictably evolving agent ecosystem
- Drawbacks: silent failures from misrouted events, debugging complexity, and tracing difficulty since workflows emerge from event cascades rather than predetermined sequences

### 5. Shared State

Agents read from and write to a **persistent store** without a central coordinator.

- Supports **collaborative work** where agents build on each other's findings in real time
- Risks: duplicate work and **reactive loops that don't converge** without explicit termination conditions

## Choosing a Pattern

Three questions guide pattern selection:

- **Do subtasks need persistent context?** → Agent Teams
- **Are workflows predetermined or emergent?** → Orchestrator-Subagent vs. Message Bus
- **Do agents require each other's intermediate discoveries?** → Shared State

## Core Insight

Start with **orchestrator-subagent** as the default, then let its failure modes guide you toward other patterns. The coordination pattern should match the structure of the problem — not the other way around. Over-engineering coordination is itself a source of failure.

## Where This Leads: Orchestration as Test-Time Compute

In the [interview with Boris](https://www.youtube.com/watch?v=qyPCVqFUyDo), Claude Code's **dynamic workflows** are described as the direct continuation of these patterns at scale — orchestrating dozens, hundreds or thousands of agents from a single prompt.

- The design comes from functional programming: an **algebra for agents**, with primitives to run agents **in sequence** and **in parallel**, composed inside a sandbox
- A single task fans out into stages — a first pass by many agents, a second stage that verifies or summarises the work, a third fan-out — which is orchestrator-subagent and generator-verifier composed rather than chosen between
- Framed as a **new form of test-time compute**: after neural net size, training data and training flops came token generation at inference, and orchestration is now a further axis for scaling the compute spent on a hard task

See [Long-Running Agents and Dynamic Workflows](../agentic-coding/techniques/long-running-agents-and-dynamic-workflows.md) for the practical side — verification loops, steering, and tasks that run for days or weeks.
