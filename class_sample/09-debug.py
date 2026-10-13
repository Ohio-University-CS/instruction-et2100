# def get_grade(score):
#     if score >= 90:
#         return "A"
#     elif score >= 80
#         return "B"
#     elif score >= 70:
#         return "C"
#     else:
#         return "F"


# scores = [95, 82, 76, 91]

# for score in scores:
# print(score, get_grade(score))




####################



# scores = [95, 82, 76, 91, 68]

# total = 0
# passed = 0
# highest = 0
# lowest = 0

# for score in scores:
#     total += score

#     if score >= 70:
#         passed += 1

#     if score > highest:
#         highest = score

#     if score < lowest:
#         lowest = score

# average = total / (len(scores) - 1)

# print("Average:", average)
# print("Passed:", passed)
# print("Highest:", highest)
# print("Lowest:", lowest)

# # Average: 82.4
# # Passed: 4
# # Highest: 95
# # Lowest: 68



# ##########################

# grid = [
#     [".", ".", "#", "."],
#     [".", ".", "#", "."],
#     ["#", ".", ".", "."],
#     [".", ".", ".", "."]
# ]

# row = 0
# col = 0

# commands = "DDRRRU"

# for command in commands:

#     new_row = row
#     new_col = col

#     if command == "U":
#         new_row += 1

#     elif command == "D":
#         new_row -= 1

#     elif command == "L":
#         new_col -= 1

#     elif command == "R":
#         new_col += 1

#     if new_row >= 0 and new_row < len(grid) \
#        and new_col >= 0 and new_col < len(grid[0]):

#         row = new_row
#         col = new_col

#     if grid[row][col] == "#":
#         print("Wall!")

# print("Final position:", row, col)

# # Wall!
# # Wall!
# # Wall!
# # Final position: 0 1


##########################


# # O = available
# # X = occupied
# seats = [
#     ["X", "O", "O"],
#     ["X", "X", "O"],
#     ["O", "O", "X"]
# ]

# passengers = 3

# for passenger in range(passengers):

#     for row in range(len(seats)):
#         for col in range(len(seats[row])):

#             if seats[row][col] == "O":
#                 seats[row][col] = "X"

#                 print(
#                     "Passenger",
#                     passenger + 1,
#                     "assigned to",
#                     row,
#                     col
#                 )

#                 break