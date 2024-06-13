travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"],
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"],
    },
]


def add_log(country, visits, cities):
    new_log = {"country": country, "visits": visits, "cities": [cities]}
    travel_log.append(new_log)
    print(travel_log)


def main():
    while True:
        user_country = input("Write the name of the country you want to add: ")
        user_visits = int(input("How many times did you visited it?: "))
        user_cities = input("Which cities did you visited? (Separated by comma): ")
        add_log(user_country, user_visits, user_cities)


if __name__ == "__main__":
    main()
