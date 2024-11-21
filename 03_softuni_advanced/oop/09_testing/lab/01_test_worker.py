from unittest import TestCase, main


class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception("Not enough energy.")

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f"{self.name} has saved {self.money} money."


class WorkerTest(TestCase):

    def test_init(self):
        w = Worker("Test", 1000, 100)
        self.assertEqual(w.name, "Test")
        self.assertEqual(w.salary, 1000)
        self.assertEqual(w.energy, 100)
        self.assertEqual(w.money, 0)

    def test_worker_works_no_energy_raises(self):
        w = Worker("Test", 1000, 0)

        self.assertEqual(w.money, 0)
        self.assertEqual(w.energy, 0)

        with self.assertRaises(Exception) as ex:
            w.work()

        self.assertEqual(str(ex.exception), "Not enough energy.")

    def test_worker_works(self):
        w = Worker("Test", 1000, 100)
        self.assertEqual(w.money, 0)
        self.assertEqual(w.energy, 100)

        result = w.work()

        self.assertEqual(w.money, 1000)
        self.assertEqual(w.energy, 99)

        self.assertIsNone(result)

    def test_worker_rest(self):
        w = Worker("Test", 1000, 100)
        self.assertEqual(w.energy, 100)
        result = w.rest()
        self.assertEqual(w.energy, 101)
        self.assertIsNone(result)

    def test_info(self):
        w = Worker("Test", 1000, 100)
        result = w.get_info()
        expected_result = "Test has saved 0 money."

        self.assertEqual(result, expected_result)
        w.work()
        result = w.get_info()
        expected_result = "Test has saved 1000 money."
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    main()
