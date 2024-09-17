n = int(input(""))


matrix = [[int(j) for j in input().split(", ") if int(j) % 2 == 0] for i in range(n)]


print(matrix)


"""
2
1, 2, 3
4, 5, 6
"""

# matrix = []
#
# for i in range(n):
#     data_row = [int(n) for n in input().split(", ") if int(n) % 2 == 0]
#     matrix.append(data_row)
