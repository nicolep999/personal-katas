def main():
    list_numbers = list(map(int, input().split(", ")))
    max_number = max(list_numbers)

    for group in range(10, max_number + 10, 10):
        group_numbers = [num for num in list_numbers if (group - 10) < num <= group]
        print(f"Group of {group}'s: {group_numbers}")


main()
