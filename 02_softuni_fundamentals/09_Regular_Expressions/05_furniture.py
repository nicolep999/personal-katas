import re


def main():
    bought_furniture = []
    money_spend = 0
    regex = r"\b[A-Za-z0-9.]+"
    while True:

        command = input()

        if command == "Purchase":
            print("Bought furniture:")
            for x in bought_furniture:
                print(x)
            print(f"Total money spend: {money_spend:.2f}")
            break

        command_splitter = re.findall(regex, command)

        if len(command_splitter) < 3:
            continue

        bought_furniture.append(command_splitter[0])
        price = float(command_splitter[1])
        quantity = int(command_splitter[2])
        money_spend += price * quantity


main()
