# x = 5
# print('Hello')
# def print_lyrics():
#     print("I'm a lumberjack, and I'm okay.")
#     print('I sleep all night and I work all day.')

# print('Yo')
# x = x + 2
# print_lyrics()

# x = 3
# print(x)
# print("-------")
# print("--- line split ----")
# print("-------")
# x = 5
# print(x)
# print("-------")
# print("--- line split ----")
# print("-------")
# x = 6
# print(x)
# print("-------")
# print("--- line split ----")
# print("-------")
# x = 9
# print(x)
# print("-------")
# print("--- line split ----")
# print("-------")

# def print_line():
#     print("-------")
#     print("--- line split ----")
#     print("-------")

# x = 3
# print(x)
# print_line()
# x = 5
# print(x)
# print_line()
# x = 6
# print(x)
# print_line()
# x = 9
# print(x)
# print_line()


# def print_line(x):
#     print(x)
#     print("-------")
#     print("--- line split ----")
#     print("-------")

# x = 3
# print_line(x)
# x = 5
# print_line(x)
# x = 6
# print_line(x)
# x = 9
# print_line(x)


# write a program to ask user to enter some number,
#  and base on the value of number, print its value + 10
# using function

# num = int(input("Enter a number: "))
# print(num + 10)

# def add_ten(num):
#     print(num + 10)

# num = int(input("Enter a number: "))
# add_ten(num)


# def print_value(x):
#     x = x + 10 # this x has nothing to do with the x outside
#     print(x) 

# x = 10
# y = 8

# print_value(y) # same as print_value(8)
# print_value(x) # same as print_value(10)
# print(x)
# print(y)




# def cal(x):
#     return x + 10

# x = cal(9)
# print(x)


# create a calculator program that ask user for 2 thing:
# 1, type of operation: + -, 2 value that use for calculation
# calculate the result base on input
# using function, also using return

# def plus_func(a, b):
#     return a + b

# def minus_func(a, b):
#     return a - b

# operation = input("Enter the type of operation (+ or -): ")
# first_num = int(input("Enter the first number: "))
# second_num = int(input("Enter the second number: "))
# # how to pack below if elif else part of code also into a function?
# result = -1
# if operation == "+":
#     result = plus_func(first_num, second_num)
# elif operation == "-":
#     result = minus_func(first_num, second_num)
# else:
#     print("Invalid operation")

# print(result)




# def plus_func(a, b):
#     return a + b

# def minus_func(a, b):
#     return a - b

# def condition_checking(_operation, _first_num, _second_num):
#     result = -1
#     if _operation == "+":
#         result = plus_func(_first_num, _second_num)
#     elif _operation == "-":
#         result = minus_func(_first_num, _second_num)
#     else:
#         print("Invalid operation")

#     print(result)


# operation = input("Enter the type of operation (+ or -): ")
# first_num = int(input("Enter the first number: "))
# second_num = int(input("Enter the second number: "))

# condition_checking(operation, first_num, second_num)



# def test_two_out(a,b):
#     return a + 10, b - 9

# x, y = test_two_out(10, 20)

# print(x, y)

# a = 1
# b = 2
# def test_two_out(a,b):
#     a = a + 1
#     b = b + 1
#     return a, b

# def test_two_out_1(_a,_b):
#     a = _a + 1
#     b = _b + 1

# x, y = test_two_out(3, 4)
# print(x, y)
# x, y = test_two_out_1(3, 4) # None
# print(x, y)
# print(a, b)




def test(_a):
    # global c. # With global, c will be treated as a global variable, and the function will modify the global c instead of creating a new local variable.
    a = _a + 1
    c = a
    return a

c = 4
b = test(6)
print(b, c)