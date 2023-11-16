import random

dice_art = {
    1: ("┌─────────┐",
        "|         |",
        "|    ●    |",
        "|         |",
        "└─────────┘"),

    2: ("┌─────────┐",
        "|  ●      |",
        "|         |",
        "|      ●  |",
        "└─────────┘"),

    3: ("┌─────────┐",
        "| ●       |",
        "|    ●    |",
        "|       ● |",
        "└─────────┘"),

    4: ("┌─────────┐",
        "|  ●   ●  |",
        "|         |",
        "|  ●   ●  |",
        "└─────────┘"),

    5: ("┌─────────┐",
        "| ●     ● |",
        "|    ●    |",
        "| ●     ● |",
        "└─────────┘"),

    6: ("┌─────────┐",
        "| ●     ● |",
        "| ●     ● |",
        "| ●     ● |",
        "└─────────┘"),
}

def roll_die():
    result = random.randint(1, 6)
    for line in dice_art[result]:
        print(line)
    return result

if __name__ == "__main__":
    rolled_value = roll_die()
    print(f"Total: {rolled_value}")
