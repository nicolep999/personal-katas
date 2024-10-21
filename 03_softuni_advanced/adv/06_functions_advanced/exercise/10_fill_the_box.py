def fill_the_box(x, y, z, *args):
    box_size = x * y * z
    total_cubes = sum(arg for arg in args if isinstance(arg, int))
    cubes_used = 0

    for arg in args:
        if not isinstance(arg, int):
            break

        if box_size >= arg:
            box_size -= arg
            cubes_used += arg
        else:
            cubes_used += box_size
            box_size = 0
            break

    if box_size > 0:
        return f"There is free space in the box. You could put {box_size} more cubes."
    else:
        return f"No more free space! You have {total_cubes - cubes_used} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
