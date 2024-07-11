first_number = int(input())
second_number = int(input())
third_number = int(input())


def sum_numbers(a, b):
    return a + b


def subtract(a, b):
    return a - b


def add_and_subtract(first, second, third):
    add = sum_numbers(first, second)
    sub = subtract(add, third)
    print(sub)


add_and_subtract(first_number, second_number, third_number)
