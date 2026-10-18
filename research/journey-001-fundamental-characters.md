# Journey 001 — Fundamental Characters

**Status:** First implementation committed; local Termux verification pending.

## Goal
Use the installed Python environment to seed a character/token vocabulary, inspect Python source with its own tokenizer, and attach additional metadata without replacing the existing Python machinery.

## Implementation
- Seed from printable source characters, keywords, soft keywords, exact operator/delimiter spellings, and token type names.
- Record each Unicode code point with its representation, code point, Unicode name/category, and accumulated tags.
- Use tokenize to identify token occurrences and tag their context.
- Use ast.parse and compile for parsing and compilation; inspected source is never executed.
- Preserve source text and keep the metadata registry separate.

## Initial tags
python:keyword, python:soft-keyword, python:identifier, python:numeric-literal, python:string-literal, python:operator-or-delimiter, and python:layout.

Tags describe a role observed in a context. A character can accumulate multiple tags in different contexts.

## Acceptance checks
- Character registration and Unicode identity.
- Accumulation of metadata tags.
- Token tagging using Python's tokenizer.
- Source preservation.
- Syntax validation and compilation without execution.
- Unit tests pass on the target Termux environment.

## Questions after testing
- Which Python token spellings or source characters need additional coverage?
- Which operations need character-level tags versus token-occurrence tags?
- What metadata format will best support later formula construction?
- What are the measured time and memory costs?

Record observed findings before introducing new structures.
