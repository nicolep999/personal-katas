# O(2^n) Recursive solution:

# n = int(input())
# vector = [0] * n


# def generate(idx, vector):
#     if idx == n:
#         print(*vector, sep="")
#         return
#     vector[idx] = 0
#     generate(idx + 1, vector)
#     vector[idx] = 1
#     generate(idx + 1, vector)


# generate(0, vector)


# O(n) Solution:
n = int(input())
for i in range(2**n):
    vector = [int(x) for x in bin(i)[2:].zfill(n)]
    print(*vector, sep="")
