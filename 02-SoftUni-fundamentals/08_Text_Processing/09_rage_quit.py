def main():
    user_input = input().upper()

    unique_symbols = 0
    current_symbol = ""

    current_index = 0

    end_result = ""

    for letter in user_input:

        if letter.isdigit():

            if (
                current_index < len(user_input) - 1
                and user_input[current_index + 1].isdigit()
            ):
                current_power = int(str(letter) + (str(user_input[current_index + 1])))
                end_result += current_symbol * int(current_power)

            else:
                end_result += current_symbol * int(letter)

            current_symbol = ""

        else:

            if letter not in current_symbol and letter not in end_result:
                unique_symbols += 1

            current_symbol += letter

        current_index += 1

    print(f"Unique symbols used: {unique_symbols}")
    print(f"{end_result}")


main()
