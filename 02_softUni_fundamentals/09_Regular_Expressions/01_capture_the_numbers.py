import re

matches = []

while True:
    user_input = input()
    if user_input:
        regex = r"\d+"
        reg_matches = re.findall(regex, user_input)
        matches.extend(reg_matches)
    else:
        print(f"{' '.join(matches)}")
        break
