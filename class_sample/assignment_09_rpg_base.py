# Simple Terminal Map Game
# W = Up, S = Down, A = Left, D = Right, Q = Quit

ROWS = 8
COLS = 15

# Player starting position
player_row = 3
player_col = 5

while True:

    # Clear terminal using blank lines
    print("\n" * 30)

    # Draw the map
    for row in range(ROWS):
        for col in range(COLS):

            if row == player_row and col == player_col:
                print("P", end=" ")

            elif row == 0 or row == ROWS - 1:
                print("#", end=" ")

            elif col == 0 or col == COLS - 1:
                print("#", end=" ")

            else:
                print(".", end=" ")

        print()

    print("\nW = Up | S = Down | A = Left | D = Right | Q = Quit")

    move = input("Move: ").lower()

    # Move player
    if move == "w" and player_row > 1:
        player_row -= 1

    elif move == "s" and player_row < ROWS - 2:
        player_row += 1

    elif move == "a" and player_col > 1:
        player_col -= 1

    elif move == "d" and player_col < COLS - 2:
        player_col += 1

    elif move == "q":
        print("Game over!")
        break