def main():

    houses_list = list(map(int, input().split("@")))

    last_house = 0

    while True:
        command = input()

        if command == "Love!":

            print(f"Cupid's last position was {last_house}.")

            houses_checked = 0
            houses_failed = 0

            for houses in houses_list:
                if houses == 0:
                    houses_checked += 1
                else:
                    houses_failed -= 1

            if houses_checked < len(houses_list):
                print(f"Cupid has failed {abs(houses_failed)} places.")

            else:
                print("Mission was successful.")

            break

        command = command.split(" ")

        current_house = last_house + int(command[1])
        if current_house >= len(houses_list):
            current_house = 0
            last_house = 0

        if houses_list[current_house] == 0:
            print(f"Place {current_house} already had Valentine's day.")
            last_house = current_house
            continue

        houses_list[current_house] -= 2
        last_house = current_house

        if houses_list[current_house] == 0:
            print(f"Place {current_house} has Valentine's day.")


main()
