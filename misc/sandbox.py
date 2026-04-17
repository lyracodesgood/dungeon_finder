"""
for messing around with whatever
"""

#opening a list of names from the internet and getting just the first names
with open("misc/player_names.txt", "w") as player_names:
    with open("misc/names.txt", "r") as names_file:
        names = names_file.readlines()
        print(names)
        for name in names:
            first_last = name.split()
            player_names.write(first_last[0] + "\n")
            print(f"writing {first_last[0]}")
print("done")
