
def show_instructions():
    """Prints the game's welcome screen and rules."""
    print('''
RPG Game
========
Commands:
 go [north / south / east / west]
 get [item]
''')




def show_status():
    """Displays the player's current location, inventory, and visible items."""
    print('---------------------------')
    print(f'You are in the {current_room}')
    print(f'Inventory: {inventory}')
    if "item" in rooms[current_room] and rooms[current_room]["item"]:
        print(f'You see a {rooms[current_room]["item"]}')
        print("""   
         N                +-----------------+
         ^                |     Garage      |
         |                |   (Matchbox)    |
     W <-+-> E            +-----------------+
         |                         ^
         v                         |
         S                         |
+-----------------+       +-----------------+
|    Bathroom     | <---  |   Living Room   |
| (Poop Monster)  |       | (Toilet Cleaner)|
+-----------------+       +-----------------+
                                   ^
                                   |
+-----------------+       +-----------------+
|      Hall       | --->  |   Dining Room   |
|      (Key)      |       |    (Potion)     |
+-----------------+       +-----------------+
         |                         |
         v                         v
+-----------------+       +-----------------+
|     Kitchen     |       |     Garden      |
|    (Monster)    |       |   (Chainsaw)    |
+-----------------+       +-----------------+
                                   |
                                   v
                          +-----------------+       +-----------------+
                          |     Forest      | --->  |    Campsite     |
                          |     (Wood)      |       |  (Ice Tickler)  |
                          +-----------------+       +-----------------+
""")
    print('---------------------------')




# Initialize game variables
inventory = []
current_room = 'Hall'


# Define the game world map layout
rooms = {
    'Bathroom': {
        'east': 'Living Room',
        'item': 'Poop Monster'
    },
    'Garage': {
        'south': 'Living Room',
        'item': 'Matches'
    },
    'Living Room': {
        'south': 'Dining Room',
        'west': 'Bathroom',
        'north': 'Garage',
        'item': 'toilet cleaner'
    },
    'Campsite': {
        'west': 'Forest',
        'item': 'Ice tickler'
    },
    'Forest': {
        'north': 'Garden',
        'east': 'Campsite',
        'item': 'Firewood'


    },
    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'item': 'key'
    },
    'Kitchen': {
        'north': 'Hall',
        'item': 'monster'
    },
    'Dining Room': {
        'west': 'Hall',
        'north': 'Living Room',
        'south': 'Garden',
        'item': 'potion'
    },
    'Garden': {
        'north': 'Dining Room',
        'item': 'chainsaw',
        'south': 'Forest',
    }
}


# Clear terminal screen and show rules once at startup


show_instructions()


# Core Game Loop
while True:
    show_status()


    # Get player input and normalize it
    move = input('>>> ').split(' ', 1)



    # Clear the terminal screen for the next turn




    # Handle empty input gracefully
    if not move or move[0] == '':
        continue


    # ACTION: Handling Movement
    if move[0] == 'go':
        if len(move) > 1 and move[1] in rooms[current_room]:
            current_room = rooms[current_room][move[1]]
        else:
            print("You can't go that way!")


    # ACTION: Handling Picking Up Items
    elif move[0] == 'get':
        if len(move) > 1 and "item" in rooms[current_room] and move[1] == rooms[current_room]['item']:
            inventory.append(move[1])
            print(f'You got the {move[1]}!')
            rooms[current_room]['item'] = ''  # Remove item from room state
        else:
            print(f"You don't see a {move[1] if len(move) > 1 else 'item'} here!")


    else:
        print("Invalid command. Use 'go' or 'get'.")


    # WIN STATE: Reaching the Garden with both Key and Potion
    if current_room == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the mansion with the magic key and potion! You win!')
        break


    # COMBAT/LOSS STATE: Encountering the Monster
    if 'item' in rooms[current_room] and rooms[current_room]['item'] == 'monster':
        if 'chainsaw' in inventory:
            print('You have brutally defeated the monster with a chainsaw!')
            rooms[current_room]['item'] = ''  # Clear monster from the room
        else:
            print('You have been eaten by a Monster! Game Over.')


            break
    if 'item' in rooms[current_room] and rooms[current_room]['item'] == 'Ice tickler':
        if 'matches' and 'Firewood' in inventory:
            print('You melted the Ice Tickler! You win!')
            break
        else:
            print('The Ice Tickler Froze You! Game Over.')
            break


    if 'item' in rooms[current_room] and rooms[current_room]['item'] == 'Poop Monster':
        if 'toilet cleaner' in inventory:
            print \
                ("You Cleaned the bathroom so much that that the poop monster flushed itself down the Toilet! You win!")
            break
        else:
            print("The Poop monster Flushed You! Game Over.")
            break


