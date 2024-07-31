def main():

    parking = {}

    users = int(input())

    for _ in range(users):

        user_input = input().split()

        command = user_input[0]
        username = user_input[1]

        if command == "register":
            licence_plate = user_input[2]
            if username in parking:
                print(
                    f"ERROR: already registered with plate number {parking[username]}"
                )
            else:
                parking[username] = licence_plate
                print(f"{username} registered {licence_plate} successfully")

        elif command == "unregister":
            if username not in parking:
                print(f"ERROR: user {username} not found")
            else:
                del parking[username]
                print(f"{username} unregistered successfully")

    for x in parking:
        print(f"{x} => {parking[x]}")


main()
