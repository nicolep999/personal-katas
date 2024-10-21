from collections import deque


def time_controller(hours, minutes, seconds):

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
    robots = []
    for robot_data in robots_input:
        robot, process_time = robot_data.split("-")
        robots.append([robot, int(process_time), 0])

    hours, minutes, seconds = map(int, input().split(":"))

    products = deque()
    command = input()

    while command != "End":
        products.append(command)
        command = input()

    current_time = hours * 3600 + minutes * 60 + seconds

    while products:
        current_time += 1
        hours, minutes, seconds = time_controller(
            current_time // 3600 % 24, current_time // 60 % 60, current_time % 60
        )

        product = products.popleft()

        assigned = False
        for robot in robots:
            if robot[2] <= current_time:
                robot[2] = current_time + robot[1]
                print(f"{robot[0]} - {product} [{hours}:{minutes}:{seconds}]")
                assigned = True
                break

        if not assigned:
            products.append(product)


main()
