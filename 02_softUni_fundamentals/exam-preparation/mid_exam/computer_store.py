def main():
    user_sum = 0
    sum_with_taxes = 0
    taxes = 0
    while True:
        command = input()
        if command == "special" or command == "regular":
            if user_sum <= 0:
                print("Invalid order!")
                break
            taxes = user_sum * 0.20
            sum_with_taxes = user_sum + taxes
            if command == "special":
                sum_with_taxes *= 0.90
            print(f"Congratulations you've just bought a new computer!")
            print(f"Price without taxes: {user_sum:.2f}$\nTaxes: {taxes:.2f}$")
            print("-----------")
            print(f"Total price: {sum_with_taxes:.2f}$")
            break
        if float(command) <= 0:
            print("Invalid price!")
            continue
        user_sum += float(command)


if __name__ == "__main__":
    main()
