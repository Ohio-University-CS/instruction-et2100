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

for i in range(10, 2, -3): # [10, 7, 4]
    print(i)
    print("Welcome to Python!")







# for i in range(11, 1, -1):
#     print(i)