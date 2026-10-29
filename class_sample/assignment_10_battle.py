"""
Terminal Battle Animation Demo
- A = attack animation
- S = skill animation (flashy text effect)
- Q / Ctrl+C = quit
- No HP — just visuals
- Requires: pip install colorama
"""

import sys
import termios
import time
import tty

from colorama import Fore, Style, Back, init

init(autoreset=True)

PLAYER = "( ͡° ͜ʖ ͡°)"
MONSTER = "( ˇ෴ˇ )"

# Layout: left padding for player, gap, then monster
PLAYER_BASE_COL = 4
MONSTER_BASE_COL = 40
ARENA_WIDTH = 60

FRAME_DELAY = 0.08


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

    if key == "\x03":
        raise KeyboardInterrupt

    return key.lower()


def clear_screen():
    print("\033[2J\033[H", end="")


def draw_scene(
    player_col,
    monster_col,
    title="BATTLE!",
    status="",
    effect_line="",
    projectile_col=None,
):
    """Draw player and monster at given column offsets. Optional 💥 projectile."""
    clear_screen()

    print(Fore.CYAN + Style.BRIGHT + "=" * ARENA_WIDTH)
    print(Fore.CYAN + Style.BRIGHT + title.center(ARENA_WIDTH))
    print(Fore.CYAN + Style.BRIGHT + "=" * ARENA_WIDTH)
    print()

    # Sky / empty rows
    print()
    print()

    # Character row — list of (color, char) cells
    cells = [(" ", " ")] * ARENA_WIDTH

    def place_text(text, col, color):
        nonlocal cells
        cells = list(cells)
        for i, ch in enumerate(text):
            pos = col + i
            if 0 <= pos < ARENA_WIDTH:
                cells[pos] = (color, ch)

    place_text(PLAYER, player_col, Fore.CYAN + Style.BRIGHT)
    place_text(MONSTER, monster_col, Fore.RED + Style.BRIGHT)

    if projectile_col is not None:
        place_text("💥", projectile_col, Fore.YELLOW + Style.BRIGHT)

    line = "".join(color + ch for color, ch in cells)
    print(line)

    # Ground
    print(Fore.GREEN + "~" * ARENA_WIDTH)
    print()

    if effect_line:
        print(effect_line)
        print()

    if status:
        print(status)
        print()

    print(Fore.WHITE + "Controls: A=Attack   S=Skill   Q / Ctrl+C=Quit")


def wait_frames(n=1):
    time.sleep(FRAME_DELAY * n)


def shake_monster(title="HIT!", status="", effect_line="", shakes=4):
    """Shake the monster left and right when hit."""
    for i in range(shakes):
        offset = -1 if i % 2 == 0 else 1
        draw_scene(
            PLAYER_BASE_COL,
            MONSTER_BASE_COL + offset,
            title=title,
            status=status,
            effect_line=effect_line,
        )
        wait_frames(1)

    # Settle back to center
    draw_scene(
        PLAYER_BASE_COL,
        MONSTER_BASE_COL,
        title="BATTLE!",
        status=Fore.WHITE + "Ready...",
    )
    wait_frames(1)


# ----------------------------
# Attack animation
# ----------------------------

def animate_attack():
    """
    Player lunges right one step, then returns.
    Monster shakes left and right when hit.
    """
    # Player moves right
    draw_scene(
        PLAYER_BASE_COL + 1,
        MONSTER_BASE_COL,
        title="ATTACK!",
        status=Fore.YELLOW + "You strike!",
        effect_line=Fore.YELLOW + Style.BRIGHT + "        * whoosh *",
    )
    wait_frames(2)

    # Player back
    draw_scene(
        PLAYER_BASE_COL,
        MONSTER_BASE_COL,
        title="ATTACK!",
        status=Fore.YELLOW + "You strike!",
    )
    wait_frames(1)

    # Monster hit — shake left / right
    shake_monster(
        title="HIT!",
        status=Fore.RED + Style.BRIGHT + "Monster takes a hit!",
        effect_line=Fore.RED + Style.BRIGHT + " " * 36 + "* BAM *",
        shakes=4,
    )


