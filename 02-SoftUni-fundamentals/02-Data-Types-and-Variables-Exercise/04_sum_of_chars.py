    lines_number = int(input())
    total_sum = 0
    for _ in range(lines_number):
        user_input = input()
        total_sum += ord(user_input)

    print(f"The sum equals: {total_sum}")
