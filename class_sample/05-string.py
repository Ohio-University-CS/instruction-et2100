# char  (letter)

# # create a program loop through all letters and 
# # print out all letter in "hello"
# # len(xxx) get length
# # xxx[x] get the character at index x
# text = "hello"
# print(len(text))
# for i in range(len(text)):
#     print(text[i])



# for x in range() # range(5) => [0,1,2,3,4]

# fruit = 'banana'
# for letter in fruit:
#     print(letter)


# a = "hello world"
# print(a[0:5])
# print(a[0:-3])
# print(a[-1])



# a = "hello world"
# if "e" in a:
#     print("yes")
# if "ello" in a:
#     print("yes")
# if "x" not in a:
#     print("no")


# lower letter > upper letter > number > special character
# "abc" and "acf" and "baf" when compare string, you compare the first letter, 
# if they are the same, then compare the second letter, if they are the same, 
# then compare the third letter, and so on. If one string is shorter than the other, 
# the shorter string is considered smaller. "abc" < "abcd" because "abc" is shorter than "abcd".
# "abrdfdf" < "adc"

# write a program to ask user to enter a string, then find out how many space is in the text
# (try to have more than 2 sapce in your input)
# then replace the space with "_"
# and change all leter after first "_" to all upper and before first "_" to all lower

# xxx.find('xx') find the index of the first occurrence of 'xx' in xxx, if not found, return -1
# xxx.find('xx', start_index) find the index of the first occurrence of 'xx' in xxx starting from start_index, if not found, return -1
# xxx.replace('xx', 'yy') replace all occurrences of 'xx' in xxx with 'yy'
# xxx.upper() convert all letters in xxx to upper case
# xxx.lower() convert all letters in xxx to lower case
# len(xxx) get length
# xxx[x] get the character at index x
# xxx[x:y] get the substring from index x to index y (not including y)

user_input = input("Enter a string: ")
updated_input = user_input.replace(" ", "_")
first_underscore_index = updated_input.find("_")
left_part = updated_input[:first_underscore_index].lower()
right_part = updated_input[first_underscore_index + 1:].upper()
final_result = left_part + "_" + right_part
print("Final result:", final_result)