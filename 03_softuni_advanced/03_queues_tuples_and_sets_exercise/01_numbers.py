set_a = set([int(num) for num in input().split()])
set_b = set([int(num) for num in input().split()])

n = int(input())


cmd_mapper = {
    "Add First": lambda *numbers: set_a.update(map(int, numbers)),
    "Add Second": lambda *numbers: set_b.update(map(int, numbers)),
    "Remove First": lambda *numbers: set_a.difference_update(map(int, numbers)),
    "Remove Second": lambda *numbers: set_b.difference_update(map(int, numbers)),
    "Check Subset": lambda: print(set_a.issubset(set_b) or set_b.issubset(set_a)),
}

for _ in range(n):
    user_input = input().split()
    cmd = f"{user_input[0]} {user_input[1]}"
    cmd_mapper[cmd](*user_input[2:])


print(*sorted(set_a), sep=", ")
print(*sorted(set_b), sep=", ")
