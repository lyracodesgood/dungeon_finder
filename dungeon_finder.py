"""
In this file I will be constructing a dungeon finder system
Lyra
"""
#from modules.queue import Queue
from modules.player import Player
from modules.linked_list import LinkedList

#globals
waiting = LinkedList()#the people wait in here
keep_going = True

#dictionaries to iterate over for menu choices
role_classes = dict(zip( (i + 1 for i in range(12)), 
                    zip(("Ninja", "Warrior", "White Mage",
           "Bard", "Paladin", "Astrologian",
           "Red Mage", "Dark Knight", "Scholar",
           "Samurai", "Gunbreaker", "Sage"), 
           ("DPS", "Tank", "Healer") * 4))) #the double zip

#main menu
menu = {
    1:"Add player to Dungeon Finder",
    2:"Remove a player from Dungeon Finder",
    3:"Search for player by name",
    4:"Display waiting players",
    5:"Count current players waiting",
    6:"Quit"
}

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
        return menu_input(bypass = True) #i recurse thee
    
    if choice > len(menu):
        print("Error: Input out of bounds... ", end = "")
        return menu_input(bypass = True)
    
    return choice

#functions
#1
def add_player():
    chosen_name = input("Player Name: ")
    for key, value in role_classes.items():
        print(f"{key}: {value[0]}, {value[1]}")
    role_class_key = menu_input(role_classes, bypass = True)
    new_player = Player(chosen_name, role_classes[role_class_key][0], role_classes[role_class_key][1])
    waiting.append(new_player) #put em in line

#2
def remove_player():
    """removes a player from the dungeon finder"""
    if len(waiting) == 0:
        print("Error: no one is waiting for a dungeon")
    #TODO finish this after we make display players

    #traverse here
    current_node = waiting.head
    while current_node.next != None: #while there is a node to go to
        if current_node.data.name == player_name: 
            waiting.remove(current_node)
            print(f"Removed {current_node}")

#3
def find_player(player_name):

#4
def display_waiting():
    """Displays all players currently waiting"""
    if waiting.head == None:
        print("Error: No players waiting.")
        return
    print("Current waiting players:")
    counter = 1
    for player in waiting:
        print(f"{counter}: {player.data.name} | class: {player.data.job} | Role: {player.data.role}")
        counter += 1


def menu_choice(choice):
    """takes a number choice, executes functions corresponding to 
    the menu choices available, returns true or false to keep going or not"""
    match choice:
        case 1:
            add_player()
        case 2:
            remove_player()
        case 3:
            pass
        case 4:
            display_waiting()
        case 5:
            pass
        case 6:
            return False #to exit
    return True #everything else


#game loop
while keep_going:
    print("Dungeon Finder --------------------------------------<&&&>")
    keep_going = menu_choice(menu_input(menu))