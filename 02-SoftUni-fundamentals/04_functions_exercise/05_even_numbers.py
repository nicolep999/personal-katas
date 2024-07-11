def even_numbers(n):
    return [x for x in n if x % 2 == 0]


user_input = list(map(int, input().split()))
print(even_numbers(user_input))
