from collections import deque

customers = deque()

while True:
    command = input()
    if command == "End":
        print(f"{len(customers)} people remaining.")
        break
    elif command == "Paid":
        while customers:
            print(customers.popleft())
        continue
    customers.append(command)
