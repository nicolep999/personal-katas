people = int(input())
capacity = int(input())
courses = 0
while True:
    people -= capacity
    courses += 1
    if people <= 0:
        print(courses)
        break
