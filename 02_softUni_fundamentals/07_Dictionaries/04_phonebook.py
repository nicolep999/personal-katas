def main():

    phonebook = {}

    while True:

        user_input = input()

        if user_input.isdigit():
            for _ in range(int(user_input)):
                contact = input()

                if contact in phonebook:
                    print(f"{contact} -> {phonebook[contact]}")
                else:
                    print(f"Contact {contact} does not exist.")
            break

        user_input = user_input.split("-")
        phonebook[user_input[0]] = user_input[1]


main()
