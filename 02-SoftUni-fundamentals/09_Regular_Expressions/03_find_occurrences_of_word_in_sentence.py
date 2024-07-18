import re


def main():
    user_input = input().lower()
    target_word = input().lower()

    regex = r"\b" + re.escape(target_word) + r"\b"
    matches = re.findall(regex, user_input)
    print(len(matches))


main()
