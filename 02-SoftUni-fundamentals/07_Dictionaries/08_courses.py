def main():
    database = {}

    while True:

        user_input = input()

        if user_input == "end":

            for entry in database:
                print(f"{entry}: {len(database[entry])}")
                for person in database[entry]:
                    print(f"-- {person}")
            break
        course, student = user_input.split(" : ")

        if course in database:
            database[course].append(student)
        else:
            database[course] = [student]


main()
