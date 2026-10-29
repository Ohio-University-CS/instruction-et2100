"""
Terminal Special Effects Demo
- Static map (player cannot walk)
- Press keys to trigger visual effects
- Requires: pip install colorama

Keys:
  Q  Level-up ring around the player (fades after ~1 sec)
  W  Map shakes left/right, then a boss appears
  E  Map loads / reveals from left to right
  R  Rain falls across the map
  F  Firework sparkles burst on the map
  H  Heal pulse (green glow around player)
  X / Ctrl+C  Quit
"""

import sys
import termios
import time
import tty

from colorama import Fore, Style, init

init(autoreset=True)

PLAYER = "👤"
TREE = "🌲"
MONSTER = "👹"
BOSS = "🐲"
RAIN = "|"
SPARK = "*"
RING = "o"
HEAL = "+"

TILE_FROM_LETTER = {
    "T": TREE,
    "M": MONSTER,
    "B": BOSS,
}

EMOJI_TILES = {PLAYER, TREE, MONSTER, BOSS}

COLORS = {
    PLAYER: Fore.CYAN,
    TREE: Fore.GREEN,
    MONSTER: Fore.RED,
    BOSS: Fore.MAGENTA + Style.BRIGHT,
    "#": Fore.WHITE,
    ".": Fore.LIGHTBLACK_EX,
    RING: Fore.YELLOW + Style.BRIGHT,
    RAIN: Fore.CYAN,
    SPARK: Fore.YELLOW + Style.BRIGHT,
    HEAL: Fore.GREEN + Style.BRIGHT,
}

# Simple static map (letters convert to emoji on load)
RAW_MAP = [
    "####################",
    "#..................#",
    "#......T...........#",
    "#..................#",
    "#..........M.......#",
    "#..................#",
    "#....T.............#",
    "#..................#",
    "#..................#",
    "####################",
]

PLAYER_ROW = 5
PLAYER_COL = 5

FRAME = 0.06


# ----------------------------
# Input
# ----------------------------

def get_key():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        key = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)

    if key == "\x03":
        raise KeyboardInterrupt
    return key.lower()


def clear_screen():
    print("\033[2J\033[H", end="")


def load_map():
    rows = []
    for row in RAW_MAP:
        rows.append([TILE_FROM_LETTER.get(ch, ch) for ch in row])
    rows[PLAYER_ROW][PLAYER_COL] = PLAYER
    return rows


# ----------------------------
# Drawing
# ----------------------------

def draw_map(
    game_map,
    overlay=None,
    title="SPECIAL EFFECTS DEMO",
    status="",
    shake_offset=0,
    visible_cols=None,
    flash_color=None,
):
    """
    overlay: dict {(row, col): (char, color)} drawn on top of the map
    shake_offset: spaces added before each line (screen shake)
    visible_cols: if set, only columns 0..visible_cols-1 are shown (loading)
    flash_color: optional full-line tint prefix
    """
    if overlay is None:
        overlay = {}

    clear_screen()

    header = title
    if flash_color:
        print(flash_color + Style.BRIGHT + "=" * 42)
        print(flash_color + Style.BRIGHT + header.center(42))
        print(flash_color + Style.BRIGHT + "=" * 42)
    else:
        print(Fore.CYAN + Style.BRIGHT + "=" * 42)
        print(Fore.CYAN + Style.BRIGHT + header.center(42))
        print(Fore.CYAN + Style.BRIGHT + "=" * 42)
    print()

    rows = len(game_map)
    cols = len(game_map[0])
    pad = " " * max(0, shake_offset)

    for r in range(rows):
        line = pad
        for c in range(cols):
            # Loading reveal: hide columns to the right
            if visible_cols is not None and c >= visible_cols:
                line += "  "
                continue

            if (r, c) in overlay:
                ch, color = overlay[(r, c)]
                tile = ch
            else:
                tile = game_map[r][c]
                color = COLORS.get(tile, Fore.WHITE)

            if tile in EMOJI_TILES or tile in {RING, SPARK, HEAL}:
                # wide / effect glyphs — no trailing space
                if tile in {RING, SPARK, HEAL}:
                    line += color + tile + " "
                else:
                    line += color + tile
            else:
                line += color + tile + " "
        print(line)

    print()
    if status:
        print(status)
        print()

    print(Fore.WHITE + "Q=Level Up  W=Boss Shake  E=Load Map")
    print(Fore.WHITE + "R=Rain  F=Fireworks  H=Heal  X=Quit")


