# Very stupid solution, but works
def main():
    sequence = list(map(str, input().split(" ")))
    player_moves = 0
    while True:
        validator = True
        command = input().split(" ")
        if not sequence and command[0] != "end":
            continue
        if len(sequence) <= 1:
            print(f"You have won in {player_moves} turns!")
            break
        elif command[0] == "end":
            print("Sorry you lose :(")
            print(f"{' '.join(map(str, sequence))}")
            break
        player_moves += 1
        for index in range(len(command)):
            if (
                int(command[index]) < 0
                or int(command[index]) >= len(sequence)
                or command[0] == command[1]
            ):
                print("Invalid input! Adding additional elements to the board")
                new_element = f"-{player_moves}a"
                sequence_middle = int(len(sequence) / 2)
                sequence = (
                    sequence[:sequence_middle]
                    + [new_element, new_element]
                    + sequence[sequence_middle:]
                )
                validator = False
                break
        if validator:
            index1 = int(command[0])
            index2 = int(command[1])
            if sequence[index1] == sequence[index2]:
                print(
                    f"Congrats! You have found matching elements - {sequence[index1]}!"
                )
                to_delete = [sequence[index1], sequence[index2]]
                sequence = [ele for ele in sequence if ele not in to_delete]
            else:
                print("Try again!")


if __name__ == "__main__":
    main()
