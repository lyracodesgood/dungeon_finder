"""
In this file I will be constructing a dungeon finder system
Lyra
"""
#from modules.queue import Queue
from modules.linked_list import LinkedList
from modules.stack import Stack
from random import randint

#globals
waiting = LinkedList()#the people wait in here
keep_going = True


classes = ("Ninja", "Warrior", "White Mage",
           "Bard", "Paladin", "Astrologian",
           "Red Mage", "Dark Knight", "Scholar",
           "Samurai", "Gunbreaker", "Sage")
roles = ("DPS", "Tank", "Healer")

#for random name generation in player creation
random_names = Stack()
with open("misc/player_names.txt") as player_names:

    names = player_names.readlines()
    for name in names:
        random_names.push(name)

#dictionaries to iterate over for menu choices
#(name,(class, role))
role_classes = dict(zip( (i + 1 for i in range(12)), zip(classes, roles* 4))) #the double zip w/list comprehension

#main menu
menu = {
    1:"Add player to Dungeon Finder",
    2:"Remove a player from Dungeon Finder",
    3:"Search for player by name",
    4:"Display waiting players",
    5:"Count current players waiting",
    6:"Add randomly generated player",
    7:"Send Dungeon",
    8:"Quit"
}

def print_players(players):
    """helper function to print players better in menus"""
    for key, value in players.items():
        print(f"{key}: {value[0]}, {value[1]}")

def menu_input(menu, bypass = False):
    """takes nothing, returns a number corresponding to menu choice"""
    if bypass == False:
        for key, value in menu.items():
            print(f"{key}: {value}")
    choice = input("Choose a number: ")
    
	#input handling
    try:
        choice = int(choice)
    except:
        print("Error: Input not accepted... ", end = "")
        return menu_input(menu, bypass = True) #i recurse thee
    
    if choice > len(menu):
        print("Error: Input out of bounds... ", end = "")
        return menu_input(menu, bypass = True)
    
    return choice

#functions
#1
def add_player():
    chosen_name = input("Player Name: ")

    print_players(role_classes)
    role_class_key = menu_input(role_classes, bypass = True)

    new_player = (chosen_name, role_classes[role_class_key][0], 
                  role_classes[role_class_key][1])
    waiting.append(new_player) #put em in line

#2
def remove_player():
    """removes a player from the dungeon finder"""
    if len(waiting) == 0:
        print("Error: no one is waiting for a dungeon")
    #TODO finish this after we make display players

    
    player_menu = dict(zip((i + 1 for i in range(len(waiting))),
                          (player.data for player in waiting))) 
    
    print_players(player_menu)
    chosen_player_key = menu_input(player_menu, bypass = True)

    print(f"Removing {player_menu[chosen_player_key]}.")
    waiting.remove(waiting[chosen_player_key].data)
        


#3
def find_player():
    player_name = input("Please input player name: ")
    """finds a player by searching inputted, returns true if found, false otherwise"""
    if len(waiting) == 0:
        print("Error: no players waiting.")
        return
    
    for player in waiting: 
        if player.data[0] == player_name:
            print("Found!")
            return True
        
    print("Not found!")
    return False


#4
def display_waiting():
    """Displays all players currently waiting"""
    if waiting.head == None:
        print("Error: No players waiting.")
        return
    print("Current waiting players:")
    counter = 1
    for player in waiting:
        print(f"{counter}: {player.data[0]} | Class: {player.data[1]} | Role: {player.data[2]}")
        counter += 1

#5 count players
def count_players():
    print(f"Waiting: {len(waiting)}")

#6 random player
def random_player():
    """creates random players"""
    name = random_names.pop()
    role_class = role_classes[randint(1,12)]
    player = (name.split("\n")[0], role_class[0], role_class[1])
    print(f"adding: {player[0]} | {player[1]} | {player[2]}")
    return player

#7 send dungeon
def send_dungeon():
    """puts 4 players in a dungeon, 2 dps 1 healer and 1 tank."""
    if len(waiting) < 4:
        print("Error: Not enough players.")
        return
    
    squad = {"DPS1":(False,"Empty"),
             "DPS2":(False,"Empty"),
             "TANK":(False,"Empty"),
             "HEALER":(False,"Empty")}
    for player in waiting:
        #space for DPS
        #if there is room in either slot and im a dps
        if player.data[2] == "DPS" and (squad["DPS1"][0] == False or squad["DPS2"][0] == False):
            #ternary operator to fill the one we havent filled yet
            if squad["DPS1"][0] == False:
                squad["DPS1"]= (True,player.data)
            else:
                squad["DPS2"] = (True, player.data)
        elif player.data[2] == "DPS":
            #no space
            print(f"Skipping {player.data[0]} | Class: {player.data[1]} | Role: {player.data[2]}")

        #space for TANK
        if player.data[2] == "Tank" and squad["TANK"][0] == False:
            squad["TANK"] = (True, player.data)
        elif player.data[2] == "TANK":
            print(f"Skipping {player.data[0]} | Class: {player.data[1]} | Role: {player.data[2]}")

        #space for HEAL
        if player.data[2] == "Healer" and squad["HEALER"][0] == False:
            squad["HEALER"] = (True, player.data)
        elif player.data[2] == "Healer":
            print(f"Skipping {player.data[0]} | Class: {player.data[1]} | Role: {player.data[2]}")
        
        #check if we are full now
        full = True
        for value in squad.values():
            if value[0] == False:
                full = False
        
        if full:
            break
    
    #if we are still empty after searching everyone
    if full == False:
        print("Error: Not enough players of correct role.")
        return
    
    print("Sending Squad:")
    print(f"DPS 1: {squad["DPS1"][1]}")
    print(f"DPS 2: {squad["DPS2"][1]}")
    print(f"Tank: {squad["TANK"][1]}")
    print(f"Healer: {squad["HEALER"][1]}")

    #remove these guys from the line now
    for value in squad.values():
        waiting.remove(value[1])



def menu_choice(choice):
    """takes a number choice, executes functions corresponding to 
    the menu choices available, returns true or false to keep going or not"""
    match choice:
        case 1:
            add_player()
        case 2:
            remove_player()
        case 3:
            find_player()
        case 4:
            display_waiting()
        case 5:
            count_players()
        case 6:
            waiting.append(random_player())
        case 7:
            send_dungeon()
        case 8:
            return False #to exit
    return True #everything else

#game loop
while keep_going:
    print("Dungeon Finder --------------------------------------<&&&>")
    keep_going = menu_choice(menu_input(menu))