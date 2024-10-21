user_input = input()

storage = {}

for char in user_input:
    if char in storage:
        storage[char] += 1
    else:
        storage[char] = 1

for x in sorted(storage):
    print(f"{x}: {storage[x]} time/s")
