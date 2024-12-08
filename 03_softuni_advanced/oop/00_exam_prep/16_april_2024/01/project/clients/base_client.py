from abc import ABC, abstractmethod


class BaseClient(ABC):

    def __init__(self, name: str, membership_type: str) -> None:
        self.name = name
        self.membership_type = membership_type
        self.points: int = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or value.isspace():
            raise ValueError("Client name should be determined!")
        self.__name = value

    @property
    def membership_type(self):
        return self.__membership_type

    @membership_type.setter
    def membership_type(self, value):
        valid_memberships = ["Regular", "VIP"]
        if value not in valid_memberships:
            raise ValueError("Invalid membership type. Allowed types: Regular, VIP.")
        self.__membership_type = value

    @abstractmethod
    def earning_points(self, order_amount: float) -> None:
        pass

    def apply_discount(self):
        if self.points >= 100:
            self.points -= 100
            discount = 10
        elif self.points >= 50:
            self.points -= 50
            discount = 5
        else:
            discount = 0
        return discount, self.points
