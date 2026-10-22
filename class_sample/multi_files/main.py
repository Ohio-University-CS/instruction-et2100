# # a.py

# import file_1
# import file_2

# file_1.say_hello()
# a = file_1.test()
# print (file_1.ll)

# result = file_2.add(file_1.xyz, 20)
# print(result)

# # create 2 files, 
# # where one contain the 
# # student class, with attribute name, age
# # and a function call get_info in the class
# # this function return both name and age

# # another one contain main logic 
# # where you create 2 student with that class
# # and get their info, and print out


import file_1

student_1 = file_1.Student("shawn", 18)
student_2 = file_1.Student("ben", 16)

(name_1, age_1) = student_1.get_info()
(name_2, age_2) = student_2.get_info()

print("Student1: ", name_1, age_1)
print("Student2: ", name_2, age_2)