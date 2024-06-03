quantity = int(input())
days = int(input())

total_cost = 0
total_spirit = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2

    if day % 2 == 0:
        total_cost += quantity * 2  # Ornament Sets
        total_spirit += 5

    if day % 3 == 0:
        total_cost += quantity * 5  # Tree Skirts
        total_cost += quantity * 3  # Tree Garlands
        total_spirit += 3 + 10

    if day % 5 == 0:
        total_cost += quantity * 15  # Tree Lights
        total_spirit += 17
        if day % 3 == 0:
            total_spirit += 30

    if day % 10 == 0:
        total_spirit -= 20
        total_cost += quantity * 5  # Tree Skirt (due to cat)
        total_cost += quantity * 3  # Tree Garland (due to cat)
        total_cost += quantity * 15  # Tree Lights (due to cat)

if days % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
