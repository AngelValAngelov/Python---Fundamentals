students = {}
courses = {}

while True:
    raw_data = input().split(" : ")
    if raw_data[0] == "end":
        break
    course = raw_data[0]
    student = raw_data[1]
    # students[course] = student
    if course in courses:
        courses[course] += 1
    else:
        courses[course] = 1
    if course in students:
        students[course] += f",{student}"
    else:
        students[course] = student

for course, participants in sorted(courses.items(), key=lambda x: x[1], reverse=True):
    print(f"{course}: {int(participants)}")
    for i in sorted(students[course].split(',')):
        print(f"-- {i}")