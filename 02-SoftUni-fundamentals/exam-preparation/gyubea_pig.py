def main():
    food_quantity = int(float(input()) * 1000)
    hay_quantity = int(float(input()) * 1000)
    cover_quantity = int(float(input()) * 1000)
    pig_weight = float(input()) * 1000

    days_passed = 1

    success = True

    while days_passed <= 30:
        if (
            int(food_quantity) <= 0
            or int(hay_quantity) <= 0
            or int(cover_quantity) <= 0
        ):
            success = False
            break

        food_quantity -= 300

        if days_passed % 2 == 0:
            hay_quantity -= food_quantity * 0.05
        if days_passed % 3 == 0:
            cover_quantity -= pig_weight / 3

        days_passed += 1

    if int(food_quantity) <= 0 or int(hay_quantity) <= 0 or int(cover_quantity) <= 0:
        success = False

    if success:
        print(
            f"Everything is fine! Puppy is happy! Food: {(food_quantity / 1000):.2f}, Hay: {(hay_quantity / 1000):.2f}, Cover: {(cover_quantity / 1000):.2f}."
        )

    else:
        print("Merry must go to the pet store!")


main()
