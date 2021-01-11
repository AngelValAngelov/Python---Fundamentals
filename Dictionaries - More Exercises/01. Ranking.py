from collections import OrderedDict

courses = input().split(":")

dictionary_courses = {}

while courses != "end of contests":
    name_course = courses[0]
    password_course = courses[1]
    dictionary_courses[name_course] = password_course

    courses = input()
    if courses == "end of contests":
        break
    else:
        courses = courses.split(":")

participant_points = input().split("=>")

partisipant_dict = {}
final_dict = {}

while participant_points[0] != "end of submissions":
    course = participant_points[0]
    password = participant_points[1]
    name_participant = participant_points[2]
    points_participant = participant_points[3]
    if course in dictionary_courses.keys() and password == dictionary_courses[course]:
        if name_participant in partisipant_dict.keys():
            if course in final_dict.keys() and final_dict[course] < points_participant:
                final_dict[course] = points_participant
            elif course not in final_dict.keys():
                final_dict[course] = points_participant
        else:
            final_dict[course] = points_participant
            print(final_dict)
            partisipant_dict[name_participant] = final_dict
            print(partisipant_dict)

    participant_points = input()
    if participant_points == "end of submissions":
        break
    else:
        participant_points = participant_points.split("=>")

print(partisipant_dict)
for key in partisipant_dict:
    print(key)
for key, value in partisipant_dict.items():
    print(key, value)
    for key, value in value.items():
        pass
















































