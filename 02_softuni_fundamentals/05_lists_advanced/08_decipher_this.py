def main():
    secret_message = input()

    words = secret_message.split()

    deciphered_words = []
    for word in words:
        char_code = "".join([char for char in word if char.isdigit()])
        first_char = chr(int(char_code))

        rest_of_word = word[len(char_code) :]

        if len(rest_of_word) > 1:
            rest_of_word = rest_of_word[-1] + rest_of_word[1:-1] + rest_of_word[0]

        deciphered_word = first_char + rest_of_word
        deciphered_words.append(deciphered_word)

    final_message = " ".join(deciphered_words)

    print(final_message)


main()
