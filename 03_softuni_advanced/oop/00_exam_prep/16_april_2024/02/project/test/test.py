import unittest
from project.restaurant import Restaurant


class TestRestaurant(unittest.TestCase):
    def test_init(self):
        restaurant = Restaurant("Test", 10)
        self.assertEqual(restaurant.name, "Test")
        self.assertEqual(restaurant.capacity, 10)
        self.assertEqual(restaurant.waiters, [])

    def test_invalid_name(self):
        with self.assertRaises(ValueError) as ex:
            Restaurant("", 10)
        self.assertEqual(str(ex.exception), "Invalid name!")

    def test_invalid_capacity(self):
        with self.assertRaises(ValueError) as ex:
            Restaurant("Test", -1)
        self.assertEqual(str(ex.exception), "Invalid capacity!")

    def test_get_waiters(self):
        pass
        restaurant = Restaurant("Test", 10)
        restaurant.add_waiter("John")
        restaurant.add_waiter("Jane")
        expected_result = [{"name": "John"}, {"name": "Jane"}]
        self.assertEqual(expected_result, restaurant.get_waiters())

    def test_add_waiter(self):
        restaurant = Restaurant("Test", 2)
        result = restaurant.add_waiter("John")
        expected_result = "The waiter John has been added."
        self.assertEqual(result, expected_result)

    def test_remove_waiter(self):
        pass


if __name__ == "__main__":
    unittest.main()
