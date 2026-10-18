"""Python character/token metadata experiment for Journey 001."""
from __future__ import annotations
import ast
import io
import keyword
import string
import token
import tokenize
import unicodedata
from dataclasses import dataclass, field


@dataclass
class CharacterRecord:
    character: str
    codepoint: str
    unicode_name: str
    unicode_category: str
    tags: set[str] = field(default_factory=set)


@dataclass(frozen=True)
class TokenRecord:
    token_type: str
    text: str
    start: tuple[int, int]
    end: tuple[int, int]
    tags: tuple[str, ...]


class CharacterRegistry:
    def __init__(self):
        self._records: dict[str, CharacterRecord] = {}

    def register_character(self, character: str, *tags: str) -> CharacterRecord:
        if len(character) != 1:
            raise ValueError("Expected exactly one Unicode code point")
        record = self._records.get(character)
        if record is None:
            record = CharacterRecord(
                character, f"U+{ord(character):04X}",
                unicodedata.name(character, "<unnamed>"),
                unicodedata.category(character),
            )
            self._records[character] = record
        record.tags.update(tag for tag in tags if tag)
        return record

    def register_text(self, text: str, *tags: str) -> None:
        for character in text:
            self.register_character(character, *tags)

    def get(self, character: str) -> CharacterRecord | None:
        if len(character) != 1:
            raise ValueError("Expected exactly one Unicode code point")
        return self._records.get(character)

    def all_records(self) -> list[CharacterRecord]:
        return sorted(self._records.values(), key=lambda record: ord(record.character))

    def __len__(self) -> int:
        return len(self._records)


def build_python_character_registry() -> CharacterRegistry:
    registry = CharacterRegistry()
    registry.register_text(string.printable, "python:source-character")
    for word in keyword.kwlist:
        registry.register_text(word, "python:keyword-spelling")
    for word in getattr(keyword, "softkwlist", []):
        registry.register_text(word, "python:soft-keyword-spelling")
    for spelling in token.EXACT_TOKEN_TYPES:
        registry.register_text(spelling, "python:operator-or-delimiter")
    for name in token.tok_name.values():
        registry.register_text(name, "python:token-type-name")
    return registry


def _token_tags(tok: tokenize.TokenInfo) -> tuple[str, ...]:
    name = token.tok_name.get(tok.type, f"TOKEN_{tok.type}")
    tags = [f"python-token:{name}"]
    if tok.type == token.NAME:
        if keyword.iskeyword(tok.string):
            tags.append("python:keyword")
        elif tok.string in getattr(keyword, "softkwlist", []):
            tags.append("python:soft-keyword")
        else:
            tags.append("python:identifier")
    elif tok.type == token.NUMBER:
        tags.append("python:numeric-literal")
    elif tok.type == token.STRING:
        tags.append("python:string-literal")
    elif tok.type == token.OP:
        tags.append("python:operator-or-delimiter")
    elif tok.type in (token.NEWLINE, tokenize.NL, token.INDENT, token.DEDENT):
        tags.append("python:layout")
    return tuple(tags)


def inspect_source(source: str, registry: CharacterRegistry | None = None,
                   filename: str = "<source>") -> dict[str, object]:
    """Tag source with Python's tokenizer, parse and compile it, but never run it."""
    if registry is None:
        registry = build_python_character_registry()
    tokens = []
    for tok in tokenize.generate_tokens(io.StringIO(source).readline):
        tags = _token_tags(tok)
        tokens.append(TokenRecord(
            token.tok_name.get(tok.type, f"TOKEN_{tok.type}"),
            tok.string, tok.start, tok.end, tags,
        ))
        for character in tok.string:
            registry.register_character(character, *tags)
    tree = ast.parse(source, filename=filename)
    code_object = compile(source, filename, "exec")
    return {
        "source": source, "tokens": tokens, "ast": tree,
        "code_object": code_object, "character_count": len(registry),
    }
