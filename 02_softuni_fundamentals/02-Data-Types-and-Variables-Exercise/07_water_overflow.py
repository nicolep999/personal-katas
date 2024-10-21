number_of_actions = int(input())
tank_capacity = 255
current_water = 0

for _ in range(number_of_actions):
    liters = int(input())
    if current_water + liters > tank_capacity:
        print("Insufficient capacity!")
    else:
        current_water += liters

print(current_water)
