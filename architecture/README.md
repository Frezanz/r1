# Architecture Research

## Objective

Test whether an explicit relational representation can support useful intelligence operations beyond token prediction alone.

## Candidate layers

1. **Input adapters:** convert text, measurements, images, tool outputs, and other observations into candidate representations.
2. **Representation store:** maintain distinctions, entities, properties, relations, context, evidence, and uncertainty.
3. **World/state model:** represent states, events, temporal order, and candidate transitions.
4. **Inference engine:** apply explicit rules, learned scoring, search, simulation, or combinations of these.
5. **Learning and revision:** update representations when new evidence conflicts with current beliefs; preserve provenance and version history.
6. **Language interface:** map natural-language expressions to internal structures and render answers from those structures.
7. **Evaluation loop:** compare predictions with outcomes, detect errors, and test whether revisions improve performance.

This is a research decomposition, not a committed implementation. Some layers may collapse, be learned jointly, or be unnecessary.

## Architecture principles

- Do not assume every internal representation must be symbolic.
- Do not assume neural networks must be excluded.
- Separate a model's confidence from the truth of its claim.
- Track where information came from and what evidence would change a conclusion.
- Make the representation support operations; a graph that merely stores facts is not by itself an intelligence architecture.
- Compare compute, memory, latency, accuracy, robustness, and generalization with appropriate baselines.

## Minimum demonstrator

Build a small synthetic world with a few objects, attributes, relations, state changes, and ambiguous descriptions. Ask the system to identify relevant differences, answer relational questions, predict simple changes, and revise beliefs after contradictory evidence.

Compare entity-first, distinction-first, and a compact learned-vector baseline on the same data and tasks. Report failures as well as successes.
