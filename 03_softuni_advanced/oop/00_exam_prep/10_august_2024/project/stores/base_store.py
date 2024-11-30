from abc import ABC, abstractmethod

from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse


class BaseStore(ABC):
    def __init__(self, name: str, location: str, capacity: int, products):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products: list[Chair | HobbyHorse] = products

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or value.isspace():
            raise ValueError("Store name cannot be empty!")
        self._name = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if len(value) != 3 or value.isspace() or " " in value:
            raise ValueError("Store location must be 3 chars long!")
        self._location = value

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError()
        self._capacity = value

    def get_estimated_profit(self):
        all_products = 0
        for product in self.products:
            all_products += product.price
        estimated_profit = all_products * 0.10
        return f"Estimated future profit for {len(self.products)} products is {estimated_profit:.2f}"

    @abstractmethod
    @property
    def store_type(self):
        pass

    @abstractmethod
    @property
    def store_stats(self):
        pass
