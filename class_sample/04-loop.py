# Ctrl + C to stop the program

# n = 5
# # while True:
# # while False:
# while n > 0 :
#     n = n + 1
#     print('Lather')
#     print('Rinse')

# print('Dry off!')

# while True:
#     line = input('> ')
#     if line == 'done' :
#         break
#     print(line)
# print('Done!')

# n = 6
# while n > 0:
#     line = input('> ')
#     if line[0] == '#' :
#         continue
#     if line == 'done' :
#         break
#     n = n -1
#     print(n)
#     print(line)
# print('Done!')

# create a calculator program for + and - operation
# ask user for 2 numbers and the type of operation
# the program will only able to run for 5 times, after that it will stop
# and it will also stop if the calculation result is 111


# count = 0
# while count < 5:
#     num_1 = input("Enter first number: ")
#     num_2 = input("Enter second number: ")
#     operation = input("Enter the type of operation (+ or -): ")

#     if operation == "+":
#         result = int(num_1) + int(num_2)
#     elif operation == "-":
#         result = int(num_1) - int(num_2)
#     print("The result is:", result)
#     if result == 111:
#         print("The result is 111, stopping the program.")
#         break

#     count = count + 1

# print("Program finished.")

# # i = 0
# # while i < 5:
# #     i = i + 1
# for i in range(5):
# # range(5) => [0,1,2,3,4]
#     print(i)
#     print("Welcome to Python!")

# for i in range(2, 5): # [2,3,4]
#     print(i)
#     print("Welcome to Python!")

# for i in range(2, 10, 3): # [2, 5, 8]
#     print(i)
#     print("Welcome to Python!")

# for i in range(10, 2, -3): # [10, 7, 4]
#     print(i)
#     print("Welcome to Python!")


# for i in range(11, 1, -1):
#     print(i)

# for i in range(1, 7):
#     for j in range(1, 7):
#         print(i, j)

# for i in range(1, 11):
#     inner_loop_function()







# line = ""
# ""
# "" + "11" => "11"
# "11" + "," + "12" => "11,12"

# # 11,12,13,14,15,16,
# # 21,22,23,24,25,26,
# # 31,32,33,34,35,36,
# # 41,42,43,44,45,46,
# # 51,52,53,54,55,56,
# # 61,62,63,64,65,66,
# line = ""
# for i in range(1, 7):
#     for j in range(1, 7):
#         line = line + str(i) + str(j) + ","

#     print(line)
#     line = ""



# # 11          
# #   22        
# #     33      
# #       44    
# #         55  
# #           66

# line = ""
# for i in range(1, 7):
#     for j in range(1, 7):
#         if (i == j):
#             # add the number
#             line = line + str(i) + str(j)
#         else:
#             # add space
#             line = line + "  "

#     print(line)
#     line = ""



int / float
string

line = ""
for i in range(1, 7):
    for j in range(1, 7):
        # if i is 1st row or 6th row
        # we print entire thing of j
        if (i == 1 or i == 6):
            line = line + str(i) + str(j) + " "
        # if i is not,
        # print 1st and 6th of j    
        else:
            if (j == 1 or j == 6):
                line = line + str(i) + str(j) + " "
            else:
                line = line + "   "

    print(line)
    line = ""