def main():
    user_input = input()
    index = 0

    for x in user_input:
        if x == ":":
            print(f"{x}{user_input[index + 1]}")
        index += 1


main()
