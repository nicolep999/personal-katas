from unittest import TestCase, main


class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_info(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old"


class TestPerson(TestCase):

    def setUp(self):
        # Arrange
        self.person = Person("John", "Smith", 18)

    def test_unit(self):
        # Assert
        self.assertEqual(self.person.first_name, "John")
        self.assertEqual(self.person.last_name, "Smith")
        self.assertEqual(self.person.age, 18)

    def test_get_full_name(self):
        # Act
        result = self.person.get_full_name()
        expected_result = "John Smith"
        # Assert
        self.assertEqual(expected_result, result)

    def test_get_info(self):
        # Act
        result = self.person.get_info()
        expected_result = "John Smith is 18 years old"
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
