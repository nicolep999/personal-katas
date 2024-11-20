class dictionary_iter:
    def __init__(self, dictionary: dict) -> None:
        self.dictionary = list(dictionary.items())
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= len(self.dictionary):
            raise StopIteration
        result = self.dictionary[self.current_index]
        self.current_index += 1
        return result


test_result = dictionary_iter({1: "1", 2: "2"})
for x in test_result:
    print(x)
