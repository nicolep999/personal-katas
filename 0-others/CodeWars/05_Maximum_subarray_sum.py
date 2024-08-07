# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c
def max_sequence(arr):
    current_sum = ""
    arr = set(arr)
    arr = sorted(arr, reverse=True)
    current_sum = 0
    for x in arr:
        print(x)
        if current_sum + x > current_sum:
            current_sum += x
        else:
            break
    print(current_sum)
    print(arr)


max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
