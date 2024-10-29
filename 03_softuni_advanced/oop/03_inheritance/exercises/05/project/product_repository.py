from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products: list[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Product | None:
        is_available = next((p for p in self.products if p.name == product_name), None)
        if is_available:
            return is_available

    def remove(self, product_name: str) -> None:
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self) -> str:
        return "\n".join(
            f"{product.name}: {product.quantity}" for product in self.products
        )
