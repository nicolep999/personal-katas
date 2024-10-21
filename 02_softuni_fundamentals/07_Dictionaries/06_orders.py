def main():
    storage = {}

    while True:
        user_input = input()

        if user_input == "buy":
            break

        name, price, quantity = user_input.split()
        price = float(price)
        quantity = int(quantity)

        if name in storage:
            current_price, current_quantity = storage[name]
            storage[name] = (price, current_quantity + quantity)
        else:
            storage[name] = (price, quantity)

    for product, (price, quantity) in storage.items():
        total_price = price * quantity
        print(f"{product} -> {total_price:.2f}")


main()
