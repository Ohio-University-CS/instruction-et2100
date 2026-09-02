import random
import time


# ----------------------------
# Player Setup
# ----------------------------

player = {
    "health": 100,
    "max_health": 100,
    "attack": 15,
    "gold": 0,
    "potions": 2
}


# ----------------------------
# Helper Functions
# ----------------------------

def slow_print(text, delay=0.02):
    """Print text one character at a time."""
    for character in text:
        print(character, end="", flush=True)
        time.sleep(delay)
    print()


def show_status():
    print("\n" + "=" * 35)
    print("❤️  Health :", player["health"], "/", player["max_health"])
    print("⚔️  Attack :", player["attack"])
    print("💰 Gold   :", player["gold"])
    print("🧪 Potions:", player["potions"])
    print("=" * 35)


def use_potion():
    if player["potions"] <= 0:
        print("You don't have any potions!")
        return

    if player["health"] == player["max_health"]:
        print("Your health is already full!")
        return

    healing = random.randint(20, 40)

    player["health"] += healing

    if player["health"] > player["max_health"]:
        player["health"] = player["max_health"]

    player["potions"] -= 1

    print(f"🧪 You drink a potion and recover {healing} health!")


# ----------------------------
# Combat
# ----------------------------

def battle(enemy_name, enemy_health, enemy_attack):

    slow_print(f"\n⚠️ A {enemy_name} appears!")

    while enemy_health > 0 and player["health"] > 0:

        print(f"\n{enemy_name} HP: {enemy_health}")
        print(f"Your HP: {player['health']}")

        print("\n1. Attack")
        print("2. Drink Potion")
        print("3. Try to Run")

        choice = input("> ")

        # Attack
        if choice == "1":

            damage = random.randint(
                player["attack"] - 5,
                player["attack"] + 5
            )

            # Critical hit
            if random.random() < 0.15:
                damage *= 2
                print("💥 CRITICAL HIT!")

            enemy_health -= damage

            print(f"You attack the {enemy_name} for {damage} damage!")

            if enemy_health <= 0:
                break

        # Potion
        elif choice == "2":
            use_potion()

        # Run
        elif choice == "3":

            if random.random() < 0.5:
                print("🏃 You escaped!")
                return True

            print("You failed to escape!")

        else:
            print("Invalid choice.")
            continue

        # Enemy attack
        enemy_damage = random.randint(
            max(1, enemy_attack - 3),
            enemy_attack + 3
        )

        player["health"] -= enemy_damage

        print(
            f"The {enemy_name} attacks you "
            f"for {enemy_damage} damage!"
        )

    if player["health"] <= 0:
        print("\n💀 You have been defeated...")
        return False

    reward = random.randint(10, 30)

    player["gold"] += reward

    print(f"\n🏆 You defeated the {enemy_name}!")
    print(f"💰 You found {reward} gold.")

    return True


# ----------------------------
# Random Events
# ----------------------------

def treasure_event():

    slow_print("\n✨ You discover an old treasure chest!")

    event = random.randint(1, 3)

    if event == 1:

        gold = random.randint(15, 50)

        player["gold"] += gold

        print(f"💰 You found {gold} gold!")

    elif event == 2:

        player["potions"] += 1

        print("🧪 You found a healing potion!")

    else:

        player["attack"] += 3

        print("🗡️ You found a better sword!")
        print("Your attack increased by 3!")


def trap_event():

    damage = random.randint(5, 20)

    player["health"] -= damage

    print("\n💥 A hidden trap activates!")
    print(f"You lose {damage} health.")


def empty_room():

    messages = [
        "The room is completely empty...",
        "You hear something moving behind the walls.",
        "There are strange symbols carved into the stone.",
        "A skeleton sits quietly in the corner.",
        "You find footprints leading deeper into the dungeon."
    ]

    print("\n" + random.choice(messages))


# ----------------------------
# Dungeon Exploration
# ----------------------------

def explore():

    event = random.randint(1, 100)

    if event <= 40:

        enemies = [
            ("Goblin 👺", 35, 8),
            ("Skeleton 💀", 40, 9),
            ("Giant Spider 🕷️", 30, 11),
            ("Orc 👹", 55, 12)
        ]

        enemy = random.choice(enemies)

        return battle(
            enemy[0],
            enemy[1],
            enemy[2]
        )

    elif event <= 65:
        treasure_event()

    elif event <= 80:
        trap_event()

    else:
        empty_room()

    return True


# ----------------------------
# Shop
# ----------------------------

def shop():

    print("\n🧙 You discover a mysterious merchant.")

    while True:

        print("\n--- SHOP ---")
        print(f"Your Gold: {player['gold']}")
        print("1. Healing Potion - 20 gold")
        print("2. Sword Upgrade  - 40 gold")
        print("3. Leave")

        choice = input("> ")

        if choice == "1":

            if player["gold"] >= 20:

                player["gold"] -= 20
                player["potions"] += 1

                print("You bought a potion! 🧪")

            else:
                print("Not enough gold!")

        elif choice == "2":

            if player["gold"] >= 40:

                player["gold"] -= 40
                player["attack"] += 5

                print("Your sword becomes stronger! ⚔️")

            else:
                print("Not enough gold!")

        elif choice == "3":
            break

        else:
            print("Invalid choice.")


# ----------------------------
# Main Game
# ----------------------------

def game():

    print("=" * 45)
    print("       🏰 ESCAPE THE DUNGEON 🏰")
    print("=" * 45)

    name = input("\nWhat is your hero's name? ")

    slow_print(
        f"\n{name}, you wake up inside a dark dungeon."
    )

    slow_print(
        "Somewhere ahead lies the exit..."
    )

    slow_print(
        "Unfortunately, something very large is guarding it."
    )

    rooms = 0

    while player["health"] > 0:

        show_status()

        print("\nWhat do you want to do?")
        print("1. Explore the next room")
        print("2. Drink a potion")
        print("3. Check status")
        print("4. Quit")

        choice = input("> ")

        if choice == "1":

            rooms += 1

            print(f"\n🚪 You enter room #{rooms}...")

            survived = explore()

            if not survived:
                break

            # Merchant every 4 rooms
            if rooms % 4 == 0 and rooms < 10:
                shop()

            # Boss after room 10
            if rooms == 10:

                slow_print(
                    "\n🔥 The dungeon begins to shake..."
                )

                slow_print(
                    "A massive dragon blocks the exit!"
                )

                survived = battle(
                    "DUNGEON DRAGON 🐉",
                    150,
                    18
                )

                if survived:

                    print("\n" + "=" * 45)

                    slow_print(
                        f"🎉 {name} ESCAPED THE DUNGEON!"
                    )

                    print(f"\n💰 Final Gold: {player['gold']}")
                    print(f"❤️ Final Health: {player['health']}")

                    print("\n🏆 YOU WIN! 🏆")
                    print("=" * 45)

                break

        elif choice == "2":
            use_potion()

        elif choice == "3":
            show_status()

        elif choice == "4":

            print("\nYou abandoned the adventure.")
            break

        else:
            print("Please enter 1, 2, 3, or 4.")

    if player["health"] <= 0:

        print("\n" + "=" * 45)
        print("             💀 GAME OVER 💀")
        print("=" * 45)


# Start the game
game()