from project.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):

    DEFAULT_FUEL_CONSUMPTION: float = 8

    def __init__(self, fuel, horse_power) -> None:
        super().__init__(fuel, horse_power)
