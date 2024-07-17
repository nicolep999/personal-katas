alphabet_list = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def cipher_maker(key, word) -> str:
    current_word = word.lower()
    new_word = ""
    for letter in range(len(current_word)):
        for index in range(len(alphabet_list)):
            if alphabet_list[index] == current_word[letter]:
                new_index = index + key
                if new_index > 25:
                    difference = new_index - 26
                    new_index = 0
                    new_index += difference
                new_word += alphabet_list[new_index]
    return new_word


def decipher_maker(key, word) -> str:
    current_word = word.lower()
    new_word = ""
    for letter in range(len(current_word)):
        for index in range(len(alphabet_list)):
            if alphabet_list[index] == current_word[letter]:
                new_index = index - key
                if new_index < 0:
                    difference = 1 + new_index
                    new_index = -1
                    new_index += difference
                new_word += alphabet_list[new_index]
    return new_word


def main():
    while True:
        print("1. Create a cipher")
        print("2. Decipher a word")
        print("3. Exit")
        user_options = int(input("Please choose your option: "))
        if user_options == 1:
            user_shift = int(input("Please choose your shift: "))
            user_word = input("Please choose your word: ")
            current_cipher = cipher_maker(user_shift, user_word)
            print("")
            print(f"Your word is: {current_cipher}")
            print("")
        elif user_options == 2:
            user_shift = int(input("Please choose your shift: "))
            user_word = input("Please choose your cipher: ")
            current_cipher = decipher_maker(user_shift, user_word)
            print("")
            print(f"Your cipher is: {current_cipher}")
            print("")

        else:
            break


if __name__ == "__main__":
    main()
