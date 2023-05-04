##############################################################################
# ADD HEADER HERE
##############################################################################
''' EXPLAIN PROGRAM '''
##############################################################################
# Imports and Global Variables -----------------------------------------------
# ALL VARIABLES NEED A COMMENT
location = [2, 0] # row columb

# ALL VARIABLES NEED A COMMENT
tiles = ["entrance","living room", "kitchen", "basement", "attic"]
spooky_house = [ [tiles[4], tiles[4], tiles[4], tiles[4]], 
                 [tiles[1], tiles[1], tiles[1], tiles[1]], 
                 [tiles[0], tiles[2], tiles[2], tiles[2]],
                 [tiles[3], tiles[3], tiles[3], tiles[3]]   ]

# valid directions and actions for the characters
possible_directions = ["north", "south", "east", "west"]
possible_actions = ["explore","attack","move", "check inventory" "quit"]
attack_actions = ["punch","jump","kick"]
movement_actions = ["jump","slide","forward","backward"]

# Create a dictionary to hold the player's inventory
inventory = {
        'food': {'amount': 10,'description': "You found can of food!"},
        'water': {'amount': 5,'description': "You can quench your thirst!!"},
        'oxygen tank': {'amount': 1,'description': "You found an oxygen tank!"},
        'spacesuit': {'amount': 1,'description': "You found a space suit!"},
        'laser gun': {'amount': 1,'description': "You found a laser gun!!"},
        'repair kit': {'amount': 1,'description': "You found a repair kit!"}
}


# Functions -------------------------------------------------------------------
def Movement():
    '''EXPLAIN FUNCTION'''
    global location
    for direction in possible_directions:
       print(f"* {direction}")
    direction_input = input("Which direction do you want to go?\n") 
    # checking if input is in the list possible_directions
    if direction_input.lower() in possible_directions:
        # Add code here
        if direction_input == "north":
            if location[0] == 0:
              print("Invalid")
            else:
              location[0] = location[0]-1
        elif direction_input == "south":
            # UPDATE OTHER DIRECTIONS
            location[0] = location[0]+1
        elif direction_input == "east":
            location[1] = location[0]+1
        elif direction_input == "west":
            location[1] = location[0]-1
    elif direction_input.lower() not in possible_directions:
        print("Invalid direction!")


def Attack():
    '''EXPLAIN FUNCTION'''
    for attack in attack_actions:
        print(f"*{attack}")
        attack = input("choose strategy:")
    print(f"Great, you {attack}!")


def Move():
    '''EXPLAIN FUNCTION'''
    for Move in movement_actions:
        print(f"*{Move}")
        Move = input("choose movement:")
        if action_input.lower() in movement_actions:
             print(f"{Move} was a good move!")
        

# Define a function to display the player's inventory
def display_inventory():
    '''EXPLAIN FUNCTION'''
    print("Your inventory:")
    for item, count in inventory.items():
        print(f"{item}: {count}")
        

# Define a function to add an item to the player's inventory
def add_item(item, count=1):
    '''EXPLAIN FUNCTION'''
    if item in inventory:
        inventory[item] += count
    else:
        inventory[item] = count
        print(f"{count} {item} added to your inventory.")

  
# Define a function to remove an item from the player's inventory
def remove_item(item, count=1):
    '''EXPLAIN FUNCTION'''
    if item in inventory:
        if inventory[item] >= count:
            inventory[item] -= count
            print(f"{count} {item} removed from your inventory.")
        else:
            print(f"You don't have {count} {item} in your inventory.")
    else:
        print(f"You don't have {item} in your inventory.")


# Main ---------------------------------------------------------------------------------
print("Welcome\n")

# character choices
print("character choices:")
character_choices =["Spiderman","Wonder woman","Iron man"]
print(f"*{character_choices}")
character_choices = input("Choose your character:")
for character in character_choices:
  if character_choices == "Spiderman":
    print("yay,you chose," + "Spiderman")
  if character_choices == "Wonder woman":
    print("yay,you chose," + "Wonder woman")
  if character_choices == "Ironman":
    print("yay,you chose," + "Ironman")

  # Start the continuous playing loop
while True:
    print(spooky_house[location[0]][location[1]])
    print("What do you want to do?")
    for action in possible_actions:
        print(f"* {action}")
    # after user input, print out the action choosen by the user
    action_input = input("Action: ")
    # checking if the input is in the list possible_actions
    if action_input.lower() in possible_actions:
        if action_input == "explore":
            print("You will srtat explorting now.")
            Movement()
        elif action_input == "attack":
            Attack()
        elif action_input == "move":
            Move()
        elif action_input == "check inventory":
            display_inventory()
        elif action_input == "quit":
            print(f"{action_input.title()}!")
            print("Thanks for playing !")
            break
    else:
        print("Invalid Action!")


# Call the display_inventory function to show the initial inventory
    #display_inventory()

# Call the add_item function to add a new item to the inventory
    #add_item('med kit')

# Call the display_inventory function again to show the updated inventory
    #display_inventory()
