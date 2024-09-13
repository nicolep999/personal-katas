n = int(input())

user_set = set()

for _ in range(n):
    user_set.add(input())

print(*user_set, sep="\n")
