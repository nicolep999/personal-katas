from project.vehicle import Vehicle


class Car(Vehicle):

    DEFAULT_FUEL_CONSUMPTION: float = 3

    def __init__(self, fuel, horse_power) -> None:
        super().__init__(fuel, horse_power)
