def main(*args):
    numbers = [int(x) for x in args[0].split()]

    negative_numbers = [x for x in numbers if x < 0]
    positive_numbers = [x for x in numbers if x > 0]

    negative_sum = sum(negative_numbers)
    positive_sum = sum(positive_numbers)

    print(negative_sum)
    print(positive_sum)

    if abs(negative_sum) > positive_sum:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


main(input())
