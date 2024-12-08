from unittest import TestCase, main
from project.mammal import Mammal


class MammalTest(TestCase):
    def setUp(self):
        self.m = Mammal("Test", "test_type", "meow")

    def test_init(self):
        self.assertEqual(self.m.name, "Test")
        self.assertEqual(self.m.type, "test_type")
        self.assertEqual(self.m.sound, "meow")
        self.assertEqual(self.m.get_kingdom(), "animals")

    def test_if_make_sound(self):
        result = self.m.make_sound()
        expected = "Test makes meow"
        self.assertEqual(expected, result)

    def test_get_kingdom(self):
        result = self.m.get_kingdom()
        self.assertEqual(result, "animals")

    def test_info(self):
        result = self.m.info()
        expected_result = "Test is of type test_type"
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
