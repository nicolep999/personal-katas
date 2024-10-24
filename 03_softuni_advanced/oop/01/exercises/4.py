class Cup:

    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity

    def fill(self, quantity: int) -> int:
        if self.quantity + quantity <= self.size:
            self.quantity += quantity
            return self.quantity

    def status(self) -> int:
        return self.size - self.quantity
