user_input = input()
final_result = ""
current_strength = 0

for i in range(len(user_input)):
    if user_input[i] == ">":
        current_strength += int(user_input[i + 1])
        final_result += user_input[i]
    elif user_input[i] != ">" and current_strength > 0:
        current_strength -= 1
    else:
        final_result += user_input[i]

print(final_result)
