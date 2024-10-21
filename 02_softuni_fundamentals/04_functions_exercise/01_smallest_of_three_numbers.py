def smallest_of_three() -> int:
    number = int(input())
    for _ in range(2):
        int_input = int(input())
        if int_input > number:
            continue
        number = int_input
    return number


print(smallest_of_three())
