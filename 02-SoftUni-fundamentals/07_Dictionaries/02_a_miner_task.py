def main():

    user_dict = {}

    while True:

        user_input = input()

        if user_input == "stop":
            for x in user_dict:
                print(f"{x} -> {user_dict[x]}")
            break

        user_quantity = int(input())

        if user_input in user_dict:
            user_dict[user_input] += user_quantity
        else:
            user_dict[user_input] = user_quantity


main()
