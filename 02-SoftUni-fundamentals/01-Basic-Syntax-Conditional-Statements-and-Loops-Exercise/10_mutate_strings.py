first_string = input()
second_string = input()

current_string = list(first_string)

for i in range(len(first_string)):
    if current_string[i] != second_string[i]:
        current_string[i] = second_string[i]
        transformed_string = ''.join(current_string)
        print(transformed_string)
