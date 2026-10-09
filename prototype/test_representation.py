import unittest

from representation import DistinctionResult, compare


class DistinctionTests(unittest.TestCase):
    def setUp(self):
        self.apple = {"color": "red", "shape": "round"}
        self.ball = {"color": "red", "shape": "round"}
        self.sign = {"color": "red", "shape": "square"}
        self.unknown = {"color": "red"}

    def test_same_pair_can_be_equivalent_under_one_criterion_and_distinct_under_another(self):
        self.assertEqual(
            compare("apple", "sign", "color", self.apple, self.sign).result,
            DistinctionResult.EQUIVALENT,
        )
        self.assertEqual(
            compare("apple", "sign", "shape", self.apple, self.sign).result,
            DistinctionResult.DISTINCT,
        )

    def test_equal_values_are_equivalent_under_selected_criterion(self):
        record = compare("apple", "ball", "shape", self.apple, self.ball)
        self.assertEqual(record.result, DistinctionResult.EQUIVALENT)
        self.assertIn("shape", record.evidence)

    def test_missing_value_is_unknown_not_equivalent(self):
        record = compare("apple", "unknown", "shape", self.apple, self.unknown)
        self.assertEqual(record.result, DistinctionResult.UNKNOWN)

    def test_criterion_is_explicit_in_the_record(self):
        record = compare("apple", "sign", "shape", self.apple, self.sign)
        self.assertEqual(record.criterion, "shape")
        self.assertEqual(record.left_id, "apple")
        self.assertEqual(record.right_id, "sign")


if __name__ == "__main__":
    unittest.main()
