def main():
    user_input = list(map(int, input().split(",")))

    positive_numbers = [x for x in user_input if x >= 0]
    negative_numbers = [x for x in user_input if x < 0]
    even_numbers = [x for x in user_input if x % 2 == 0]
    odd_numbers = [x for x in user_input if x % 2 != 0]

    print(
        f"Positive: {', '.join(map(str, positive_numbers))}\n"
        f"Negative: {', '.join(map(str, negative_numbers))}\n"
        f"Even: {', '.join(map(str, even_numbers))}\n"
        f"Odd: {', '.join(map(str, odd_numbers))}"
    )


main()
