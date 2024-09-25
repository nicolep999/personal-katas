n = int(input())

odd_list = []
even_list = []

for i in range(1, n + 1):
    name = input()

    if name.strip() == "":
        continue

    ascii_sum = sum(ord(char) for char in name)
    final_value = ascii_sum // i

    if final_value % 2 == 0:
        even_list.append(final_value)
    else:
        odd_list.append(final_value)

sum_odd = sum(odd_list)
sum_even = sum(even_list)

if sum_odd == sum_even:
    result_list = list(set(odd_list).union(even_list))
    print(", ".join(map(str, result_list)))
elif sum_odd > sum_even:
    result_list = list(set(odd_list).difference(even_list))
    print(", ".join(map(str, reversed(result_list))))
else:
    result_list = list(set(even_list).symmetric_difference(odd_list))
    print(", ".join(map(str, result_list)))
