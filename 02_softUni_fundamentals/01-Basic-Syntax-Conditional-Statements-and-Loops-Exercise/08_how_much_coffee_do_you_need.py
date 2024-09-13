coffee_count = 0

while True:
    event = input()
    if event == "END":
        break
    if event.lower() in ["coding", "dog", "cat", "movie"]:
        if event.islower():
            coffee_count += 1
        elif event.isupper():
            coffee_count += 2

if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)
