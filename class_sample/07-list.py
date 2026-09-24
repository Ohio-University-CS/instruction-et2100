# a = 6
# a = 9
# print(a)
# b = ['hello', 5, 7, [1, 5]]
# print(b)
# print(b[0])
# print(b[2])
# b[2] = 23
# print(b)
# c = []

# for x in range(5): 
#     print(x)
# for x in [0,1,2,3,4]: 
#     print(x)

# for x in [0,"hello",2,56,4]: 
# # create variable x, loop through all value in the list after keyword "in"
#     print(x)

# b = ['hello', 5, 7, [1, 5]]
# print(len(b))


# friends = ['Joseph', 'Glenn', 'Sally']
# print(list(range(len(friends))))
# # print(list(range(3)))
# # print(list([0,1,2]))
# # print([0,1,2])
# # => [0,1,2]


# create a program to going through all value in [3,6,2,7]
# then calculate the sum of them

# new_list = [3, 6, 2, 7]
# sum = 0
# for item in new_list:
#     sum = sum + item

# print(sum)





# a = [3, 4, 5]
# # add value to list
# a.append(7) # [3, 4, 5, 7]
# # insert a value at given location, 1st value is location, 2nd value is value to insert
# a.insert(1, 2) # [3, 2, 4, 5, 7]
# # remove the FIRST matching vlaue in the list
# a.remove(3) # [2, 4, 5, 7]
# # pop remove last index value in the list
# a.pop() # [2, 4, 5]
# # pop(index) remove the value at given index location
# a.pop(1) # [2, 5]
# # remove all value in the list
# a.clear() # []
# print(a)
# xxx.index(value) # find the index of this value in the list

# b = [3, 8, 2, 10, 5, 8]
# # sort all value in increasing order
# b.sort() # [2, 3, 5, 8, 8, 10]
# # sort all value in decreasing order
# b.reverse() # [10, 8, 8, 5, 3, 2]
# # getting length of list
# len(b) # 6
# print(b)
# # getting a sub list within defined range
# print(b[1:3]) # [8, 8]

# # define a empty list
# x = list()
# x = []

# # get max number of list
# max(b)
# # get min num of list
# min(b)
# # add up all number
# sum(b)

# # with string, xx.split() can split string with spaces into list
# # with xx.split('y'), can split string with 'y' into list
# a = 'first;second;third'
# print(a.split(';'))



# #       3.         6.    9. 
# PKG1001 | Columbus | 4.5 | DELIVERED
# xxx.find("|")
# 3,6, 9
# float(xxx[6+1:9])


# id=xxx[:"num of first '|'"]
# line = id + xx + xx
# xxx.write(line)




# friends = ['Joseph', 'Glenn', 'Sally']
# print(list(range(len(friends))))

# len_num = len(friends)
# range_list = range(len_num)
# friend_range_list = list(range_list)
# print(friend_range_list)





# # # use concept of list, think about how you can make the shape below
# # *****
# # *   *
# # *   *
# # *   *
# # *****

# line = []
# for i in range(5):
#     for j in range(5):
#         if (i == 0 or i == 4):
#             line.append("*")
#         else:
#             if (j == 0 or j == 4):
#                 line.append("*")
#             else:
#                 line.append(" ")
#     # print(line)
#     line_str = ""
#     for item in line:
#         line_str = line_str + item
#     print(line_str)
#     line.clear()


# you are asking to design a menu,
# ask user to define what is the name of each item
# and corresponding price to that item
# a menu should have more than 5 items
# once done, calculate what is total price
# if someone order the entire menu
# item_name = ['xx', 'yy', 'zz']
# price = [1.5, 5, 2]

# item = []
# price = []

# count = 1
# ## add a way to allow user to remove a item in the menu, which maens also 
# # include corresponding price

# while True:
#     single_item_name = input("Enter a Item Name: ")
#     single_item_price = input("Enter price for that item: ")
#     item.append(single_item_name)
#     price.append(float(single_item_price))
#     operation = input("Finish(f), remove(r), nothing(n): ")
#     if(operation == "f"):
#         if(count > 5):
#             break
#         else:
#             print("you need to enter more items")
#     elif(operation == "r"):
#         print("Before: ", item, price)
#         remove_item_name = input("Enter item want to remove: ")

#         # xxx.index(value) # find the index of this value in the list
#         index = 0
#         for _item in item:
#             if _item == remove_item_name:
#                 break
#             else:
#                 index = index + 1
#         item.pop(index)
#         price.pop(index)

#         print("After: ", item, price)

#     count = count + 1
# print(item)
# print(price)

# # final_price = 0
# # for single_price in price:
# #     final_price = final_price + single_price
# print("total price of entire menu", sum(price))


# a = [1,2,3,4]
# b = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# b = [[1,2,3], [4,5,6], [7,8,9]]

table = []
for i in range(5):
    row = []
    for j in range(5):
        if (i == 0 or i == 4):
            row.append("*")
        else:
            if (j == 0 or j == 4):
                row.append("*")
            else:
                row.append(" ")
        # row.append(j)
    table.append(row)

print(table)

# *****
# *   *
# *   *
# *   *
# *****


# table = []
# for i in range(5):
#     row = []
#     for j in range(5):
#         row.append("*")
#     table.append(row)

# print(table)