def main():
    user_string = input()

    while True:
        command = input()
        if command == "Finish":
            break

        command = command.split()

        if command[0] == "Replace":
            current_char = command[1]
            new_char = command[2]
            user_string = user_string.replace(current_char, new_char)
            print(user_string)
        elif command[0] == "Cut":
            start_index = int(command[1])
            end_index = int(command[2])
            if start_index < 0 or end_index >= len(user_string):
                print(f"Invalid indices!")
                continue
            user_string = user_string[:start_index] + user_string[end_index + 1 :]
            print(user_string)
        elif command[0] == "Make":
            user_action = command[1]
            if user_action == "Upper":
                user_string = user_string.upper()
            else:
                user_string = user_string.lower()
            print(user_string)
        elif command[0] == "Check":
            user_action = command[1]
            if user_action in user_string:
                print(f"Message contains {user_action}")
            else:
                print(f"Message doesn't contain {user_action}")
        elif command[0] == "Sum":
            start_index = int(command[1])
            end_index = int(command[2])
            if start_index < 0 or end_index >= len(user_string):
                print(f"Invalid indices!")
                continue
            substring = user_string[start_index : end_index + 1]
            ascii_sum = sum(ord(char) for char in substring)
            print(ascii_sum)


main()

"""
ILikeSoftUni
Replace I We
Make Upper
Check SoftUni
Sum 1 4
Cut 1 4
Finish
"""
