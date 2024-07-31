def main():
    database = {}

    while True:

        user_input = input()

        if user_input == "End":

            for entry in database:
                print(f"{entry}")
                for person in database[entry]:
                    print(f"-- {person}")
            break
        company, employee = user_input.split(" -> ")

        if company in database:
            if employee in database[company]:
                continue
            database[company].append(employee)
        else:
            database[company] = [employee]


main()
