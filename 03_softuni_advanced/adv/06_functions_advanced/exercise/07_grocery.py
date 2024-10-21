def grocery_store(**kwargs):
    result = sorted(kwargs.items(), key=lambda x: (-x[1] - len(x[0]), x[0]))
    return "\n".join(f"{x}: {y}" for x, y in result)


print(
    grocery_store(
        bread=5,
        pasta=12,
        eggs=12,
    )
)
