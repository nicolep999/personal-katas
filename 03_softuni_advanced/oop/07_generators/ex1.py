class Test:
    def __init__(self, name):
        self.name = name
        self.index = -1

    def __next__(self):
        self.index += 1
        try:
            return self.name[self.index]
        except IndexError:
            raise StopIteration

    def __iter__(self):
        return self


my_object = Test("Test")

for c in my_object:
    print(c)
