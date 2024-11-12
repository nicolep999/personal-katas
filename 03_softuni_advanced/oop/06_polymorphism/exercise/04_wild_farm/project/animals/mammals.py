from project.animals.animal import Animal, Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):

    def __init__(self, name, weight, living_region: str) -> None:
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if not isinstance(food, (Vegetable, Fruit)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += 0.10 * food.quantity


class Dog(Mammal):

    def __init__(self, name, weight, living_region: str) -> None:
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += 0.40 * food.quantity


class Cat(Mammal):
    def __init__(self, name, weight, living_region: str) -> None:
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if not isinstance(food, (Meat, Vegetable)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += 0.30 * food.quantity


class Tiger(Mammal):
    def __init__(self, name, weight, living_region: str) -> None:
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += 1 * food.quantity
