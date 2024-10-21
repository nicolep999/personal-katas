def main():
    user_countries = list(map(str, input().split(", ")))
    user_capitals = list(map(str, input().split(", ")))

    user_dict = {
        country: capital for country, capital in zip(user_countries, user_capitals)
    }

    for country, capital in user_dict.items():
        print(f"{country} -> {capital}")


main()
