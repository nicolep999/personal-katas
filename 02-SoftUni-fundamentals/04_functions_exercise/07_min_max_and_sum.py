def main(n):
    return f"The minimum number is {min(n)}\nThe maximum number is {max(n)}\nThe sum number is: {sum(n)}"


user_input = list(map(int, input().split()))
print(main(user_input))
