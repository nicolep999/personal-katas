def main():
    user_input = list(map(int, input().split(".")))
    if user_input[1] == 9 and user_input[2] == 9:
        user_input[0] += 1
        user_input[1] = 0
        user_input[2] = 0
    elif user_input[2] == 9:
        user_input[1] += 1
        if user_input[1] == 10:
            user_input[1] = 0
        user_input[2] = 0
    else:
        user_input[2] += 1

    print(f"{'.'.join(map(str, user_input))}")


main()
