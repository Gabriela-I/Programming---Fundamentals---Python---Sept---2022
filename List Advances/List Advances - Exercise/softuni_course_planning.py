def add(all_lessons, some_lesson):
    all_lessons.append(some_lesson)
    return all_lessons


def insert(all_lessons, some_lesson, place):
    all_lessons.insert(place, some_lesson)
    return all_lessons


def remove(all_lessons, some_lesson):
    some_lesson_index = all_lessons.index(some_lesson)
    if some_lesson_index + 1 in range(len(all_lessons)):
        if 'Exercise' in all_lessons[some_lesson_index + 1]:
            all_lessons.pop(some_lesson_index + 1)
    all_lessons.remove(some_lesson)
    return all_lessons


def swap(all_lessons, some_lesson, lesson_two):
    some_lesson_index = all_lessons.index(some_lesson)
    lesson_two_index = all_lessons.index(lesson_two)
    first_has_exercise = False
    second_has_exercise = False
    if some_lesson_index + 1 in range(len(all_lessons)):
        first_has_exercise = 'Exercise' in all_lessons[some_lesson_index + 1]
    if lesson_two_index + 1 in range(len(all_lessons)):
        second_has_exercise = 'Exercise' in all_lessons[lesson_two_index + 1]
    all_lessons[some_lesson_index], all_lessons[lesson_two_index] = \
        all_lessons[lesson_two_index], all_lessons[some_lesson_index]
    if first_has_exercise and second_has_exercise:
        all_lessons[some_lesson_index + 1], all_lessons[lesson_two_index + 1] = \
            all_lessons[lesson_two_index + 1], all_lessons[some_lesson_index + 1]
    elif not first_has_exercise and second_has_exercise:
        all_lessons.insert(some_lesson_index + 1, all_lessons.pop(lesson_two_index + 1))
    elif first_has_exercise and not second_has_exercise:
        all_lessons.insert(lesson_two_index + 1, all_lessons.pop(some_lesson_index + 1))
    return all_lessons


def exercise(all_lessons, some_lesson):
    if some_lesson in all_lessons and f'{some_lesson}-Exercise' not in all_lessons:
        some_lesson_index = all_lessons.index(some_lesson)
        all_lessons.insert(some_lesson_index + 1, f'{some_lesson}-Exercise')
    elif some_lesson not in all_lessons:
        all_lessons.append(some_lesson)
        all_lessons.append(f'{some_lesson}-Exercise')
    return all_lessons


lessons = input().split(', ')
while True:
    command = input()
    if command == 'course start':
        break
    action = command.split(':')[0]
    first_lesson = command.split(':')[1]
    if action == 'Add':
        if first_lesson not in lessons:
            lessons = add(lessons, first_lesson)
    elif action == 'Insert':
        if first_lesson not in lessons:
            index = int(command.split(':')[2])
            lessons = insert(lessons, first_lesson, index)
    elif action == 'Remove':
        if first_lesson in lessons:
            lessons = remove(lessons, first_lesson)
    elif action == 'Swap':
        second_lesson = command.split(':')[2]
        if first_lesson in lessons and second_lesson in lessons:
            lessons = swap(lessons, first_lesson, second_lesson)
    elif action == 'Exercise':
        lessons = exercise(lessons, first_lesson)
for i, element in enumerate(lessons):
    print(f'{i + 1}.{element}')
