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

## Core Insight

The form factor is chosen once and then answers a hundred later questions on your behalf. Debating a feature's visibility, its onboarding, or its extensibility in isolation is usually a debate about a decision already made upstream — so treat the form factor as a first-class product decision, not as the container the real decisions go in.
