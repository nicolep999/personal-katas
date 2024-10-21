def main():
    user_input = list(map(str, input().split()))
    output_list = [x for x in user_input if len(x) % 2 == 0]
    for x in output_list:
        print(x)


main()
