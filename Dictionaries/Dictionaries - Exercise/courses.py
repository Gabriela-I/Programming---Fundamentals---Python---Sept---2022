all_courses = {}
while True:
    info = input().split(' : ')
    course = info[0]
    if course == 'end':
        break
    name = info[1]
    if course not in all_courses:
        all_courses[course] = []
    all_courses[course].append(name)

for key, value in all_courses.items():
    print(f"{key}: {len(value)}")
    for student in value:
        print(f"-- {student}")

