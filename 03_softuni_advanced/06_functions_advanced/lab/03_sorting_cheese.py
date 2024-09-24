def sorting_cheeses(**kwargs):
    sorted_result = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ""
    for key, value in sorted_result:
        result += f"{key}\n"
        sorted_quantity_list = sorted(value, reverse=True)
        result += "\n".join(str(el) for el in sorted_quantity_list) + "\n"
    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

print(sorting_cheeses(Parmigiano=[165, 215], Feta=[150, 515], Brie=[150, 125]))
