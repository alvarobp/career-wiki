# Agentic Systems

Anthropic distinguishes two types in [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents):

- **Workflows** are systems where LLMs and tools are orchestrated through predefined code paths.
- **Agents** are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks. Main characteristics of agents:
    - Open-ended
    - Feedback loops
    - No fixed path
    
    ![image.png](Agentic%20Systems/image.png)
    

### Risks of Agents

- Unpredictable path
- Unpredictable output
- Unpredictable costs

Mitigations for these risks are:

- Monitoring
- Guardrails: ensuring the agents behave safely, consistently and within your intended boundaries.