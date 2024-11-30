from abc import ABC
from project.products.base_product import BaseProduct


class HobbyHorse(BaseProduct, ABC):
    def __init__(self, model: str, price: float):
        super().__init__(
            model=model, price=price, material="Wood/Plastic", sub_type="Toys"
        )

    def discount(self):
        self.price *= 0.20
