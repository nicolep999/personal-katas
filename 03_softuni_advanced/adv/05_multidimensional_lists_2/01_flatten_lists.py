sublist = input().split("|")
flattened = []

for sub in reversed(sublist):
    flattened.extend(sub.split())


print(f"{' '.join(flattened)}")
