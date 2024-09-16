from collections import deque

materials = [int(num) for num in input().split()]
magic = deque([int(num) for num in input().split()])

storage = {}

cmd_mapper = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}

while magic and materials:
    current_magic = magic[0] * materials[-1]
    if current_magic in cmd_mapper:
        current_present = cmd_mapper[current_magic]
        if current_present not in storage:
            storage[current_present] = 0
        storage[current_present] += 1
        materials.pop()
        magic.popleft()

    elif current_magic < 0:
        materials.append(magic.popleft() + materials.pop())
    elif current_magic > 0:
        magic.popleft()
        materials[-1] += 15
    else:
        if materials[-1] == 0:
            materials.pop()
        if magic[0] == 0:
            magic.popleft()

if ("Doll" in storage and "Wooden train" in storage) or (
    "Teddy bear" in storage and "Bicycle" in storage
):
    print(f"The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join([str(m) for m in materials[::-1]])}")
if magic:
    print(f"Magic left: {', '.join([str(m) for m in magic])}")

for k, value in sorted(storage.items()):
    print(f"{k}: {value}")
