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


#OLD DEBUGGING CODE FROM WHEN I WAS USING A QUEUE
# waiting.enqueue("peter")
# waiting.enqueue("mary")
# waiting.enqueue("johnny")
# print(len(waiting))

menu = {
    1:"Add player to Dungeon Finder",
    2:"Remove a player from Dungeon Finder",
    3:"Search for player by name",
    4:"Display waiting players",
    5:"Count current players waiting",
    6:"Quit"
}

#functions
#1
def add_player(bypass = False):
    if bypass == False:
        print(">----input player data----<")
    
    #TODO could do some input validation here
    chosen_name = input("Player Name: ")
    chosen_class = input("Player Class: ")
    chosen_role = input("Player Role: ")
    
    new_player = Player(chosen_name, chosen_class, chosen_role)
    waiting.append(new_player) #put em in line

#2
def remove_player(player_name):
    """removes a player based on their name"""
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

def menu_input(bypass = False):
    """takes nothing, returns a number corresponding to menu choice"""
    if bypass == False:
        print(">----Dungeon Finder----<")
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
        print("Error: Input not accepted... ", end = "")
        return menu_input(bypass = True) #i recurse thee
    return choice

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



while keep_going:
    keep_going = menu_choice(menu_input())