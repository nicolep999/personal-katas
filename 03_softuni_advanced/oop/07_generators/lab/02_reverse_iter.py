class reverse_iter:

    def __init__(self, iterable) -> None:
        self.iterable: list = iterable
        self.end_index = len(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        self.end_index -= 1
        if self.end_index >= 0:
            return self.iterable[self.end_index]
        raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
