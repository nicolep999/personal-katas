while True:
    string = input()
    if string == "End":
        break
    if string == "SoftUni":
        continue
    doubled_string = ''.join([char * 2 for char in string])
    print(doubled_string)
