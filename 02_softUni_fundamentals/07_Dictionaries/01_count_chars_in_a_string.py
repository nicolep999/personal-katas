def main():
    user_input = list(map(str, input().split()))
    user_dict = {}

    for word in user_input:
        for char in word:
            if char in user_dict:
                user_dict[char] += 1
            else:
                user_dict[char] = 1
    for x in user_dict:
        print(f"{x} -> {user_dict[x]}")


main()
