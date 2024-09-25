def grocery_store(**kwargs):
    sorted_products = sorted(
        kwargs.items(), key=lambda item: (-item[1], -len(item[0]), item[0])
    )

    receipt_lines = [f"{name}: {quantity}" for name, quantity in sorted_products]

    return "\n".join(receipt_lines)


print(
    grocery_store(
        bread=5,
        pasta=12,
        eggs=12,
    )
)

print("***")

print(
    grocery_store(
        bread=2,
        pasta=2,
        eggs=20,
        carrot=1,
    )
)
