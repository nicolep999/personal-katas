from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity: float, fuel_consumption: float) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float) -> None:
        pass

    @abstractmethod
    def refuel(self, fuel: float) -> None:
        pass


class Car(Vehicle):

    AC_FUEL_CONSUMPTION = 0.9

    def drive(self, distance: float) -> None:
        required_fuel = (self.fuel_consumption + self.AC_FUEL_CONSUMPTION) * distance
        if required_fuel <= self.fuel_quantity:
            self.fuel_quantity -= required_fuel

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):

    AC_FUEL_CONSUMPTION = 1.6
    HOLE_IN_TANK = 0.95

    def drive(self, distance: float) -> None:
        required_fuel = (self.fuel_consumption + self.AC_FUEL_CONSUMPTION) * distance
        if required_fuel <= self.fuel_quantity:
            self.fuel_quantity -= required_fuel

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel * self.HOLE_IN_TANK
