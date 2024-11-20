class countdown_iterator:

    def __init__(self, count: int) -> None:
        self.count = count + 1
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.count > 0:
            self.count -= 1
            return self.count
        raise StopIteration


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
