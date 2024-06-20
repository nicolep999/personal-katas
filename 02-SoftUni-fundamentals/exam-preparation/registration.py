def main():
    user_name = input()
    while True:
        command = input().split(" ")
        if command[0] == "Letters":
            if command[1] == "Lower":
                user_name = user_name.lower()
                print(user_name)
            else:
                user_name = user_name.upper()
                print(user_name)
        elif command[0] == "Reverse":
            start_index = int(command[1])
            end_index = int(command[2]) + 1
            if end_index - 1 < len(user_name):
                substring = user_name[start_index:end_index]
                print(f"{substring[::-1]}")
        elif command[0] == "Substring":
            substring = command[1]
            found = False
            for index in range(len(user_name)):
                end_index = index + len(substring)
                if user_name[index:end_index] == substring:
                    found = True
                    user_name = user_name.replace(f"{user_name[index:end_index]}", "")
                    print(user_name)
                    break
            if not found:
                print(f"The username {user_name} doesn't contain {substring}.")
        elif command[0] == "Replace":
            user_name = user_name.replace(f"{command[1]}", "-")
            print(user_name)
        elif command[0] == "IsValid":
            is_valid = False
            for letter in user_name:
                if letter == command[1]:
                    is_valid = True
                    print("Valid username.")
                    break
            if not is_valid:
                print(f"{command[1]} must be contained in your username.")
        elif command[0] == "Registration":
            break


if __name__ == "__main__":
    main()
