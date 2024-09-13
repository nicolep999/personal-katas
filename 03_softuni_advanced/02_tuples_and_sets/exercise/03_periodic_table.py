# n = int(input())
#
# storage = set()
#
# for _ in range(n):
#     command = input().split()
#     for el in command:
#         storage.add(el)
#
# print(*storage, sep="\n")
# # print("\n".join(storage))

print(*{el for _ in input().split() for el in input().split()}, sep="\n")
