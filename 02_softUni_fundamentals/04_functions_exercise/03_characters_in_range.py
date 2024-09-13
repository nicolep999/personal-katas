def characters_in_range(o, n):
    start = ord(o)
    end = ord(n)

    characters = [chr(i) for i in range(start + 1, end)]
    result = " ".join(characters)

    return result


user_char1 = input()
user_char2 = input()

print(characters_in_range(user_char1, user_char2))
