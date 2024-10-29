from project.car import Car


class SportCar(Car):

    DEFAULT_FUEL_CONSUMPTION: float = 10

    def __init__(self, fuel, horse_power) -> None:
        super().__init__(fuel, horse_power)
