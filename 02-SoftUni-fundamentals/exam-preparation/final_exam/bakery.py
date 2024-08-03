def main():
    bakery_storage = {}
    total_goods_sold = 0
    while True:
        command = input().split(" ")
        if command[0] == "Complete":
            for item in bakery_storage:
                print(f"{item}: {bakery_storage[item]}")
            print(f"All sold: {total_goods_sold} goods")
            break
        product_quantity = int(command[1])
        product_name = command[2]
        if command[0] == "Receive":
            if product_name in bakery_storage:
                bakery_storage[product_name] += product_quantity
            elif product_quantity > 0:
                bakery_storage[product_name] = product_quantity
        if command[0] == "Sell":
            if product_name not in bakery_storage:
                print(f"You do not have any {product_name}.")
            elif bakery_storage[product_name] < product_quantity:
                print(
                    f"There aren't enough {product_name}. You sold the last {bakery_storage[product_name]} of them."
                )
                total_goods_sold += bakery_storage[product_name]
                del bakery_storage[product_name]
            else:
                total_goods_sold += product_quantity
                bakery_storage[product_name] -= product_quantity
                print(f"You sold {product_quantity} {product_name}.")
                if bakery_storage[product_name] == 0:
                    del bakery_storage[product_name]


if __name__ == "__main__":
    main()
