def main():

    iterations = int(input())

    grades_database = {}

    for _ in range(iterations):

        student = input()
        grade = float(input())

        if student in grades_database:
            grades_database[student].append(grade)
        else:
            grades_database[student] = [grade]

    for entry in grades_database:
        average = sum(grades_database[entry]) / len(grades_database[entry])

        if average >= 4.5:
            print(f"{entry} -> {average:.2f}")


main()
