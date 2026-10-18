import unittest
from fundamental_characters import CharacterRegistry, build_python_character_registry, inspect_source


class FundamentalCharacterTests(unittest.TestCase):
    def test_registry_contains_python_source_characters(self):
        registry = build_python_character_registry()
        for char in ("a", "7", "=", "+", "(", ")", " "):
            self.assertIsNotNone(registry.get(char))

    def test_record_contains_unicode_identity_and_tags(self):
        record = CharacterRegistry().register_character("A", "letter", "identifier-part")
        self.assertEqual(record.codepoint, "U+0041")
        self.assertEqual(record.unicode_category, "Lu")
        self.assertEqual(record.tags, {"letter", "identifier-part"})

    def test_tags_accumulate(self):
        registry = CharacterRegistry()
        registry.register_character("+", "operator")
        registry.register_character("+", "seen-in-source")
        self.assertEqual(registry.get("+").tags, {"operator", "seen-in-source"})

    def test_requires_one_codepoint(self):
        with self.assertRaises(ValueError):
            CharacterRegistry().register_character("ab")

    def test_source_preserved_and_tokens_tagged(self):
        source = "total = price * quantity\n"
        result = inspect_source(source)
        self.assertEqual(result["source"], source)
        price = next(t for t in result["tokens"] if t.text == "price")
        self.assertIn("python:identifier", price.tags)
        operator = next(t for t in result["tokens"] if t.text == "*")
        self.assertIn("python:operator-or-delimiter", operator.tags)

    def test_keyword_and_number_tagged(self):
        result = inspect_source("if count == 3:\n    pass\n")
        keyword_token = next(t for t in result["tokens"] if t.text == "if")
        number_token = next(t for t in result["tokens"] if t.text == "3")
        self.assertIn("python:keyword", keyword_token.tags)
        self.assertIn("python:numeric-literal", number_token.tags)

    def test_compiles_without_executing(self):
        source = "raise RuntimeError('must not execute during inspection')\n"
        result = inspect_source(source)
        self.assertEqual(result["source"], source)
        self.assertIsNotNone(result["code_object"])

    def test_python_reports_invalid_syntax(self):
        with self.assertRaises(SyntaxError):
            inspect_source("if x print(x)\n")

    def test_unicode_character_supported(self):
        record = CharacterRegistry().register_character("é", "observed")
        self.assertEqual(record.codepoint, "U+00E9")
        self.assertIn("observed", record.tags)


if __name__ == "__main__":
    unittest.main()
