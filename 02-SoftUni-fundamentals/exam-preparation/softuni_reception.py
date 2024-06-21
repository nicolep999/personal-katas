def main():
    employee_efficiency = 0
    hours_count = 0
    for _ in range(3):  # Bruteforce as they're always 3 employees
        employee = int(input())
        employee_efficiency += employee
    students_count = int(input())
    while True:
        if students_count <= 0:
            print(f"Time needed: {hours_count}h.")
            break
        hours_count += 1
        if hours_count % 4 == 0:
            continue
        students_count -= employee_efficiency


if __name__ == "__main__":
    main()
