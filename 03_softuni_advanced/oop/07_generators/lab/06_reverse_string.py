def reverse_text(step: str):
    current_index = len(step) - 1
    while current_index >= 0:
        yield step[current_index]
        current_index -= 1


for char in reverse_text("step"):
    print(char, end="")
