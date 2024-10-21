def main():
    won_battles = 0
    battles_counter = 0
    initial_energy = int(input())

    while True:
        enemy_distance = input()
        if enemy_distance == "End of battle":
            print(f"Won battles: {won_battles}. Energy left: {initial_energy}")
            break
        if initial_energy - int(enemy_distance) >= 0:
            won_battles += 1
            battles_counter += 1
            if battles_counter == 3:
                initial_energy += won_battles
                battles_counter = 0
            initial_energy -= int(enemy_distance)
        else:
            print(
                f"Not enough energy! Game ends with {won_battles} won battles and {initial_energy} energy"
            )
            break


main()
