# Behavioral Composition / Test Composition (Kent Beck)

Created By: Álvaro Bautista Pino
Last Edited: April 18, 2024 10:31 PM

[TDD's Missing Skill: Behavioral Composition](https://tidyfirst.substack.com/p/tdds-missing-skill-behavioral-composition)

**TDD's Missing Skill: Behavioral Composition**

![Untitled](Behavioral%20Composition%20Test%20Composition%20(Kent%20Beck/Untitled.png)

I appreciate Mr. Zakharchenko’s extensive critique of TDD even as I have some reservations regarding his language. He tried TDD. He thought about it. He put his thoughts out there. He knew he was going to get a reaction & he did—300K views, 160 comments, 190 reposts, 1000 likes.

He describes his programming workflow, which he describes as Prototype→Iterate→Test. It doesn’t sound like a horrible workflow to me, aside from the inevitable temptation to skip testing. But his description of his workflow & his struggles with TDD make it sound to me like he is missing a skill, a skill that I & other folks who use TDD have taken for granted all these years.

Note that when I say he’s “missing a skill”, I don’t mean he’s a bad programmer. I’m missing loads of skills. Nobody, as Lee Trevino put it, has a full bag [of golf clubs]. There’s a thing that I do that, if he was able to do it, he wouldn’t talk about TDD the way he does. None of which is to imply that he *should* use TDD, or learn the skill I’m about to describe.

## Behavioral Composition

I’m going to call this skill Behavioral Composition. It comes in 3 parts:

- The ability to break a big complicated behavior into pieces,
- In such a way that implementing & verifying those pieces implies that the whole behavior acts as expected,
- And the confidence to work this process.

Thus, my experience of TDD is the opposite of his “you should know how the system behaves before even implementing it”. We all have *some* sense of how the system will behave when we’re “done” or we wouldn’t start. But using Behavioral Composition I explicitly don’t care how the whole system behaves in detail before I start. I gradually record my expectations piecemeal in the form of tests & satisfy those expectations piecemeal in the form of changes to the code.

## Toy Problem

The following isn’t intended to respond to his criticism, but to illustrate the skill I’m describing. I’ll close in a moment with some thoughts on using Behavioral Composition in “the real world”.

What are the behaviors of a Stack?

- IsEmpty where we get both answers.
- Pushing an item & popping it.
- Pushing 2 items & popping them in the right order.
- Popping from an empty stack.
- [optional] Overfilling a stack.

We could prototype this & iterate & come up with a reasonable solution. Or we could implement it one test case at a time & come to approximately the same solution. Coming up with the list above is what I mean by Behavioral Composition.

## Ordering

How do you know in which order to implement the items in the list of tests? You don’t, *a priori*. Practice gives you some sense of what to choose next. Sometimes, though, you hit a dead end where you can’t see how to implement the next test. Then you can either further decompose the behavior or back up a few steps & choose a different next increment of behavior.

## Discovery

What about behaviors you discover as implement? Add them to the list. One of the great joys of programming is how it shows you, in the starkest terms, when you don’t understand something.

## Conclusion

How does this play out in “the real world”? Sometimes it’s difficult or (for the moment) impossible to decompose behavior in a way that satisfies the conditions outlined above—recomposing the decomposed behavior results in overall behavior that satisfies our needs & we are confident in the process. Okay, in those cases TDD doesn’t apply.

When I’ve encountered such situations & coded ahead unsupported by tests, sometimes I’ve failed & sometimes I’ve succeeded, but I’ve always thought, “If I wanted to be supported by tests as I code, how could I have designed & coded this differently?” & I’ve often found a way I could have applied TDD if only I had known.

When using Behavioral Composition, tests in TDD support programming 2 ways:

- Tests restrict the scope of the problem you’re solving for the moment. This gets me unstuck when I’m overwhelmed. I don’t need to swallow the whole problem just yet, just this next mouthful.
- Tests tell you whether the changes to the code work as intended & if you’ve unintentionally changed code that was previously working as intended. I find this deeply reassuring as I continue to make changes.

I don’t want to program without this support.

One of the most impressive programs I’ve ever seen was a FORTRAN program that generated topographical maps with labels in the right places, both for place names and for contour lines. Now maybe there’s a trick to this that I just don’t know, but sitting here now I have no idea how I would behaviorally compose such a renderer. I’d probably fall back on Prototype→Iterate→Test or at least Prototype→Discard→TDD if I needed to implement it. I hope someone tries this problem with Behavioral Composition & tells me how it worked.

Again, I don’t mean to denigrate his skills overall, just to point out that there is a skill he seems to be missing, one we (the TDD community) hasn’t described or explored or taught. I’d love to see a list of Behavioral Composition “moves” that matches the actions of experts. And I’d love not to have to write it ‘cause I have other things to do.

## Coda: Test Composition

I suspect there’s an analogous skill of composing tests to get justified confidence in the overall behavior of a system without exhaustive testing. Again, this is a thing I do without specifically thinking about it & I don’t hear other TDDers talking about it, so there’s something else to explore here. I further suspect that this skill is only partly a test-writing skill, it’s more a software design skill that let’s you confidently test separate dimensions of variability separately. More later.