def does_item_exist(lst, item) -> bool:
    for index in range(len(lst)):
        if lst[index] == item:
            return True
    return False


def main():
    inventory = list(map(str, input().split(", ")))

    while True:

        command = input().split(" - ")
        if command[0] == "Craft!":
            print(f"{', '.join(inventory)}")
            break

        if command[0] == "Combine Items":
            combined = command[1].split(":")
            if does_item_exist(inventory, combined[0]):
                current_index = inventory.index(combined[0]) + 1
                inventory.insert(current_index, combined[1])
            else:
                continue

        elif command[0] == "Collect":
            if not does_item_exist(inventory, command[1]):
                inventory.append(command[1])

        if does_item_exist(inventory, command[1]):
            if command[0] == "Drop":
                for index in range(len(inventory)):
                    if inventory[index] == command[1]:
                        del inventory[index]
                        break

            elif command[0] == "Renew":
                for index in range(len(inventory)):
                    if inventory[index] == command[1]:
                        del inventory[index]
                        inventory.append(command[1])


main()
