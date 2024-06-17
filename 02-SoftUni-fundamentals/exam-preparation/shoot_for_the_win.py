def main():
    seq_input = list(map(int, input().split(" ")))
    shot_targets = 0
    while True:
        command = input()
        if command == "End":
            break
        elif int(command) > len(seq_input) - 1:
            continue
        else:
            current_number = seq_input[int(command)]
            seq_input[int(command)] = -1
            shot_targets += 1
            for index in range(len(seq_input)):
                if seq_input[index] == -1:
                    continue
                elif seq_input[index] > current_number:
                    seq_input[index] -= current_number
                else:
                    seq_input[index] += current_number
    print(f"Shot targets: {shot_targets} -> {' '.join(map(str, seq_input))}")


if __name__ == "__main__":
    main()