def wait(n=1):
    time.sleep(FRAME * n)


# ----------------------------
# Effects
# ----------------------------

def effect_level_up(game_map):
    """Q — ring expands around the player, then disappears (~1 sec)."""
    neighbors_1 = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]
    neighbors_2 = [
        (-2, -2), (-2, -1), (-2, 0), (-2, 1), (-2, 2),
        (-1, -2),                           (-1, 2),
        (0, -2),                             (0, 2),
        (1, -2),                             (1, 2),
        (2, -2),  (2, -1),  (2, 0),  (2, 1),  (2, 2),
    ]

    rows, cols = len(game_map), len(game_map[0])
    start = time.time()

    # Expanding ring frames, then hold, then fade — total ~1 second
    stages = [
        (neighbors_1, Fore.YELLOW + Style.BRIGHT, "LEVEL UP!"),
        (neighbors_1 + neighbors_2, Fore.YELLOW + Style.BRIGHT, "LEVEL UP!"),
        (neighbors_1 + neighbors_2, Fore.WHITE + Style.BRIGHT, "LEVEL UP!"),
        (neighbors_1, Fore.YELLOW, "Level up!"),
        ([], Fore.YELLOW, "Level up!"),
    ]

    for ring, color, msg in stages:
        overlay = {}
        for dr, dc in ring:
            rr, cc = PLAYER_ROW + dr, PLAYER_COL + dc
            if 0 <= rr < rows and 0 <= cc < cols and game_map[rr][cc] not in EMOJI_TILES:
                if game_map[rr][cc] in {".", "#"}:
                    overlay[(rr, cc)] = (RING, color)

        draw_map(
            game_map,
            overlay=overlay,
            title="LEVEL UP",
            status=color + Style.BRIGHT + f"✨ {msg} ✨",
            flash_color=Fore.YELLOW,
        )
        wait(3)

    # ensure ~1 second total
    elapsed = time.time() - start
    if elapsed < 1.0:
        time.sleep(1.0 - elapsed)

    draw_map(game_map, status=Fore.WHITE + "Ready for the next effect...")


def effect_boss_shake(game_map):
    """W — shake the map left/right, then spawn a boss."""
    for i in range(10):
        offset = 2 if i % 2 == 0 else 0
        draw_map(
            game_map,
            title="⚠ DANGER ⚠",
            status=Fore.RED + Style.BRIGHT + "The ground is shaking...!",
            shake_offset=offset,
            flash_color=Fore.RED,
        )
        wait(2)

    # Spawn boss on empty ground (skip if already on the map)
    already = any(BOSS in row for row in game_map)
    if not already:
        for r, c in [(3, 14), (2, 14), (4, 14), (3, 13), (3, 15), (5, 14)]:
            if game_map[r][c] == ".":
                game_map[r][c] = BOSS
                break

    # Boss slam flash
    for _ in range(3):
        draw_map(
            game_map,
            title="BOSS APPEARS!",
            status=Fore.MAGENTA + Style.BRIGHT + f"A wild {BOSS} Boss appears!",
            flash_color=Fore.MAGENTA,
        )
        wait(2)
        draw_map(
            game_map,
            title="BOSS APPEARS!",
            status=Fore.WHITE + f"A wild {BOSS} Boss appears!",
        )
        wait(2)

    draw_map(
        game_map,
        status=Fore.MAGENTA + Style.BRIGHT + "Boss is on the map!",
    )


