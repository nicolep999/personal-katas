def odd_and_even(n):
    n_list = [int(x) for x in str(n)]

    sum_of_odd_digits = 0
    sum_of_even_digits = 0

    for x in n_list:
        if x % 2 == 0:
            sum_of_even_digits += x
        else:
            sum_of_odd_digits += x

    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"


user_input = int(input())

print(odd_and_even(user_input))
