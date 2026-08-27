# Mastering Advanced Reasoning Techniques

## Chain of Thought Prompting

Chain of Thought breaks down the problem into steps and encourages step by step thinking, and provides few short examples.

With reasoning, we prioritized explaining the reasoning first, followed by the answer. Our goal is to train the large language model to follow this pattern, think through problems, break down into fundamental steps, and provide answers. This approach has shown to yield better reasoning outputs from the AI model.

## ReAct Prompting

[ReAct Prompting – Nextra](https://www.promptingguide.ai/techniques/react)

The goal is to train the large language model to think through a process, comprehend necessary steps, and utilize external tools to perform actions. The model can then incorporate the results of these actions as computations.

## Peer Review (AI as Judge?)

We can use LLMs to evaluate prompts and their outputs without relying on human intervention.

The large language model itself can assess the output, enabling us to develop automated processes or escalate to humans as needed.

Example:

> Input: "Vanderbilt University (informally Vandy or VU) is a private research university in Nashville, Tennessee. Founded in 1873, it was named in honor of shipping and rail magnate Cornelius Vanderbilt, who provided the school its initial $1-million endowment in the hopes that his gift and the greater work of the university would help to heal the sectional wounds inflicted by the Civil War.[1]"
Output: 1873
Explanation: The output is missing important information about the event that happened on the given date.
Grade: 3/10
> 

Give the model several examples (few-shots) of different gradings.