def main():
    user_input = input()
    start_index = len(user_input)
    for x in reversed(user_input):
        if x == "\\":
            break
        start_index -= 1

    working_area = user_input[start_index:].split(".")

    print(f"File name: {working_area[0]}\nFile extension: {working_area[1]}")


main()
