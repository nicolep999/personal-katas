from collections import deque


def time_controller(hours, minutes, seconds):
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)

    if seconds > 59:
        minutes += seconds // 60
        seconds = seconds % 60
    if minutes > 59:
        hours += minutes // 60
        minutes = minutes % 60
    if hours > 23:
        hours = hours % 24

    return f"{hours:02d}", f"{minutes:02d}", f"{seconds:02d}"


def main():
    robots_input = input().split(";")
    robots_storage = deque()

    for robot_data in robots_input:
        robot, process_time = robot_data.split("-")
        robots_storage.append((robot, int(process_time)))

    hours, minutes, seconds = input().split(":")

    products = deque()
    command = input()

    while command != "End":
        products.append(command)
        command = input()

    busy_robots = {}

    current_time = int(hours) * 3600 + int(minutes) * 60 + int(seconds)

    while products:
        current_time += 1
        hours, minutes, seconds = time_controller(
            current_time // 3600 % 24, current_time // 60 % 60, current_time % 60
        )

        for robot in list(busy_robots):
            busy_robots[robot] -= 1
            if busy_robots[robot] <= 0:
                del busy_robots[robot]

        if robots_storage and products:
            robot_name, process_time = robots_storage[0]

            if robot_name not in busy_robots:
                product = products.popleft()
                busy_robots[robot_name] = process_time
                print(f"{robot_name} - {product} [{hours}:{minutes}:{seconds}]")
            else:
                products.append(products.popleft())

        robots_storage.rotate(-1)


if __name__ == "__main__":
    main()
