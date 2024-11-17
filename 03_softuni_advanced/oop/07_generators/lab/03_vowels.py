class vowels:

    def __init__(self, data: str) -> None:
        self.data = data
        self.only_vowels = [el for el in self.data if el.lower() in "aeiouy"]
        self.index = -1

    def __iter__(self):
        return iter(self.only_vowels)

    # def __next__(self):
    #     self.index += 1
    #     if self.index < len(self.only_vowels):
    #         return self.only_vowels[self.index]
    #     else:
    #         raise StopIteration


my_string = vowels("Abcedifuty0o")
for char in my_string:
    print(char)
