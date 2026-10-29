import json

students = [
    {"name": "Alice", "grade": 93},
    {"name": "Bob", "grade": 87}
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)



# # # import json

# # # with open("students.json", "r") as file:
# # #     students = json.load(file)

# # # for student in students:
# # #     print(student["name"], student["grade"])


# # # import json
# # # with open("students.json", "r") as file:
# # #     students = json.load(file)

# # # # students[0]["grade"] = 95
# # # # print(students)

# # # # with open("students.json", "w") as file:
# # # #     json.dump(students, file, indent=4)

# # # for student in students:
# # #     if student["grade"] >= 90:
# # #         print(student)


# # ## you are ask to create a food menu system 
# # # where you ask user to input the food name and price
# # # then store it into a json file
# # # after store couple of food, you gonna ask to 
# # # update all the food price >= 15 become whatever their price * 0.9

# # import json

# # food_menu = []

# # while True:
# #     food_name = input("Enter food name (type exit to finish): ")
# #     if (food_name == "exit"):
# #         break
# #     price = input("Enter food price: ")
# #     food_menu.append({"name": food_name, "price": float(price)})
# #     print(food_menu)

# # with open("menu.json", "w") as file:
# #     json.dump(food_menu, file, indent=4)

# # tmp = input("hi")

# # with open("menu.json", "r") as file:
# #     food_menu_final = json.load(file)

# # for food in food_menu_final:
# #     if food["price"] >= 15:
# #         food["price"] = food["price"] * 0.9

# # with open("menu.json", "w") as file:
# #     json.dump(food_menu_final, file, indent=4)



# from tinydb import TinyDB

# db = TinyDB("students.json")

# db.insert({
#     "name": "Alice",
#     "major": "CS",
#     "grade": 93
# })

# db.insert({
#     "name": "Bob",
#     "major": "CS",
#     "grade": 12
# })

# print(db.all())
