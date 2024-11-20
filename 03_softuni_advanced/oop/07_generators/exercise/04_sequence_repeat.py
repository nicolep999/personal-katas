class sequence_repeat:
    def __init__(self, sequence: str, length: int):
        self.sequence = list(sequence)
        self.length = length
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= self.length:
            raise StopIteration
        current_item = self.sequence[self.current_index % len(self.sequence)]
        self.current_index += 1
        return current_item


# test zero
import unittest


class Tests(unittest.TestCase):
    def test_zero(self):
        result = list(sequence_repeat("abc", 5))
        self.assertEqual(result, ["a", "b", "c", "a", "b"])


if __name__ == "__main__":
    unittest.main()
