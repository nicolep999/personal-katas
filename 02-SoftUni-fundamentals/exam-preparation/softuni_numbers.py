def main():
    numbers_list = list(map(int, input().split(" ")))
    numbers_list.sort(reverse=True)
    average_number = float(sum(numbers_list) / len(numbers_list))
    top5 = []
    for number in numbers_list:
        if number > average_number:
            top5.append(number)
            if len(top5) >= 5:
                break
    if not top5:
        print("No")
    print(f"{' '.join(map(str, top5))}")


if __name__ == "__main__":
    main()
