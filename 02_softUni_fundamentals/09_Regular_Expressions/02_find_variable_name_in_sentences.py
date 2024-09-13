import re


def main():
    user_input = input()
    regex = r"\b_{1}[a-zA-Z0-9]+\b"
    reg_match = re.findall(regex, user_input)
    print_matches = [match[1:] for match in reg_match]
    print(f"{','.join(print_matches)}")


main()
