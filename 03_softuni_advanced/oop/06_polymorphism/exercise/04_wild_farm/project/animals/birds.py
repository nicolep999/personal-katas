from abc import ABC
from project.animals.animal import Animal
from project.food import Meat, Vegetable, Fruit, Seed


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float) -> None:
        super().__init__(name, weight)
        self.wing_size: float = wing_size

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Owl(Bird):

    def __init__(self, name: str, weight: float, wing_size) -> None:
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += 0.25 * food.quantity


class Hen(Bird):

    def __init__(self, name: str, weight: float, wing_size) -> None:
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        if not isinstance(food, (Meat, Vegetable, Fruit, Seed)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += 0.35 * food.quantity
