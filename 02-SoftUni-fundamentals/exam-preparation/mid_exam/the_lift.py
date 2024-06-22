def main():
    queue_length = int(input())
    wagons = list(map(int, input().split(" ")))
    for index in range(len(wagons)):
        while True:
            if wagons[index] == 4 or queue_length <= 0:
                break
            wagons[index] += 1
            queue_length -= 1

    if wagons[-1] == 4 and queue_length <= 0:
        print(f"{' '.join(map(str, wagons))}")
        return
    if queue_length <= 0:
        print(f"The lift has empty spots!\n{' '.join(map(str, wagons))}")
        return
    if wagons[-1] == 4 and queue_length > 0:
        print(
            f"There isn't enough space! {queue_length} people in a queue!\n{' '.join(map(str, wagons))}"
        )
        return


if __name__ == "__main__":
    main()
