from collections import deque

food_quantity = int(input())
all_orders = deque(map(int, input().split()))

print(max(all_orders))

while all_orders:
    current_order = all_orders[0]
    if current_order > food_quantity:
        print(f"Orders left: {' '.join(map(str, all_orders))}")
        break
    food_quantity -= all_orders.popleft()
    if len(all_orders) == 0:
        print("Orders complete")
        break
