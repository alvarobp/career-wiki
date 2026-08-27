# Testing Microservices, the sane way

Created By: Álvaro Bautista Pino
Last Edited: June 26, 2020 8:01 AM
Tags: microservices, testing
Link: https://medium.com/@copyconstruct/testing-microservices-the-sane-way-9bb31d158c16

- Full Stack in a Box (have the whole stack in local laptops), is quite tricky and hard to maintain.
    - "trying to replicate a cloud environment locally doesn’t offer benefits commensurate with the effort required to get it off the ground and subsequently maintain it"
- Post-Production testing: "Pushing regression testing to post-production monitoring requires not just a change in mindset and a certain appetite for risk, but more importantly an overhaul in system design along with a solid investment in good release engineering practices and tooling. In other words, it involves not just architecting for failure, but in essence, coding for failure when the heretofore default was coding for success."
- What to test pre and post production:
    - Both forms of testing to be primary considerations at the time of **system design**. Some functionalities may require verification pre-production. However, **some functionalities, given their own characteristics (idiosyncrasies), are better to be explored in production with the help of comprehensive instrumentation and tooling.**
    - A “top-down” approach to testing or monitoring by treating it as an afterthought has proven to be hopelessly ineffective so far.
- Exploratory testing, may make more sense to be carried on in post-production with the "real thing", except for critical features/systems (safety critical systems, financial systems...)
- Embrace failure (mid-large distributed systems will fail 100% of the time), code accordingly:
    - understanding the operational semantics of the application (from how app is deployed to many details of the app running in production)
    - understanding the operational characteristics of the dependencies
    - writing code that’s debuggable (being able to ask questions in the future)
        - **Observability format**: metrics or logs or exception trackers or traces or a combination of these
- Pre-production testing
    - Four axes — **the goal, scope, tradeoffs and payoffs** — can prove to be a good proxy for being able to assess how effective any form of testing might be
        - Goal: best effort verification of the correctness of a system as well as a best effort simulation of the known failure modes
        - The scope of pre-production testing is only as good as our ability to conceive good heuristics that might prove to be a precursor of production bugs