def effect_load_map(game_map):
    """E — reveal the map from left to right (loading)."""
    cols = len(game_map[0])
    for visible in range(0, cols + 1):
        pct = int(visible / cols * 100)
        bar = "█" * (visible // 2) + "░" * ((cols - visible) // 2)
        draw_map(
            game_map,
            title="LOADING...",
            status=Fore.CYAN + f"Loading map... {pct}%  [{bar}]",
            visible_cols=visible,
        )
        wait(1)

    draw_map(
        game_map,
        title="LOADED!",
        status=Fore.GREEN + Style.BRIGHT + "Map load complete!",
    )
    wait(5)
    draw_map(game_map, status=Fore.WHITE + "Ready for the next effect...")


def effect_rain(game_map):
    """R — rain drops fall down the map."""
    rows, cols = len(game_map), len(game_map[0])
    # columns that get rain
    rain_cols = [2, 4, 7, 9, 11, 13, 16, 18]

    for frame in range(12):
        overlay = {}
        for i, c in enumerate(rain_cols):
            r = (frame + i * 2) % (rows - 1)
            if r == 0:
                r = 1
            if game_map[r][c] == ".":
                overlay[(r, c)] = (RAIN, Fore.CYAN)
            # trailing drop
            r2 = r - 1
            if r2 >= 1 and game_map[r2][c] == ".":
                overlay[(r2, c)] = (".", Fore.BLUE)

        draw_map(
            game_map,
            overlay=overlay,
            title="RAIN",
            status=Fore.CYAN + "It's raining on the map...",
        )
        wait(2)

    draw_map(game_map, status=Fore.WHITE + "The rain stopped.")


def effect_fireworks(game_map):
    """F — sparkles burst in a few spots on the map."""
    rows, cols = len(game_map), len(game_map[0])
    centers = [(2, 4), (4, 10), (6, 15), (3, 16), (7, 8)]
    colors = [
        Fore.YELLOW,
        Fore.MAGENTA,
        Fore.CYAN,
        Fore.GREEN,
        Fore.RED,
        Fore.WHITE,
    ]

    for frame in range(10):
        overlay = {}
        radius = frame % 4
        color = colors[frame % len(colors)] + Style.BRIGHT

        for cr, cc in centers:
            for dr in range(-radius, radius + 1):
                for dc in range(-radius, radius + 1):
                    if abs(dr) + abs(dc) != radius:
                        continue
                    rr, cc2 = cr + dr, cc + dc
                    if 0 <= rr < rows and 0 <= cc2 < cols and game_map[rr][cc2] == ".":
                        overlay[(rr, cc2)] = (SPARK, color)

        draw_map(
            game_map,
            overlay=overlay,
            title="FIREWORKS",
            status=color + "Boom! Sparkles everywhere!",
            flash_color=colors[frame % len(colors)],
        )
        wait(2)

    draw_map(game_map, status=Fore.WHITE + "Fireworks faded.")


def effect_heal(game_map):
    """H — green heal pulse expanding from the player."""
    rows, cols = len(game_map), len(game_map[0])

    for radius in range(0, 5):
        overlay = {}
        for dr in range(-radius, radius + 1):
            for dc in range(-radius, radius + 1):
                if max(abs(dr), abs(dc)) != radius:
                    continue
                rr, cc = PLAYER_ROW + dr, PLAYER_COL + dc
                if 0 <= rr < rows and 0 <= cc < cols and game_map[rr][cc] == ".":
                    overlay[(rr, cc)] = (HEAL, Fore.GREEN + Style.BRIGHT)

        draw_map(
            game_map,
            overlay=overlay,
            title="HEAL",
            status=Fore.GREEN + Style.BRIGHT + "Healing energy surrounds you...",
            flash_color=Fore.GREEN,
        )
        wait(3)

    draw_map(
        game_map,
        status=Fore.GREEN + Style.BRIGHT + "HP restored! (visual only)",
    )
    wait(4)
    draw_map(game_map, status=Fore.WHITE + "Ready for the next effect...")


# ----------------------------
# Main
# ----------------------------

def main():
    game_map = load_map()

    clear_screen()
    print(Fore.CYAN + Style.BRIGHT + "=" * 42)
    print(Fore.CYAN + Style.BRIGHT + "   SPECIAL EFFECTS DEMO")
    print(Fore.CYAN + Style.BRIGHT + "=" * 42)
    print()
    print(Fore.WHITE + "A static map with player, trees, and a monster.")
    print(Fore.WHITE + "Press keys to play visual effects (no walking).")
    print()
    print(Fore.YELLOW + "Press ENTER to start...")
    input()

    draw_map(game_map, status=Fore.WHITE + "Press a key to trigger an effect...")

    try:
        while True:
            key = get_key()

            if key == "q":
                effect_level_up(game_map)
            elif key == "w":
                effect_boss_shake(game_map)
            elif key == "e":
                effect_load_map(game_map)
            elif key == "r":
                effect_rain(game_map)
            elif key == "f":
                effect_fireworks(game_map)
            elif key == "h":
                effect_heal(game_map)
            elif key == "x":
                break
            else:
                draw_map(
                    game_map,
                    status=Fore.RED + "Unknown key. Try Q W E R F H or X.",
                )

    except KeyboardInterrupt:
        print()

    clear_screen()
    print(Fore.CYAN + "Thanks for watching the effects!")
    print()


if __name__ == "__main__":
    main()
