# a = "hello there"
# b = "hello \nthere"
# c = "hello \nthere\n"
# print(a)
# print(len(a))
# print("---")
# print(b)
# print(len(b))
# print("---")
# print(c)   
# print(len(c))
# print("---") 


# xfile = open('class_sample/06-file.txt') # relative path, showing how to open a file from where you running it
# # xfile = open('/Users/cricel/Documents/GitHub/instruction-et2100/class_sample/06-file.txt') #absolute path, showing how to open a file no matter where you are running it
# count = 0
# for cheese in xfile:
#     count = count + 1
#     # print(cheese)                # wefwef\n
#     print(cheese.rstrip())       # wefwef
#     # print(type(cheese))

# print("Line Count:", count)




# xfile = open('class_sample/06-file.txt')
# inp = xfile.read()
# print(inp)
# print(inp[:20])


# xfile = open('class_sample/06-file.txt')
# for line in xfile:
#     line = line.rstrip()
#     if line.startswith('w'):
#         print(line)



# manually create a txt file store all the text
# then using python to load it into program
# then replace the first and thrid space with "_"
# then replace the fifth line with "hello there"
# then merge every 2 line into 1 line
# and print out

# rfile = open('class_sample/06-file.txt', 'r')
# count = 1
# prev_line = ""
# for line in rfile:
#     line = line.rstrip()
#     line = line.replace(" ", "_", 2)
#     if count == 5:
#         line = "hello there"

#     if count % 2 == 1:
#         prev_line = line
#     else:
#         line = prev_line + " " + line
#         print(line)

#     count = count + 1


#     # print(line)


# xfile = open('class_sample/06-file.txt', 'r')

# inp = xfile.read()
# print(inp)

# xfile.close()  # close the file after reading it

#### Write files
# xfile = open('class_sample/06-file_1w.txt', 'w')

# xfile.write("Hello, World!")

# xfile.close()  # close the file after reading it




rfile = open('class_sample/06-file.txt', 'r')
wfile = open('class_sample/06-file_new.txt', 'w')
count = 1
prev_line = ""
for line in rfile:
    line = line.rstrip()
    line = line.replace(" ", "_", 2)
    if count == 5:
        line = "hello there"

    if count % 2 == 1:
        prev_line = line
    else:
        line = prev_line + " " + line
        wfile.write(line + "\n")  # write the merged line to the new file
        print(line)

    count = count + 1


rfile.close()  # close the input file after reading it
wfile.close()  # close the output file after writing to it