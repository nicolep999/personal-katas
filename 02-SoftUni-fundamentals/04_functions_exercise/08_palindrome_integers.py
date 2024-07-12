def main(n):
    for x in n:
        if str(x) == str(x)[::-1]:
            print(True)
        else:
            print(False)


user_input = list(map(int, input().split(", ")))
main(user_input)
