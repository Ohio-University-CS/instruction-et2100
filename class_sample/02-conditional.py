# x = 5
# if x < 10:
#     print('Smaller')
#     x = 4
# x = 27
# if x > 20:
#     print('Bigger')
#     if x < 30:
#         print("hello")
#         x = 7
#     x = 3
# x = x +2
# print('Finis')
# print(x)


# x = 1
# if x > 2 :
#     print('Bigger')
# else :
#     print('Smaller')
# print('All done')



# # x = 1

# # if x < 2 :
# #     print('small')
# # elif x < 10 :
# #     print('Medium')
# # else :
# #     print('LARGE')


# # if x < 2 :
# #     print('small')
# # if x < 10 :
# #     print('Medium')
# # else :
# #     print('LARGE')

# x = 12
# if x > 2 :
#     print('small')
# if x < 10 : 
#     print('Medium')
# else :
#     print('LARGE')

# #if elif, else

# #if, elif, if, else

# print('All done')

# x = 1
# if x < 2 :
#  print('Below 2')
# elif x < 20 :
#  print('Below 20')
# elif x < 10 :
#  print('Below 10')
# else :
#  print('Something else')

# input()
# write a program that ask user for a number,
# then base on that number, print out if it is smaller or bigger than 10
# if it equal to 10, then print result of that value + 10 
# num = input("Enter a number: ")
# if(int(num) < 10):
#     print("Small")
# elif(int(num) > 10):
#     print("Big")
# else:
#     print(int(num) + 10)

# num_raw = input("Enter a number: ")
# num = int(num_raw)
# if(num < 10):
#     print("Small")
# elif(num > 10):
#     print("Big")
# else:
#     print(num + 10)

# num = int(input("Enter a number: "))

# if(num < 10):
#     print("Small")
# elif(num > 10):
#     print("Big")
# else:
#     print(num + 10)


# num = int(input("Enter a number: "))
# try:
#     if(num < 10):
#         print("Small")
#     elif(num > 10):
#         print("Big")
#     else:
#         print(num + 10)
# except:
#     print("Please check your input")



# try:
#     num = int(input("Enter a number: "))
# except:
#     print("Please check your input")
# try:
#     if(num < 10):
#         print("Small")
#     elif(num > 10):
#         print("Big")
#     else:
#         print(num + 10)
# except:
#     print("Please check your input")


# try:
#     num = int(input("Enter a number: "))
# except:
#     num = -1

# if(num == -1):
#     print("Something goes wrong with your input")
# elif(num < 10):
#     print("Small")
# elif(num > 10):
#     print("Big")
# else:
#     print(num + 10)


num = int(input("Enter a number: "))

# 0 < num < 10
# if (num > 0):
#     if(num <10):
#         print(num)

if (num > 0 and num <10):
    print("1: ", num)

if (num > 0 or num <10):
    print("2: ", num)