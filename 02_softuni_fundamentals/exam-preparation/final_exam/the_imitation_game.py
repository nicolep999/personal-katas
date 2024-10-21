def main():
    encrypted_message = input()

    while True:

        command = input()

        if command == "Decode":
            print(f"The decrypted message is: {encrypted_message}")
            break

        command = command.split("|")
        n = command[1]

        if command[0] == "Move":
            n = int(command[1])
            encrypted_message = encrypted_message[n:] + encrypted_message[:n]
            continue

        x = command[2]

        if command[0] == "Insert":
            n = int(command[1])
            encrypted_message = encrypted_message[:n] + x + encrypted_message[n:]

        elif command[0] == "ChangeAll":
            encrypted_message = encrypted_message.replace(n, x)


main()
