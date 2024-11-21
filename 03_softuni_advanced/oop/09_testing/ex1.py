from unittest import TestCase, expectedFailure


def sum_nums(a, b):
    return a + b


class SumTest(TestCase):

    def test_sum_returns_result(self):
        expected_result = 11
        actual_result = sum_nums(5, 6)
        self.assertEqual(expected_result, actual_result)
