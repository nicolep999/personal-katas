import re


def main():

    user_input = input()

    regex = r"(?:(#|\|)(?P<item_name>[A-Za-z\s]+)\1(?P<expiration_date>\d{2}/\d{2}/\d{2})\1(?P<calories>\d{1,5})\1)"

    matches = re.finditer(regex, user_input)

    food_items = []
    total_calories = 0

    for match in matches:
        item_name = match.group("item_name")
        expiration_date = match.group("expiration_date")
        calories = int(match.group("calories"))

        food_items.append((item_name, expiration_date, calories))

        total_calories += calories

    days = total_calories // 2000

    print(f"You have food to last you for: {days} days!")
    for item in food_items:
        print(f"Item: {item[0]}, Best before: {item[1]}, Nutrition: {item[2]}")


main()
