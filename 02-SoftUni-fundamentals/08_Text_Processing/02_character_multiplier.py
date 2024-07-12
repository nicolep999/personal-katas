def main():
    user_input = list(map(str, input().split()))

    total_sum = 0

    str1 = user_input[0]
    str2 = user_input[1]

    if len(str1) > len(str2):
        for index in range(len(str1)):
            if index > len(str2) - 1:
                total_sum += ord(str1[index])
            else:
                total_sum += ord(str1[index]) * ord(str2[index])
    elif len(str2) > len(str1):
        for index in range(len(str2)):
            if index > len(str1) - 1:
                total_sum += ord(str2[index])
            else:
                total_sum += ord(str2[index]) * ord(str1[index])
    else:
        for index in range(len(str1)):
            total_sum += ord(str1[index]) * ord(str2[index])

    print(total_sum)


main()
