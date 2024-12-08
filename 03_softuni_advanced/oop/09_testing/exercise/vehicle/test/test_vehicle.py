from unittest import TestCase, main
from project.vehicle import Vehicle


class VehicleTest(TestCase):

    def test_init(self):
        v = Vehicle(100, 200)
        self.assertEqual(100, v.fuel)
        self.assertEqual(200, v.horse_power)
        self.assertEqual(100, v.capacity)
        self.assertEqual(1.25, v.fuel_consumption)

    def test_drive(self):
        v = Vehicle(100, 200)
        fuel_expected = v.fuel - (v.fuel_consumption * 10)
        v.drive(10)
        self.assertEqual(fuel_expected, v.fuel)

    def test_drive_exception(self):
        v = Vehicle(100, 200)
        with self.assertRaises(Exception) as ex:
            v.drive(1000)
        self.assertEqual(str(ex.exception), "Not enough fuel")

    def test_refuel(self):
        v = Vehicle(100, 200)
        v.drive(10)
        expected_fuel = v.fuel + 1
        v.refuel(1)
        self.assertEqual(expected_fuel, v.fuel)

    def test_refuel_exception(self):
        v = Vehicle(100, 200)
        with self.assertRaises(Exception) as ex:
            v.refuel(100)
        self.assertEqual(str(ex.exception), "Too much fuel")

    def test_str(self):
        v = Vehicle(100, 200)
        self.assertEqual(
            "The vehicle has 200 horse power with 100 fuel left and 1.25 fuel consumption",
            str(v),
        )


if __name__ == "__main__":
    main()
