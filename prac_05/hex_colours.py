COLOUR_DICTIONARY = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "Amber": "#ffbf00", "Amethyst": "#9966cc",
                     "Aqua": "#00ffff", "Ash Grey": "#b2beb5", "Beaver": "#9f8170", "Beige": "#f5f5dc",
                     "Bistre": "#3d2b1f",
                     "Blond": "#faf0be"}

for colour in COLOUR_DICTIONARY:
    print(colour)

colour = input("Enter Colour: ").title()
while colour != "":
    if colour in COLOUR_DICTIONARY:
        print(f"{colour} has the colour code {COLOUR_DICTIONARY[colour]}")
    else:
        print("Invalid colour")
    colour = input("Enter Colour: ").title()
