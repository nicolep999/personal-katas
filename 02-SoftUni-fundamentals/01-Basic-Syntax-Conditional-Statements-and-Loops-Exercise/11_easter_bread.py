budget = float(input())
price_flour_per_kg = float(input())

price_eggs_per_pack = price_flour_per_kg * 0.75
price_milk_per_liter = price_flour_per_kg * 1.25
price_milk_per_250ml = price_milk_per_liter * 0.25

price_per_loaf = price_flour_per_kg + price_eggs_per_pack + price_milk_per_250ml

number_of_loaves = 0
colored_eggs = 0

while budget >= price_per_loaf:
    number_of_loaves += 1
    colored_eggs += 3
    budget -= price_per_loaf

    if number_of_loaves % 3 == 0:
        colored_eggs -= (number_of_loaves - 2)

print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
