import re


def main():
    input_string = input()
    pattern = r"(=|\/)([A-Z][a-zA-Z]{2,})\1"

    matches = re.findall(pattern, input_string)
    destinations = [match[1] for match in matches]
    travel_points = sum(len(destination) for destination in destinations)

    print(f"Destinations: {', '.join(destinations)}")
    print(f"Travel Points: {travel_points}")


main()
