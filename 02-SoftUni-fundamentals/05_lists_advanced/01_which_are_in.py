def main():
    substring_string = list(map(str, input().split(", ")))
    user_string = list(map(str, input().split(", ")))

    result = []

    for substring in substring_string:
        for string in user_string:
            if substring in string:
                result.append(substring)
                break
    print(result)


main()
