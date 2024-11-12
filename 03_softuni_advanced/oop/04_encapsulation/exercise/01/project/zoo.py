from collections import defaultdict
from project.animal import Animal
from project.cheetah import Cheetah
from project.lion import Lion
from project.tiger import Tiger
from project.worker import Worker


class Zoo:

    def __init__(
        self, name: str, budget: int, animal_capacity: int, workers_capacity: int
    ):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list[Animal] = []
        self.workers: list[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal._name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker._name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        worker = next((w for w in self.workers if w._name == worker_name), None)
        if worker:
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        total_salary = sum(worker.salary for worker in self.workers)
        if self.__budget >= total_salary:
            self.__budget -= total_salary
            return (
                f"You payed your workers. They are happy. Budget left: {self.__budget}"
            )
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        total_care_cost = sum(animal.money_for_care for animal in self.animals)
        if self.__budget >= total_care_cost:
            self.__budget -= total_care_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        lions = [animal for animal in self.animals if isinstance(animal, Lion)]
        tigers = [animal for animal in self.animals if isinstance(animal, Tiger)]
        cheetahs = [animal for animal in self.animals if isinstance(animal, Cheetah)]

        result = f"You have {len(self.animals)} animals\n"
        result += f"----- {len(lions)} Lions:\n" + "\n".join(map(repr, lions)) + "\n"
        result += f"----- {len(tigers)} Tigers:\n" + "\n".join(map(repr, tigers)) + "\n"
        result += f"----- {len(cheetahs)} Cheetahs:\n" + "\n".join(map(repr, cheetahs))

        return result

    def workers_status(self) -> str:
        keepers = [
            worker for worker in self.workers if worker.__class__.__name__ == "Keeper"
        ]
        caretakers = [
            worker
            for worker in self.workers
            if worker.__class__.__name__ == "Caretaker"
        ]
        vets = [worker for worker in self.workers if worker.__class__.__name__ == "Vet"]

        result = f"You have {len(self.workers)} workers\n"
        result += (
            f"----- {len(keepers)} Keepers:\n" + "\n".join(map(repr, keepers)) + "\n"
        )
        result += (
            f"----- {len(caretakers)} Caretakers:\n"
            + "\n".join(map(repr, caretakers))
            + "\n"
        )
        result += f"----- {len(vets)} Vets:\n" + "\n".join(map(repr, vets))

        return result
