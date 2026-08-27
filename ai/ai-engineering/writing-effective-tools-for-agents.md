# Writing Effective Tools for LLM Agents: Key Principles

*Summary of principles from Anthropic's engineering blog post*
https://www.anthropic.com/engineering/writing-tools-for-agents

## Overview

Traditional software establishes contracts between deterministic systems, while **tools represent a new kind of software** that creates contracts between deterministic systems and non-deterministic agents. This fundamental difference requires rethinking how we design software for agents.

## Development Process

### 1. Build and Test Prototypes
- Start with quick prototypes to understand what agents find ergonomic
- Use Claude Code or MCP servers for rapid development
- Test tools yourself to identify rough edges
- Collect user feedback on expected use cases and prompts

### 2. Create Comprehensive Evaluations
- Generate evaluation tasks grounded in real-world uses
- Use realistic data sources and complex scenarios
- Create prompt-response pairs with verifiable outcomes
- Measure accuracy, runtime, token consumption, and error rates
- Use agents to help analyze results and identify improvements

### 3. Collaborate with Agents
- Let agents analyze evaluation transcripts and suggest improvements
- Use agents to refactor multiple tools simultaneously
- Rely on held-out test sets to prevent overfitting

## Core Principles for Effective Tools

### Choose the Right Tools

**Quality over Quantity**
- More tools don't always lead to better outcomes
- Build thoughtful tools targeting high-impact workflows
- Avoid simply wrapping existing API endpoints without considering agent affordances

**Consolidate Functionality**
- Handle multiple discrete operations in a single tool call
- Example: Instead of separate `list_users`, `list_events`, and `create_event` tools, create a single `schedule_event` tool

**Match Agent Capabilities**
- Agents have limited context but can reason and search
- Example: Use `search_contacts` instead of `list_contacts` (which forces agents to read through all contacts)

### Namespace Your Tools

**Clear Boundaries**
- Use prefixes to group related tools (e.g., `asana_search`, `jira_search`)
- Namespace by service and resource (e.g., `asana_projects_search`, `asana_users_search`)
- Choose naming schemes based on your own evaluations

**Reduce Confusion**
- Help agents select the right tools at the right time
- Minimize overlapping or vague tool purposes
- Enable natural task subdivision similar to human workflows

### Return Meaningful Context

**High Signal Information**
- Prioritize contextual relevance over technical flexibility
- Avoid low-level identifiers (UUIDs, technical IDs)
- Use semantic, interpretable names and identifiers

**Flexible Response Formats**
- Implement `response_format` parameter with options like "concise" or "detailed"
- Allow agents to control verbosity based on their needs
- Example: Concise responses use ~⅓ the tokens of detailed responses

**Natural Language Focus**
- Use human-readable names instead of cryptic identifiers
- Resolve UUIDs to meaningful language when possible
- Reduce hallucinations through clearer identifiers

### Optimize for Token Efficiency

**Context Management**
- Implement pagination, filtering, and truncation with sensible defaults
- Restrict tool responses (e.g., 25,000 tokens maximum)
- Encourage targeted searches over broad searches

**Helpful Error Messages**
- Provide specific, actionable error responses
- Avoid opaque error codes or tracebacks
- Guide agents toward more effective strategies

### Prompt-Engineer Tool Descriptions

**Clear Communication**
- Write descriptions as if explaining to a new team member
- Make implicit context explicit (query formats, terminology, relationships)
- Avoid ambiguity in expected inputs and outputs

**Unambiguous Parameters**
- Use specific parameter names (e.g., `user_id` instead of `user`)
- Provide clear examples and expected formats
- Define relationships between parameters

**Dramatic Impact**
- Small refinements to tool descriptions can yield significant improvements
- Tool descriptions are loaded into agent context and steer behavior
- Consider how tools are dynamically loaded into system prompts

## Key Insights

### Tools as Agent Partners
- Tools should enable agents to subdivide tasks like humans would
- Reduce context consumption through efficient tool design
- Offload computation from agent context into tool implementations

### Context is Limited and Precious
- Unlike traditional software with abundant memory, agents have context limits
- Design tools to minimize irrelevant information in responses
- Enable agents to find relevant information efficiently

### Evaluation-Driven Development
- Systematic evaluation reveals consistent patterns in tool effectiveness
- Effective tools are intentionally defined, use context judiciously, and combine well in workflows
- Continuous iteration and measurement drive improvement

## Looking Forward

As agents become more capable, tools must evolve alongside them. The principles outlined here—intentional design, judicious context use, composability, and intuitive problem-solving—will remain fundamental as the specific mechanisms of agent-world interaction continue to develop.

The transition from deterministic to non-deterministic software patterns requires this systematic, evaluation-driven approach to ensure tools remain effective as both agents and underlying technologies advance.
