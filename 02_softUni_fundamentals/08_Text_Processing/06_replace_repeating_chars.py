def main():
    user_input = input()
    new_seq = ""

    current_letter = ""

    for letter in user_input:
        if letter != current_letter:
            new_seq += letter
        current_letter = letter
    print(new_seq)


main()
