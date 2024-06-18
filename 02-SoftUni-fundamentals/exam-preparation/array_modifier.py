def main():
    array = list(map(int, input().split(" ")))
    while True:
        command_input = list(map(str, input().split(" ")))
        command = command_input[0]
        if command == "end":
            break
        if command == "swap":
            index1 = int(command_input[1])
            index2 = int(command_input[2])
            array[index1], array[index2] = array[index2], array[index1]
        if command == "multiply":
            index1 = int(command_input[1])
            index2 = int(command_input[2])
            array[index1] *= array[index2]
        if command == "decrease":
            for index in range(len(array)):
                array[index] -= 1
    print(f"{', '.join(map(str, array))}")
    return


main()

"""
23 -2 321 87 42 90 -123
swap 1 3
swap 3 6
swap 1 0
multiply 1 2
multiply 2 1
decrease
end
"""
