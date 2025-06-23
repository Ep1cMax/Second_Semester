def select_lessons(timetable):
    timetable.sort(key=lambda x: (x[1], x[0]))

    result = []
    last_end = 0.0

    for start, end in timetable:
        if start >= last_end:
            result.append((start, end))
            last_end = end

    return result

print("Input number of lessons: ", end='')
lesson_count = int(input())
lessons = []

for i in range(lesson_count):
    print(f"Input start/end time for lesson {i + 1}: ", end='')
    start, end = map(float, input().split())
    lessons.append((start, end))

selected = select_lessons(lessons)

print(f"\n{len(selected)}")
for lesson in selected:
    print(f"{lesson[0]} {lesson[1]}")

'''
5
9 10
9.3 10.3
10 11
10.3 11.3
11 12
'''