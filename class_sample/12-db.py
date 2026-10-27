# import json

# students = [
#     {"name": "Alice", "grade": 93},
#     {"name": "Bob", "grade": 87}
# ]

# with open("students.json", "w") as file:
#     json.dump(students, file, indent=4)



# import json

# with open("students.json", "r") as file:
#     students = json.load(file)

# for student in students:
#     print(student["name"], student["grade"])


import json
with open("students.json", "r") as file:
    students = json.load(file)

# students[0]["grade"] = 95
# print(students)

# with open("students.json", "w") as file:
#     json.dump(students, file, indent=4)

for student in students:
    if student["grade"] >= 90:
        print(student)

