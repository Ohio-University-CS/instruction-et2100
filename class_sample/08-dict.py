# price = dict()
# price['apple'] = 3
# price['banna'] = 4
# price['aa'] = 6
# price['bb'] = 1

# price['apple'] = 7

# print(price)

# price_list = list()
# fruits = list()

# price_list.append(3)
# price_list.append(4)
# price_list.append(6)
# price_list.append(1)

# fruits.append('apple')
# fruits.append('banna')
# fruits.append('aa')
# fruits.append('bb')

# print(fruits, price_list)
# print(fruits[0],price_list[0])



# price_1 = dict()
# price_2 = {}
# price_3 = {'apple': 3, 'aa': 5}
# price_list_1 = list()
# price_list_2 = []
# price_list_3 = [3, 5]



# price_3 = {'apple': 3, 'aa': 5}
# # print(price_3['cc'])
# print(price_3.get('cc', -1))
# print(price_3.get('apple', -1))
# # try, except


# # given text 
# # aa bb cc aa bb dd aa
# # use dict to count how many time each duplicate value show up in the text
# # xxx.split() => [x,x,x,x]
# text = 'aa bb cc aa bb dd aa '
# text_list = text.split()
# text_dict = dict()
# print(text_list)
# for word in text_list:
#     text_dict[word] = text_dict.get(word, 0) + 1

# print(text_dict)



# price_3 = {'apple': 3, 'aa': 5, 'bb': 7, 'cc': 2}
# for item in price_3:
#     print(item, price_3[item])


# jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
# print(list(jjj))
# print(list(jjj.keys()))
# print(jjj.keys())
# print(list(jjj.values()))
# print(jjj.values())
# print(list(jjj.items()))
# print(jjj.items())

# for value in jjj.values():
#     print(value)
# for value in jjj.keys():
#     print(value)
# for value in jjj.items():
#     print(value)

# for key, value in jjj.items():
#     print(key, value)

# create a program to ask TA to enter grade for student
# after log some student, the TA is asking to update one of the student's grade
# (for example: shawn, update grade to 90)
# but when typing, TA found out shawn did not exist, it is sean that need to update
# show the error catching in your program

student = dict()
while(True):
    print("Menu")
    print("1. Add grade")
    print("2. Update grade")
    print("3. Done")
    input_menu = input("Enter a option: ")
    if(int(input_menu) == 1):
        input_name = input("Enter Student Name: ")
        input_grade = int(input("Enter Student Grade"))
        student[input_name] = input_grade

        print(student)
    elif(int(input_menu) == 2):
        input_update_name = input("Enter Student Name: ")
        student_grade = int(student.get(input_update_name, -1))
        if (student_grade == -1):
            print("The student did not exist")
        else:
            print("The current grade for this student is: ", student_grade)
            input_update_grade = int(input("Enter New Student Grade: "))
            student[input_update_name] = input_update_grade

        print(student)
    else:
        break
