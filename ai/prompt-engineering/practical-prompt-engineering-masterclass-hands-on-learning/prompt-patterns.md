# Prompt Patterns

### Persona Pattern

Used to seek guidance from the appropriate person or entity in the real world. Although we don't know how exactly they would respond, we aim to replicate the behavior and the output.

The persona pattern is designed to mimic this behavior, enabling us to seek guidance from the experts **without needing specific knowledge of their response, format or expertise**.

We don’t have to limit ourselves to actual personas, we can refer to objects. E.g: `Acts as the Linux terminal for a computer that has been hacked`

### Refinement Pattern

To improve interaction with large language models like ChatGPT, we can use the question refinement pattern.

The basic idea is that we observe the model's response when we ask a question, and try to improve our question based on its insights.

Tell the model to suggest a better question and ask if I want to use it instead. This improves the user experience by eliminating the need to manually copy or specify the generated question.

Example prompt: `Whenever I ask a question, suggest a better question and ask me if I would like to use it instead`. Then you make questions to the assistant.

### Cognitive Verifier Pattern

Ask the model to break down questions or problems into smaller ones that can help finding solutions. 

> Whenever you are asked a question, follow these rules. Generate an additional number of questions that would help more accurately answer the question. Combine the answers to the individual questions to produce the final answer to the overall question.
> 

### Audience Persona Pattern

Sometimes, instead of focusing on the large language models behavior, we want it to generate output for a specific persona.

By specifying the audience, the model can tailor the output accordingly, ensuring it is appropriate for the particular audience, rather than listing rules about what is and what isn't allowed in the output.

> Explain large language models and how they work to me. Assume that I have no background in computer science.
> 

> Explain large language models and how they work to me. Assume that I am Christopher Columbus
> 

### Flipped Interaction

Instead of asking questions and the language model providing answers, we flip the interaction. We let the language model ask us questions and we provide the answers.

> Ask me questions about fitness goals until you have enough information to suggest a strength training regime for me. When you have enough information show me the strength training regime.

Ask me the first question.
>