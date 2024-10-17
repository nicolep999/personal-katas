from collections import deque


def main():
    packages_storage = [int(x) for x in input().split()]
    courier_storage = deque([int(x) for x in input().split()])

    total_weight = 0

    while packages_storage and courier_storage:
        package_weight = packages_storage.pop()
        courier_capacity = courier_storage.popleft()

        if courier_capacity >= package_weight:
            if courier_capacity > package_weight:
                courier_capacity -= package_weight * 2
                if courier_capacity > 0:
                    courier_storage.append(courier_capacity)
            total_weight += package_weight
        else:
            left = package_weight - courier_capacity
            total_weight += courier_capacity
            packages_storage.append(left)
    print(f"Total weight: {total_weight} kg")

    if not packages_storage and not courier_storage:
        print(
            "Congratulations, all packages were delivered successfully by the couriers today."
        )
    elif packages_storage and not courier_storage:
        print(
            f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(map(str, packages_storage))}"
        )
    elif courier_storage and not packages_storage:
        print(
            f"Couriers are still on duty: {', '.join(map(str, courier_storage))} but there are no more packages to deliver."
        )


if __name__ == "__main__":
    main()
