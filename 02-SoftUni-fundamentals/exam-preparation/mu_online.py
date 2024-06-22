def main():
    player_health = 100
    player_bitcoins = 0
    rooms_reached = 0
    has_lost = False

    dungeon_map = list(map(str, input().split("|")))

    for index in range(len(dungeon_map)):
        player_action_divider = dungeon_map[index].split(" ")
        action = player_action_divider[0]
        value = int(player_action_divider[1])

        rooms_reached += 1

        if action == "potion":

            effective_heal = min(value, 100 - player_health)
            player_health += effective_heal
            print(f"You healed for {effective_heal} hp.")
            print(f"Current health: {player_health} hp.")

        elif action == "chest":

            print(f"You found {value} bitcoins.")
            player_bitcoins += value

        else:
            player_health -= value

            if player_health > 0:
                print(f"You slayed {action}.")
            else:
                print(f"You died! Killed by {action}.")
                print(f"Best room: {rooms_reached}")
                has_lost = True
                break

    if not has_lost:
        print("You've made it!")
        print(f"Bitcoins: {player_bitcoins}")
        print(f"Health: {player_health}")


main()
