# The Bitter Lesson

**Source:** http://www.incompleteideas.net/IncIdeas/BitterLesson.html
**Author:** Rich Sutton
**Date:** March 13, 2019

## Summary

"The Bitter Lesson" argues that 70 years of AI research consistently shows that general methods leveraging computation ultimately outperform approaches that encode human knowledge and domain expertise. Rich Sutton demonstrates this pattern across multiple fields:

- **Computer Chess**: Deep search with computation defeated world champions, not human chess expertise
- **Computer Go**: Self-play and learning at scale won, not hand-crafted game strategies
- **Speech Recognition**: Statistical methods (HMMs, then deep learning) outperformed linguistic knowledge
- **Computer Vision**: Deep learning with convolutions surpassed edge detection and hand-crafted features

The "bitter" aspect is that researchers repeatedly invest in building their understanding of domains into systems, which helps short-term but plateaus. Meanwhile, general methods that scale with computation (search and learning) eventually dominate.

## Practical Implications

1. **Favor scalable, general methods over domain-specific optimizations**
   - When building AI systems, prioritize approaches that can leverage more computation and data
   - Be cautious about over-engineering domain knowledge into your solutions

2. **Design for learning and search**
   - The two methods that scale arbitrarily are *search* and *learning*
   - Build meta-methods that discover patterns, rather than encoding the patterns directly

3. **Don't encode human reasoning processes**
   - Resist the temptation to make systems work the way we think they should work
   - Let agents discover solutions through computation rather than implementing our discoveries

4. **Long-term thinking**
   - Short-term gains from domain expertise are often technical debt
   - Computation becomes exponentially cheaper over time - design for that future

5. **For AI engineering**
   - Focus on data quality and quantity over feature engineering
   - Invest in infrastructure that enables scaling (more compute, more data, better training)
   - Be skeptical of complex, hand-crafted solutions when simple, scalable alternatives exist

## Key Quotes and Modern Implications

### 1. On the Core Lesson
> "The biggest lesson that can be read from 70 years of AI research is that general methods that leverage computation are ultimately the most effective, and by a large margin."

This quote directly challenges the modern tendency to build elaborate domain-specific architectures and prompt engineering techniques. In 2024-2025, we see this playing out with foundation models: modern LLMs succeed not through carefully engineered linguistic rules, but through massive scale and general transformer architectures. For product engineers, this suggests investing in infrastructure that enables more compute and data rather than intricate feature pipelines. The "large margin" part is crucial—it's not a minor difference, meaning time spent on clever optimizations often yields diminishing returns compared to simply scaling.

### 2. On Resource Allocation
> "Time spent on one is time not spent on the other. There are psychological commitments to investment in one approach or the other. And the human-knowledge approach tends to complicate methods in ways that make them less suited to taking advantage of general methods leveraging computation."

This speaks directly to modern engineering decisions. When building AI products, teams face constant pressure to add "smart" heuristics, rules, and domain logic. But each addition creates complexity that makes it harder to benefit from model improvements or increased compute. Consider RAG systems: over-engineered retrieval pipelines with hand-crafted ranking algorithms often perform worse than simple semantic search once models improve. The "psychological commitment" aspect is particularly relevant—engineers naturally want to apply their domain expertise, but this essay warns that such investments may become liabilities.

### 3. On Wasted Effort
> "As in the games, researchers always tried to make systems that worked the way the researchers thought their own minds worked—they tried to put that knowledge in their systems—but it proved ultimately counterproductive, and a colossal waste of researcher's time."

The phrase "colossal waste" is deliberately harsh but increasingly vindicated. Modern software engineering has countless examples: elaborate NLP pipelines replaced by transformers, feature-engineered ML models replaced by end-to-end deep learning, rules-based chatbots replaced by LLMs. For product teams, this suggests radical simplification: instead of building complex business logic to handle edge cases, consider whether a more capable model with better training data could learn those patterns. The waste isn't just the code written—it's the opportunity cost of not investing in scalable approaches.

### 4. On Human-Centric Reasoning
> "We have to learn the bitter lesson that building in how we think we think does not work in the long run."

This challenges a fundamental assumption in software design: that we should model systems after human reasoning. Modern AI agents that work best often operate nothing like humans—they process vast context windows, make probabilistic decisions, and learn from massive datasets in ways humans cannot. For product engineers building with AI, this means resisting the urge to force LLMs into traditional software patterns. Instead of complex state machines and rule engines to "guide" the AI, provide clear objectives and let models find their own solution paths. The systems that win won't be the ones that mimic human processes most faithfully.

