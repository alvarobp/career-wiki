# Agentic Engineer - Principled AI Coding

[Agentic Engineer - Build LIVING software](https://agenticengineer.com/principled-ai-coding)

## Concepts

- Big Three Bullseye: Context - Model - Prompt. Means the right intersection of the three to get the results we want / expect.
- IDKs: Information-Dense Words (via Agentic Engineer course)
- Balance then Boost: Make sure context and prompt are aligned.

## Prompting

### **Low Level Prompts**

- Use IDKs for more accurate and effective prompts
    
    > The most common Information Dense Keywords (IDKs) are: create/update/delete, add/remove/move/replace/save/mirror, and var/function/class/type/file/default. These keywords are distinct, clear, and have direct meaning.
    > 
- Use punctuaction as its meant to. comma for a list, dots for separating orders, etc.
- Repeatable patterns
    - Location → Action → Detail:
        
        ```
        CREATE chart.py: 
        	CREATE def word_count_bar_chart(threshold_word_count: dict): show horizontal barchart, sort descending. 
        UPDATE main.py: 
        	REPLACE word count print with word_count_bar_chart. 
        	MOVE threshold logic AFTER for word loop.
        ```
        
        `CREATE [chart.py](http://chart.py)` is location. `CREATE def word_count_bar_chart` is action and the rest of the line are the details of that action.
        
- Argument keywords. By naming arguments to functions, or properties in types, etc adequately we hint the model in the right direction. No need to overexplain.

## Common Pitfalls

- Context
    - Missing context
        - The AI coding assistant will miss places that need to change. Can be compensated with prompts, like referring to files.
    - Too much context
- Prompt
    - Too high-level
        - Model responses are unpredictable, entropy is too high. We should strive for more mid-level prompts, letting the model know what we expect and as much as possible how.
        - When a high-level prompt does not work, rollback and try with lower-level prompts. (Similarly to TDD, go back to green and proceed in smaller steps)
    - Too low-level
        - Sometimes we don’t need to go too low-level, with some mid-level well-crafted prompt we can save time. For example, if our context is small enough for the model to know the Location (some function definition) we may just refer to the function name without specifying where it is. This balances Context and Prompt.
- Model
    - Using a weak model
        - It is not worth it to go with cheaper models just to save money. They willl force us to use more lower-level prompts and to correct mistakes we’d avoid with more powerful models. That would cost us time, at the very least.
    - Overkill model
        - Don’t use models too powerful for tasks a more general-purpose model can do well. For example (as of March 2025), do not use a reasoning model (e.g o3) for regular coding tasks.

**Summary:** It’s all about **balance**.

Always **think of the context from the the AI coding assistant perspective**. With this context and this prompt “would I be able to solve the problem?”.

### Practical Solutions

**Configure coding assistant tool**

Like tweaking Aider settings in .aider.conf.yml.

**Balance then Boost**

Start with low-level prompts (IDKs and phrases) to write high quality prompts. As you progress play with mid-level and high-level prompts to save time. Whenever getting issues with high-level prompt get back to low-level prompts. **Focus on getting things done**, not merely saving keystrokes.

## **Summaries**

[**Lesson 1: Hello AI Coding World: Install, Configure, Prompt**](lesson-1-hello-ai-coding-world-install-configure-prompt.md)

[Lesson 2: Multi-File Editing: STOP coding, START prompting](lesson-2-multi-file-editing-stop-coding-start-prompting.md)

[**Lesson 3: Know your IDKs: Crafting the PERFECT Prompt**](lesson-3-know-your-idks-crafting-the-perfect-prompt.md)

[Lesson 4: How to Suck at AI Coding: Common Pitfalls and Practical Solutions](lesson-4-how-to-suck-at-ai-coding-common-pitfalls-and.md)

[**Lesson 5: Spec based AI Coding with Reasoning Models**](lesson-5-spec-based-ai-coding-with-reasoning-models.md)