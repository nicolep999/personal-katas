from collections import deque


def main():

    robots_data = input().split(";")
    current_time = list(map(int, input().split(":")))

    robots_workload = {}
    for x in robots_data:
        robots_workload[x] = 0
    print(robots_workload)


    command = input()

    products_storage = deque()

    while command != "End":
        products_storage.appendleft(command)

    print(products_storage)


if __name__ == "__main__":
    main()
