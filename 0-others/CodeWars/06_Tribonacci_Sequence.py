# https://www.codewars.com/kata/556deca17c58da83c00002db


def tribonacci(signature, n):
    if n == 0:
        return []
    elif n < 3:
        return signature[0:n]
    while len(signature) < n:
        new_signature = signature[-1] + signature[-2] + signature[-3]
        signature.append(new_signature)
    return signature


print(tribonacci([1, 1, 1], 1))
print(tribonacci([106, 12, 126], 2))
print(tribonacci([106, 12, 126], 1))
