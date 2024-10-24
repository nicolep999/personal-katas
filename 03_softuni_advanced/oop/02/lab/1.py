class Vet:

    animals: list = []
    space: int = 5

    def __init__(self, name: str):
        self.name = name

    def register_animal(self, animal_name):
        if self.space:
            self.animals.append(animal_name)
