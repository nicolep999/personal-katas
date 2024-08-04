import re


def main():
    user_n = int(input())
    regex = r"^(\$|%)([A-Z][a-z]{2,})\1: (\[\d+\]\|\[\d+\]\|\[\d+\]\|)$"

    for _ in range(user_n):
        input_string = input()
        user_match = re.match(regex, input_string)

        if user_match:
            tag = user_match.group(2)
            number_groups = re.findall(r"\d+", user_match.group(3))
            decrypted_message = "".join(chr(int(num)) for num in number_groups)
            print(f"{tag}: {decrypted_message}")
        else:
            print("Valid message not found!")


main()
