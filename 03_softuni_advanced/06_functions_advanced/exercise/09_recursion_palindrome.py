def palindrome(w, i):
    if i == len(w) // 2:
        return f"{w} is a palindrome"
    if w[i] != w[-i - 1]:
        return f"{w} is not a palindrome"
    return palindrome(w, i + 1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
