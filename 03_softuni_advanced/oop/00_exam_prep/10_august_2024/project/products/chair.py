from abc import ABC
from project.products.base_product import BaseProduct


class Chair(BaseProduct, ABC):

    def __init__(self, model: str, price: float):
        self.model = model
        self.price = price
        super().__init__(
            model=model, price=price, material="Wood", sub_type="Furniture"
        )

    def discount(self):
        self.price *= 0.10
