def perfect_number(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    sum_divisors = sum(divisors)

    if sum_divisors == n:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


user_input = int(input())
print(perfect_number(user_input))
