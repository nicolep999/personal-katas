import re


def extract_emails(text):
    regex = re.compile(
        r"\b(?<![\.\-_])[a-zA-Z0-9]+(?:[._-][a-zA-Z0-9]+)*@[a-zA-Z]+(?:-[a-zA-Z]+)*(?:\.[a-zA-Z]+(?:-[a-zA-Z]+)*)+\b"
    )
    matches = regex.findall(text)
    for match in matches:
        print(match)


def main():
    user_input = input()
    extract_emails(user_input)


main()
