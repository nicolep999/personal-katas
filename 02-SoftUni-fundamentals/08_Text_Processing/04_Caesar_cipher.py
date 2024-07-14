def main():
    user_input = input()
    final_result = ""

    for x in user_input:
        current_index = ord(x)
        new_index = current_index + 3
        final_result += chr(new_index)

    print(final_result)


main()
