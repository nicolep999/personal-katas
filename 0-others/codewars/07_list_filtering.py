# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
def filter_list(l):
    return [x for x in l if isinstance(x, int) and x >= 0]


print(filter_list([1, 2, "a", "b"]))
print(filter_list([1, "a", "b", 0, 15]) == [1, 0, 15])
print(filter_list([1, 2, "aasf", "1", "123", 123]) == [1, 2, 123])
