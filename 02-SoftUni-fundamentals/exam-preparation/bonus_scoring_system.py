import math

total_students = int(input())
total_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
most_lectures = 00

for _ in range(total_students):
    current_student_lectures = int(input())
    temp_bonus = current_student_lectures / total_lectures * (5 + additional_bonus)

    if temp_bonus > max_bonus:
        most_lectures = current_student_lectures
        max_bonus = temp_bonus

print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {most_lectures} lectures.")
