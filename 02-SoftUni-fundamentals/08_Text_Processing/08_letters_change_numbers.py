import re


def main():
    user_input = list(map(str, input().split()))
    total_sum = 0
    temp_sum = 0

    for x in user_input:
        first_letter = x[0]
        last_letter = x[-1]
        end_index = int(len(user_input) - 1)
        number_get = re.findall(r"\d+", x)
        number = int(number_get[0])

        if first_letter.isupper():
            operation = ord(first_letter.lower()) - ord("a") + 1
            temp_sum = number / operation
        else:
            operation = ord(first_letter.lower()) - ord("a") + 1
            temp_sum = number * operation

        if last_letter.isupper():
            operation = ord(last_letter.lower()) - ord("a") + 1
            temp_sum = temp_sum - operation
        else:
            operation = ord(last_letter.lower()) - ord("a") + 1
            temp_sum = temp_sum + operation

        total_sum += temp_sum
        temp_sum = 0

    print(f"{total_sum:.2f}")


main()
