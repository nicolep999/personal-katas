sequence = input()

matches = {")": "(", "}": "{", "]": "["}
stack = []

is_stack = True

for char in sequence:
    if char in matches.values():
        stack.append(char)
    elif char in matches:
        if stack and stack[-1] == matches[char]:
            stack.pop()
        else:
            is_stack = False

if not is_stack:
    print("NO")
else:
    print("YES")
