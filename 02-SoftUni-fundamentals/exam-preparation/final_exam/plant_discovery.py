def main():

    initial_n = int(input())
    storage = []

    for _ in range(initial_n):
        command = input().split("<->")
        plant = command[0]
        rarity = command[1]
        new_dict = {"plant": plant, "rarity": rarity, "rating": []}
        storage.append(new_dict)

    while True:
        command = input()

        if command == "Exhibition":
            print("Plants for the exhibition:")
            for item in storage:
                average_rating = 0
                if len(item["rating"]) > 0:
                    average_rating = sum(item["rating"]) / len(item["rating"])
                print(
                    f"- {item['plant']}; Rarity: {item['rarity']}; Rating: {average_rating:.2f}"
                )
            break

        command = command.split(": ")

        if command[0] == "Rate":
            plant, rating = command[1].split(" - ")
            plant_found = False
            for x in storage:
                if x["plant"] == plant:
                    plant_found = True
                    x["rating"].append(int(rating))
            if not plant_found:
                print("error")
        elif command[0] == "Update":
            plant, new_rarity = command[1].split(" - ")
            plant_found = False
            for x in storage:
                if x["plant"] == plant:
                    plant_found = True
                    x["rarity"] = new_rarity
            if not plant_found:
                print("error")
        elif command[0] == "Reset":
            plant = command[1]
            plant_found = False
            for x in storage:
                if x["plant"] == plant:
                    plant_found = True
                    x["rating"] = []

            if not plant_found:
                print("error")


main()
