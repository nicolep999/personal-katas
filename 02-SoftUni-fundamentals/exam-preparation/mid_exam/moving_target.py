def main():
    sequence = list(map(int, input().split(" ")))
    while True:
        command = input()
        if command == "End":
            print(f"{'|'.join(map(str, sequence))}")
            break
        else:
            new_command = command.split(" ")
            action = new_command[0]
            index = int(new_command[1])
            value = int(new_command[2])
            if action == "Shoot":
                if index >= len(sequence) or index < 0:
                    continue
                else:
                    sequence[index] -= value
                    if sequence[index] <= 0:
                        del sequence[index]
            if action == "Add":
                if index > len(sequence) - 1 or index < 0:
                    print("Invalid placement!")
                    continue
                else:
                    sequence.insert(index, value)
            if action == "Strike":
                if index - value < 0 or index + value >= len(sequence):
                    print("Strike missed!")
                    continue
                else:
                    left_index = index - value
                    right_index = index + value
                    del sequence[left_index : right_index + 1]


if __name__ == "__main__":
    main()