# ----------------------------
# Skill animation (💥 flies from player to monster)
# ----------------------------

def animate_skill():
    """Skill: launch 💥 from player, fly into monster, then monster shakes."""
    flash_colors = [
        Fore.MAGENTA,
        Fore.YELLOW,
        Fore.CYAN,
        Fore.GREEN,
        Fore.RED,
        Fore.BLUE,
    ]

    # Charge-up flashes
    for i, color in enumerate(flash_colors[:4]):
        burst = (color + Style.BRIGHT + "* S K I L L *").center(ARENA_WIDTH + 10)
        draw_scene(
            PLAYER_BASE_COL,
            MONSTER_BASE_COL,
            title=color + Style.BRIGHT + ">>> SKILL <<<",
            status=color + Style.BRIGHT + "Charging power...",
            effect_line=burst,
        )
        wait_frames(1)

    # 💥 flies from just after the player toward the monster
    start_col = PLAYER_BASE_COL + len(PLAYER) + 1
    end_col = MONSTER_BASE_COL - 2

    for col in range(start_col, end_col + 1, 2):
        color = flash_colors[(col // 2) % len(flash_colors)]
        draw_scene(
            PLAYER_BASE_COL,
            MONSTER_BASE_COL,
            title=color + Style.BRIGHT + ">>> SKILL <<<",
            status=Fore.MAGENTA + Style.BRIGHT + "💥 flying...!",
            projectile_col=col,
        )
        wait_frames(1)

    # Impact on monster
    draw_scene(
        PLAYER_BASE_COL,
        MONSTER_BASE_COL,
        title=Fore.YELLOW + Style.BRIGHT + "BOOM!",
        status=Fore.RED + Style.BRIGHT + "💥 hits the monster!",
        effect_line=Fore.YELLOW + Style.BRIGHT + Back.RED + " ~~~ KA-BOOM ~~~ " + Style.RESET_ALL,
        projectile_col=MONSTER_BASE_COL - 1,
    )
    wait_frames(2)

    # Monster shakes left / right from the blast
    shake_monster(
        title=Fore.MAGENTA + Style.BRIGHT + "CRITICAL!",
        status=Fore.RED + Style.BRIGHT + "Monster is blasted!",
        effect_line=Fore.YELLOW + Style.BRIGHT + "💥💥💥",
        shakes=6,
    )


# ----------------------------
# Main loop
# ----------------------------

def battle():
    clear_screen()
    print(Fore.CYAN + Style.BRIGHT + "=" * 50)
    print(Fore.CYAN + Style.BRIGHT + "       TERMINAL BATTLE ARENA")
    print(Fore.CYAN + Style.BRIGHT + "=" * 50)
    print()
    print(Fore.WHITE + f"  You     : {Fore.CYAN}{PLAYER}")
    print(Fore.WHITE + f"  Monster : {Fore.RED}{MONSTER}")
    print()
    print(Fore.YELLOW + "Press ENTER to start the battle...")
    input()

    status = Fore.WHITE + "Ready... Press A or S!"

    try:
        while True:
            draw_scene(
                PLAYER_BASE_COL,
                MONSTER_BASE_COL,
                title="BATTLE!",
                status=status,
            )
            print()
            print(Fore.CYAN + "Waiting for input..." + Style.RESET_ALL)

            key = get_key()

            if key == "a":
                animate_attack()
                status = Fore.WHITE + "Ready... Press A or S!"
            elif key == "s":
                animate_skill()
                status = Fore.WHITE + "Ready... Press A or S!"
            elif key == "q":
                break
            else:
                status = Fore.RED + "Invalid key. Use A, S, or Q."

    except KeyboardInterrupt:
        print()

    clear_screen()
    print(Fore.CYAN + "Battle over. Farewell, adventurer!")
    print()


if __name__ == "__main__":
    battle()
