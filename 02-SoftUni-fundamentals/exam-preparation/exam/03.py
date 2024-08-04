def main():

    meal_collection = {}
    unliked_meals_count = 0

    while True:
        command = input()

        if command == "Stop":
            for guest, meals in meal_collection.items():
                print(f"{guest}: {', '.join(meals)}")
            print(f"Unliked meals: {unliked_meals_count}")
            break

        action, guest, meal = command.split("-")

        if action == "Like":
            if guest not in meal_collection:
                meal_collection[guest] = []
            if meal not in meal_collection[guest]:
                meal_collection[guest].append(meal)

        elif action == "Dislike":
            if guest not in meal_collection:
                print(f"{guest} is not at the party.")
            elif meal not in meal_collection[guest]:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
            else:
                meal_collection[guest].remove(meal)
                print(f"{guest} doesn't like the {meal}.")
                unliked_meals_count += 1


main()
