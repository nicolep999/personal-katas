from typing import NamedTuple, Any, Optional


class Pair(NamedTuple):
    key: Any
    value: Any


class HashTable:

    def __init__(self, capacity: Optional[int] = 4) -> None:
        if capacity is None or capacity <= 0:
            raise ValueError("Capacity must be a positive integer")
        self.capacity: int = capacity
        self._array: list = [None] * self.capacity

    @property
    def array(self) -> list:
        return [pair for pair in self._array if pair]

    @property
    def keys(self) -> list:
        return [pair.key for pair in self._array if pair]

    def hash(self, key: Any) -> int:
        if key is None:
            raise ValueError("Key cannot be None")
        return hash(key) % self.capacity

    @property
    def values(self) -> list:
        return [pair.value for pair in self._array if pair]

    def add(self, key: Any, value: Any) -> None:
        if key is None:
            raise ValueError("Key cannot be None")
        self[key] = value

    def get(self, key: Any) -> Any:
        try:
            return self[key]
        except KeyError as e:
            raise KeyError(f"Key '{key}' not found") from e

    def __delitem__(self, key):
        if key is None:
            raise ValueError("Key cannot be None")
        self._array[self.hash(key)] = None

    def __setitem__(self, key: Any, value: Any):
        if key is None:
            raise ValueError("Key cannot be None")
        self._array[self.hash(key)] = Pair(key, value)

    def __getitem__(self, key: Any) -> Any:
        if key is None:
            raise ValueError("Key cannot be None")
        pair = self._array[self.hash(key)]
        if pair is None:
            raise KeyError(f"Key '{key}' not found")
        return pair.value

    def __len__(self) -> int:
        return sum(1 for pair in self._array if pair is not None)

    def __repr__(self) -> str:
        return repr(self._array)


table = HashTable()
try:
    table["name"] = "Peter"
    table["age"] = 25

    print(table)
    print(table.get("name"))
    print(table["age"])
    print(len(table))
except Exception as e:
    print(f"An error occurred: {e}")
