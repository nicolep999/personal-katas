def does_item_exist(lst, item) -> bool:
    return item in lst


def main():
    treasure_map = input().split("|")

    while True:
        command = input().split(" ")

        if command[0] == "Yohoho!":
            break

        if command[0] == "Loot":
            for item in command[1:]:
                if not does_item_exist(treasure_map, item):
                    treasure_map.insert(0, item)

        elif command[0] == "Drop":
            index = int(command[1])
            if 0 <= index < len(treasure_map):
                item = treasure_map.pop(index)
                treasure_map.append(item)

        elif command[0] == "Steal":
            count = int(command[1])
            stolen_items = treasure_map[-count:]
            treasure_map = treasure_map[:-count]
            print(", ".join(stolen_items))

    if treasure_map:
        total_length = sum(len(item) for item in treasure_map)
        average_gain = total_length / len(treasure_map)
        print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
    else:
        print("Failed treasure hunt.")


main()
