def average():
    for key, value in better_students.items():
        average_grade = sum(value) / len(value)
        if average_grade >= 4.5:
            print(f"{key} -> {average_grade:.2f}")


better_students = {}
number_of_lines = int(input())
for line in range(number_of_lines):
    student = input()
    grade = float(input())
    if student not in better_students:
        better_students[student] = []
    better_students[student].append(grade)
average()


