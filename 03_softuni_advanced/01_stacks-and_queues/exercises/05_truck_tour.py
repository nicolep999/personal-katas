petrol_pumps = int(input())

current_balance = 0
start_index = 0

for i in range(petrol_pumps):
    petrol, distance = input().split()
    current_balance += int(petrol) - int(distance)

    if current_balance < 0:
        start_index = i + 1
        current_balance = 0

print(start_index)
