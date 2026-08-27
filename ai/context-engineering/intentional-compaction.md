# Intentional Compaction

Sources:

- https://youtu.be/IS_y40zY-hc?t=288
- https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md

## Concept

Intentional compaction is a technique for recovering from agent confusion or task drift. When an AI agent becomes lost or unfocused during a complex task, you can prompt it to:

> "Write everything we did so far to progress.md, ensure to note the approach we're taking, the steps we've done so far, and the current failure we're working on"

This forces the agent to:
1. Review and synthesize the entire conversation history
2. Extract the core approach and methodology being used
3. Identify completed steps and current blockers
4. Create a focused summary that serves as a restart point

The resulting progress file becomes a clean slate for restarting the task in a new agent instance or conversation, eliminating the noise and confusion that accumulated in the original thread.
