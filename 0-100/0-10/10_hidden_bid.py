bidders_data = {}


def bidder_finder(dict) -> None:
    key_list = list(dict.keys())
    val_list = list(dict.values())

    best_bidder_value = max(dict.values())
    best_bidder_index = val_list.index(best_bidder_value)
    print(
        f"The highest bidder is {key_list[best_bidder_index]} with bid of ${best_bidder_value}"
    )


def add_bidder(dict, name, bid) -> None:
    dict[name] = bid


def main() -> None:
    while True:
        print("1. New hidden bid")
        print("2. Exit")

        user_input = int(input("Choose your option: "))

        if user_input == 1:
            while True:
                bidder_name = input("Add the name of the bidder: ")
                bidder_value = int(input("Add the bid value: "))

                add_bidder(bidders_data, bidder_name, bidder_value)

                user_choice = int(
                    input(
                        "Do you want to add another bidder? 1. Yes 2. No, continue with the results: "
                    )
                )

                if user_choice == 2:
                    bidder_finder(bidders_data)
                    break
        if user_input == 2:
            break


if __name__ == "__main__":
    main()
