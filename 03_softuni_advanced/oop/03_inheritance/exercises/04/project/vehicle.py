class Vehicle:

    DEFAULT_FUEL_CONSUMPTION: float = 1.25

    def __init__(self, fuel, horse_power) -> None:
        self.fuel_consumption: float = self.DEFAULT_FUEL_CONSUMPTION
        self.fuel: float = fuel
        self.horse_power: int = horse_power

    def drive(self, kilometers):
        required_fuel = kilometers * self.fuel_consumption
        if required_fuel <= self.fuel:
            self.fuel -= required_fuel
