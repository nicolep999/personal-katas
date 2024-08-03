class Inventory:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.items = []

    def add_item(self, item: str):
        if len(self.items) < self.__capacity:
            self.items.append(item)
            return
        return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        items_str = ", ".join(self.items)
        left_capacity = self.__capacity - len(self.items)
        return f"Items: {items_str}.\nCapacity left: {left_capacity}"
