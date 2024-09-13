def main():
    user_input = input()

    while True:
        command = input()

        if command == "Travel":
            print(f"Ready for world tour! Planned stops: {user_input}")
            break

        action, x, y = command.split(":")

        if action == "Add Stop":
            x = int(x)
            if x <= len(user_input):
                user_input = user_input[:x] + y + user_input[x:]
            print(user_input)
        elif action == "Remove Stop":
            x = int(x)
            y = int(y) + 1
            if x >= 0 and y <= len(user_input):
                user_input = user_input[:x] + user_input[y:]
            print(user_input)

        elif action == "Switch":
            if x in user_input:
                user_input = user_input.replace(x, y)
            print(user_input)


main()
