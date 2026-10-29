"""
Terminal RPG Map Demo
- WASD to walk (instant keypress — no Enter needed), Q to quit
- Obstacles block movement
- Walking onto monsters / NPCs / items shows an encounter message
- Two maps linked by a . gap in the wall (entry / exit)
- Requires: pip install colorama
"""

import sys
import termios
import tty

from colorama import Fore, Style, init

init(autoreset=True)

# ----------------------------
# Map legend
# ----------------------------
# @  player
# #  wall (obstacle — cannot walk through)
# T  tree (obstacle — cannot walk through)
# R  rock (obstacle — cannot walk through)
# M  monster
# N  NPC
# C  chest
# .  empty ground  (a . in the outer wall is an entry / exit)

# Colors for each tile type
COLORS = {
    "@": Fore.CYAN,
    "#": Fore.WHITE,
    "T": Fore.GREEN,
    "R": Fore.LIGHTBLACK_EX,
    "M": Fore.RED,
    "N": Fore.YELLOW,
    "C": Fore.MAGENTA,
    ".": Fore.LIGHTBLACK_EX,
}

# Human-readable names for encounter messages
ENCOUNTERS = {
    "M": "a fierce Monster!",
    "N": "a friendly NPC.",
    "C": "a mysterious Treasure Chest!",
}

# Tiles the player cannot walk onto
OBSTACLES = {"#", "T", "R"}

# ----------------------------
# Two maps
# Look for the single . in the outer # wall — that is the entry / exit
# ----------------------------

MAPS = {
    "forest": {
        "title": "LOST FOREST",
        "tiles": [
            "####################",
            "#........T.........#",
            "#..M..........C....#",
            "#.......##.........#",
            "#..N....##....R....#",
            "#...................",  # <-- . gap on the right = exit to cave
            "#....T.............#",
            "#.........N........#",
            "#..C..........T....#",
            "#..................#",
            "####################",
        ],
    },
    "cave": {
        "title": "DARK CAVE",
        "tiles": [
            "####################",
            "#....R........M....#",
            "#..C...............#",
            "#......####........#",
            "#......####...N....#",
            "...................#",  # <-- . gap on the left = exit to forest
            "#........T.........#",
            "#..M..........C....#",
            "#.............R....#",
            "#.........N........#",
            "####################",
        ],
    },
}

# Portal links: (map_name, row, col) -> (other_map, spawn_row, spawn_col)
# Standing on the wall gap switches you to the other map.
PORTALS = {
    ("forest", 5, 19): ("cave", 5, 1),    # leave forest right side -> appear in cave
    ("cave", 5, 0): ("forest", 5, 18),    # leave cave left side -> appear in forest
}

# Current map state
current_map = "forest"
game_map = [list(row) for row in MAPS[current_map]["tiles"]]
ROWS = len(game_map)
COLS = len(game_map[0])

# Player starting position (row, col) — must be empty ground
player_row = 1
player_col = 1

# Message shown under the map (no Enter required)
status_message = ""


# ----------------------------
# Instant keypress (no Enter)
# ----------------------------