### 5. The Four-Point Bitter Lesson
> "The bitter lesson is based on the historical observations that 1) AI researchers have often tried to build knowledge into their agents, 2) this always helps in the short term, and is personally satisfying to the researcher, but 3) in the long run it plateaus and even inhibits further progress, and 4) breakthrough progress eventually arrives by an opposing approach based on scaling computation by search and learning."

This four-point framework is a decision-making tool. When evaluating AI features, ask: "Are we building in knowledge that helps now but will plateau?" Modern examples include: prompt engineering techniques that work for current models but break with newer versions, retrieval heuristics optimized for current embedding models, or validation rules that constrain what future models might handle naturally. The "personally satisfying" part explains why teams keep making this mistake—it feels good to apply expertise, even when it's counterproductive. Product strategy should favor approaches that improve with model generations rather than requiring constant re-engineering.

### 6. The Two Scalable Methods
> "One thing that should be learned from the bitter lesson is the great power of general purpose methods, of methods that continue to scale with increased computation even as the available computation becomes very great. The two methods that seem to scale arbitrarily in this way are search and learning."

For modern AI engineering, "search" manifests as techniques like tree search, MCTS (Monte Carlo Tree Search), and even inference-time compute scaling. "Learning" means not just pre-training but fine-tuning, RLHF, and continuous learning from user interactions. Product teams should design systems where throwing more compute at search or learning produces better results indefinitely. This could mean: building evaluation pipelines that support model retraining, implementing AB testing infrastructure for model variations, or designing prompts/agents that can leverage extended reasoning time. Avoid architectures that hit a ceiling regardless of additional resources.

### 7. On Complexity of Reality
> "The actual contents of minds are tremendously, irredeemably complex; we should stop trying to find simple ways to think about the contents of minds, such as simple ways to think about space, objects, multiple agents, or symmetries."

This quote warns against reductionism in AI system design. Modern software engineers often want to decompose problems into "understandable" components—a planning module, a reasoning module, a knowledge retrieval module. But Sutton argues the world's complexity is irreducible, and attempts to simplify often fail. This is visible in multi-agent systems: hand-designed agent interactions and communication protocols often underperform compared to end-to-end trained systems. For product engineering, this suggests embracing rather than fighting complexity—provide models with rich, unprocessed data rather than carefully curated, "simplified" inputs. The model can handle complexity better than your preprocessing pipeline can.

### 8. On Discovery vs. Encoding
> "We want AI agents that can discover like we can, not which contain what we have discovered. Building in our discoveries only makes it harder to see how the discovering process can be done."

This is perhaps the most profound insight for 2024-2025 AI engineering. As we build agents with tools, retrieval systems, and workflows, there's constant tension: should we hard-code solutions to known problems, or let agents discover solutions? For example, when an agent struggles with a task, the knee-jerk response is to add specific instructions or tools. But this prevents discovering whether the agent could solve it differently given more context or reasoning time. Product teams should bias toward building meta-capabilities (better reasoning, more tools, richer context) rather than encoding specific solutions. Each hard-coded solution is a constraint on future discovery.

### 9. On Meta-Methods
> "We should build in only the meta-methods that can find and capture this arbitrary complexity. Essential to these methods is that they can find good approximations, but the search for them should be by our methods, not by us."

This defines the boundary of where human engineering should focus: not on solutions, but on solution-finding methods. In modern terms, this means: building excellent evaluation frameworks rather than manually improving outputs; creating robust feedback loops rather than curating training data; designing agent architectures that can learn from failures rather than preventing failures through rules. The phrase "search for them should be by our methods, not by us" is a call for automation and learned optimization. Product engineers should ask: "Am I solving this problem, or am I building a system that can solve this class of problems?"

### 10. On Long-Term vs. Short-Term Thinking
> "Seeking an improvement that makes a difference in the shorter term, researchers seek to leverage their human knowledge of the domain, but the only thing that matters in the long run is the leveraging of computation."

This quote captures the core product strategy dilemma. Business pressure demands short-term wins, which naturally leads to domain-specific optimizations and clever heuristics. But "the only thing that matters in the long run" is unambiguous: these short-term gains are temporary. For engineering leaders, this suggests a portfolio approach: use domain knowledge for immediate needs, but simultaneously invest in scalable foundations. When newer model generations arrive, which parts of your system will improve automatically, and which will require complete rewrites? The ratio between these determines your technical leverage over time. Products architected for computation scaling will compound advantages; those built on clever tricks will require constant maintenance.
