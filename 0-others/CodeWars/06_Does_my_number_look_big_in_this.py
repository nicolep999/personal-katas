# https://www.codewars.com/kata/5287e858c6b5a9678200083c


def narcissistic(value) -> bool:
    power_sum = 0
    is_narcissistic = False
    for n in str(value):
        power_sum += int(n) ** len(str(value))
    if power_sum == value:
        is_narcissistic = True
    return is_narcissistic


print(narcissistic(10))
print(narcissistic(7))
print(narcissistic(122))
