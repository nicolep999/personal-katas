n = int(input())

matrix = [[int(j) for j in input().split(", ")] for i in range(n)]
flattened = [num for sublist in matrix for num in sublist]

print(flattened)

"""
2
1, 2, 3
4, 5, 6
"""
