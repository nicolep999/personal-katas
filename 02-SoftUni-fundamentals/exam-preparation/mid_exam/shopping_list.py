def does_element_exist(lst, el) -> bool:
    for index in range(len(lst)):
        if lst[index] == el:
            return True
    return False


def main():

    groceries_list = list(map(str, input().split("!")))

    while True:
        command = input()

        if command == "Go Shopping!":
            print(f"{', '.join(groceries_list)}")
            break

        command = command.split(" ")

        if command[0] == "Urgent":
            if not does_element_exist(groceries_list, command[1]):
                groceries_list.insert(0, command[1])

        if does_element_exist(groceries_list, command[1]):
            for index in range(len(groceries_list)):
                if command[0] == "Unnecessary":
                    if groceries_list[index] == command[1]:
                        del groceries_list[index]
                        break
                if command[0] == "Correct":
                    if groceries_list[index] == command[1]:
                        groceries_list[index] = command[2]
                        break
                if command[0] == "Rearrange":
                    if groceries_list[index] == command[1]:
                        del groceries_list[index]
                        groceries_list.append(command[1])
                        break


main()

"""
Milk!Pepper!Salt!Water!Banana
Unnecessary Salt
Urgent Salt 
Correct Pepper Onion
Rearrange Onion
Correct Tomatoes Potatoes
Go Shopping!

"""
