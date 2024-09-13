numbers = list(map(int, input().split()))
n = int(input())

for _ in range(n):
    numbers.remove(min(numbers))

print(", ".join(map(str, numbers)))