def get_key():
    """Read one key as soon as it is pressed (no Enter needed)."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        key = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return key.lower()


# ----------------------------
# Intro story
# ----------------------------

def intro():
    print(Fore.CYAN + Style.BRIGHT + "=" * 50)
    print(Fore.CYAN + Style.BRIGHT + "          THE LOST FOREST ADVENTURE")
    print(Fore.CYAN + Style.BRIGHT + "=" * 50)
    print()
    input(Fore.WHITE + "Press ENTER to continue...")
    print()

    print(Fore.YELLOW + "You wake up at the edge of an ancient forest.")
    input(Fore.WHITE + "Press ENTER to continue...")
    print()

    print(Fore.YELLOW + "Locals whisper of monsters, hidden chests,")
    print(Fore.YELLOW + "and a dark cave connected through a break in the wall.")
    input(Fore.WHITE + "Press ENTER to continue...")
    print()

    print(Fore.YELLOW + "Look for a . opening in the # wall — that is the entry / exit.")
    print(Fore.YELLOW + "Use W A S D to move (no Enter needed). Press Q to quit.")
    input(Fore.WHITE + "Press ENTER to begin your journey...")
    print()


# ----------------------------
# Drawing & messages
# ----------------------------

def clear_screen():
    # ANSI clear — works better with instant keypress redraws
    print("\033[2J\033[H", end="")


def draw_map():
    clear_screen()

    title = MAPS[current_map]["title"]
    print(Fore.CYAN + Style.BRIGHT + f"=== {title} ===")
    print()

    for row in range(ROWS):
        line = ""
        for col in range(COLS):
            if row == player_row and col == player_col:
                tile = "@"
            else:
                tile = game_map[row][col]

            # Highlight portal gaps in the wall so they stand out
            if (current_map, row, col) in PORTALS and not (
                row == player_row and col == player_col
            ):
                line += Fore.LIGHTCYAN_EX + Style.BRIGHT + tile + " "
            else:
                color = COLORS.get(tile, Fore.WHITE)
                line += color + tile + " "
        print(line)

    print()
    print(Fore.WHITE + "Legend:")
    print(
        Fore.CYAN + "@" + Fore.WHITE + " You   "
        + Fore.RED + "M" + Fore.WHITE + " Monster   "
        + Fore.YELLOW + "N" + Fore.WHITE + " NPC   "
        + Fore.MAGENTA + "C" + Fore.WHITE + " Chest"
    )
    print(
        Fore.GREEN + "T" + Fore.WHITE + " Tree   "
        + Fore.LIGHTBLACK_EX + "R" + Fore.WHITE + " Rock   "
        + Fore.WHITE + "# Wall   "
        + Fore.LIGHTCYAN_EX + "." + Fore.WHITE + " Entry/Exit"
    )
    print()
    print(Fore.WHITE + "Controls: W=Up  S=Down  A=Left  D=Right  Q=Quit")

    if status_message:
        print()
        print(status_message)


def set_status(message):
    global status_message
    status_message = message


def show_encounter(tile):
    if tile in ENCOUNTERS:
        name = ENCOUNTERS[tile]
        color = COLORS.get(tile, Fore.WHITE)
        set_status(color + Style.BRIGHT + f"You just encounter {name}")


def switch_map(dest_map, spawn_row, spawn_col):
    """Load another map and place the player at the spawn tile."""
    global current_map, game_map, ROWS, COLS, player_row, player_col

    current_map = dest_map
    game_map = [list(row) for row in MAPS[current_map]["tiles"]]
    ROWS = len(game_map)
    COLS = len(game_map[0])
    player_row = spawn_row
    player_col = spawn_col

    title = MAPS[current_map]["title"]
    set_status(
        Fore.LIGHTCYAN_EX
        + Style.BRIGHT
        + f"You pass through the opening... Welcome to the {title}!"
    )


# ----------------------------
# Movement
# ----------------------------

def try_move(d_row, d_col):
    """Attempt to move the player. Return True if the move happened."""
    global player_row, player_col

    new_row = player_row + d_row
    new_col = player_col + d_col

    # Stay inside the map bounds
    if not (0 <= new_row < ROWS and 0 <= new_col < COLS):
        return False

    tile = game_map[new_row][new_col]

    # Blocked by obstacle
    if tile in OBSTACLES:
        set_status(Fore.RED + "You cannot walk through that obstacle!")
        return False

    # Clear old status when a normal move succeeds
    set_status("")

    # Move onto the tile
    player_row = new_row
    player_col = new_col

    # Stepped on an entry / exit gap in the wall -> change maps
    portal_key = (current_map, player_row, player_col)
    if portal_key in PORTALS:
        dest_map, spawn_row, spawn_col = PORTALS[portal_key]
        switch_map(dest_map, spawn_row, spawn_col)
        return True

    # Encounter message for special tiles (monster / NPC / chest)
    show_encounter(tile)
    return True


# ----------------------------
# Main game loop
# ----------------------------

def game():
    intro()

    while True:
        draw_map()
        print()
        print(Fore.CYAN + "Press W/A/S/D to move..." + Style.RESET_ALL)

        move = get_key()

        if move == "w":
            try_move(-1, 0)
        elif move == "s":
            try_move(1, 0)
        elif move == "a":
            try_move(0, -1)
        elif move == "d":
            try_move(0, 1)
        elif move == "q":
            clear_screen()
            print(Fore.CYAN + "Thanks for playing! Farewell, adventurer.")
            break
        else:
            set_status(Fore.RED + "Invalid key. Use W, A, S, D, or Q.")


if __name__ == "__main__":
    game()
