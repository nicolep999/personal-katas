boxes = list(map(int, input().split()))
capacity = int(input())

total = 0
current_box = 0

while boxes:
    if boxes[-1] + current_box == capacity:
        total += 1
        current_box = 0
        boxes.pop()
    elif boxes[-1] + current_box > capacity:
        current_box = 0
        total += 1
    else:
        current_box += boxes.pop()
        if len(boxes) == 0:
            total += 1

print(total)
