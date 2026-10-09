# Prototype 001 — Distinction Records

This is the smallest executable probe for the current representation hypothesis.

## Run

Requires Python 3.10+.

```bash
python -m unittest -v
```

## What it tests

- A pair can be equivalent under one criterion and distinct under another.
- The criterion is explicit, not silently selected by the comparison function.
- Missing information yields `unknown`, not a guessed equivalence.
- Each result retains a short evidence string.

## What it does not test

This does not demonstrate intelligence, grounded understanding, or superiority to an LLM. It is a unit test of the schema's basic semantics. The next step is to compare representation strategies on held-out relational tasks.
