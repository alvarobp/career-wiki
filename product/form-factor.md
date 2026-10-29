# Form Factor

## Summary

**Form factor** is the physical or structural design of a product — its shape, configuration, and the way users meet it. In hardware the term is literal: size, component arrangement, laptop versus desktop, one motherboard standard versus another. In software and product management it describes the structural arrangement of features and the overall user experience within the constraints of a given interface — a terminal window, a mobile app, a web GUI.

The choice is not cosmetic. A form factor sets strict boundaries, and those boundaries drive the product decisions that follow: what is visible, what is buried, how a new user gets started, how far the thing can be bent to a user's own purposes.

## Origin: form, fit, and function

The term comes out of 1960s manufacturing and engineering, from the **form, fit, and function** (FFF) concept:

- **Form** — physical configuration and material properties
- **Fit** — the ability to interface with other components
- **Function** — the intended actions and operations

In software the "form" half drifted from physical configuration to design structure, logic flow, and the organisation of the user interface. The engineering sense survives underneath: a form factor is still the thing that determines what your product can be plugged into.

## What the choice constrains

Picking a form factor decides, in advance, a set of questions that look like separate product decisions:

- **Feature visibility** — which features are surfaced and which stay hidden
- **Depth and complexity** — how much of it the interface can hold before it collapses
- **Onboarding** — what a new user's first minutes look like
- **Customisation** — how far users can reshape it
- **Adoption patterns** — which features people actually find and use

Together these set the product's intuition, the user's workflow, and the constraints development works under.

## Worked example: Claude Code

Claude Code is a coding agent in a **minimalist, terminal-based** form factor, and the choice shapes everything downstream:

- **Usability** — keyboard-first interaction, bounded by what a terminal can render
- **Extensibility** — new features have to arrive as something that fits a command-line workflow
- **User experience** — direct, text-based exchange with none of the overhead of a GUI

The terminal constrains how a user can talk to the assistant. It also buys the thing that matters most: it sits inside the developer workflow that already exists, alongside the shell, the editor, and the repository.

Other form factors trade differently:

- **Mobile apps** — touch-optimised layouts, disciplined by screen size
- **Web dashboards** — desktop layouts with multiple panels and room for complex navigation

## Counterpoint: the end of the product

Javier Cañada's essay [El fin del producto](https://tramontana.ai/fin-producto) ("The End of the Product", Instituto Tramontana) questions this framing. Form factor treats the interface as the upstream decision that everything else follows from. Cañada says the interface was never the important part.

- **Digital design builds an intermediate layer**: a new interface between a person and an old function such as travel, shopping, or moving money.
- **What gave a company its edge was what sat behind that layer**: capital, operations, and a legal framework. The operations used to take millions of human hours and now start to take tens of machine hours, so "the monopoly of operations is broken."
- **A product is a standardised way of meeting a need.** AI agents can now build a solution for each person's own context, so the standardised product stops making sense.
- **What AI kills is not the interface but intermediation.** An earlier argument of his, that AI turns graphical interfaces into conversational ones, now reads to him as the surface of the change.

If he is right, picking a form factor still decides how users reach the product, but it says nothing about whether a standardised product should sit between them and the function at all. That question is further upstream. His test for it is the one he put to a worried CEO: "If you started from scratch today, what would you keep?"

## Core Insight

The form factor is chosen once and then answers a hundred later questions on your behalf. Debating a feature's visibility, its onboarding, or its extensibility in isolation is usually a debate about a decision already made upstream — so treat the form factor as a first-class product decision, not as the container the real decisions go in.
