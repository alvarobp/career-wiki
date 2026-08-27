# Lesson 5: Spec based AI Coding with Reasoning Models

- **Objective of the Lesson:**
    - Learn how to effectively generate large amounts of code using a single specification (spec) prompt.
    - Understand that the current bottleneck in coding is not the models but how effectively we can communicate with them.
- **Key Concepts Introduced:**
    - **Specification (Spec) Prompt:**
        - A spec is akin to a detailed plan that outlines what is required before coding begins.
        - Effective planning translates to effective prompting for AI models.
- **Importance of Planning:**
    - Senior engineers often utilize plans or architecture documentation to guide their work.
    - Strong prompts (or plans) enable reasoning models to perform at a higher level.
    - With great prompting, AI coding capabilities can drastically increase productivity.
- **Three Main Ideas:**
    1. **Reasoning Models:** Advanced reasoning models can process and iterate upon prompts, improving code accuracy and generation speed.
    2. **Spec Documents:** Writing comprehensive spec documents helps define tasks clearly and allows models to understand requirements fully.
    3. **Architect Mode:** The use of tools like Aider's architect mode enhances the accuracy of code generation by utilizing separate models for drafting and editing.
- **Challenges and Mental Shift:**
    - Transitioning to working with AI coding assistants involves a mindset shift from traditional coding.
    - Requires engineers to gather context, write out detailed steps, and trust models to execute tasks.
- **Learning by Doing:**
    - The lesson involved reconstructing a transcript analytics application using spec prompts and lower-level tasks.
    - Utilized Aider features such as creating models, implementation notes, and specific functions to structure the code effectively.
- **Execution and Review:**
    - After executing the prompts, tests were performed to verify the correctness of the generated code.
    - Discussions included troubleshooting issues that arise, such as naming conflicts and ensuring the accuracy of the generated output files (e.g., JSON, YAML).
- **Conclusion and Next Steps:**
    - Successful application of spec prompts can lead to significant productivity boosts in coding.
    - Emphasized the importance of creating reusable patterns and communicating effectively with AI coding assistants.
    - Encouraged practicing the techniques learned in the lesson before proceeding to future lessons which will build on this foundational knowledge.
- **Takeaway:**
    - Effective planning equates to effective code prompting. The lessons learned here are crucial to developing as an engineer capable of leveraging AI in coding.

- **Counter-position — write smaller specs, not bigger ones:**
    - Luca Rossi's [The Telephone Game of Software](../the-telephone-game-of-software.md) argues that the big-spec-up-front approach this lesson teaches over-focuses on the task at hand at the expense of improving the system over time.
    - Its specific objection is to putting stack, architecture, legacy systems, compliance and performance targets into the spec: you would not spell any of that out for an engineer on your team, because it belongs to the standing context of the work.
    - The alternative is **platform, not spec**: product docs, app principles, a design system, `ARCHITECTURE.md` and `ABSTRACTIONS.md`, and gates on the code itself — so the model infers what you would otherwise have to write down, and the spec shrinks to just the intent for this task.
    - It also questions the premise that you can write the full spec at all, since your understanding of the feature often improves only by prototyping and clicking on things. Its version of the spec is a living collaboration surface the model enriches with the decisions it made, which you then inspect.

This lesson lays the groundwork for future coding practices using AI that are expected to greatly enhance productivity and quality in software development. The next lesson promises to build on this knowledge by exploring how to eliminate entire classes of engineering work using AI alongside the principles covered in this lesson.