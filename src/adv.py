from room import Room
from player import Player
# from item import Item


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}
 
# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input("Please, enter player's name : ")
player = Player(name, room['outside'])

room['outside'].add_item('hatchet','add a power to the holder!')
room['outside'].add_item('food','feed yourself!')
room['foyer'].add_item('spell','add some magic to your powers!')
room['overlook'].add_item('ring','how does it feel to be the Lord of the ring?')
room['narrow'].add_item('spell','add some magic to your powers!')
room['treasure'].add_item('energy','boost your powers!')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
directions = ['n', 'e', 's', 'w', 'get', 'drop', 'i', 'inventory']

while True:
    current_room = player.get_current_room()
    north = current_room.n_to
    east = current_room.e_to
    south = current_room.s_to
    west = current_room.w_to
    room_inventory = current_room.room_inventory()
    # print("""a secret map:
    # _______________________
    # |         |-|   *****  |
    # | Overlook|-| Treasure |
    # |         |-|   *****  |
    # |         |-|          | 
    # +---   ---------   ----+
    # |         |-|         |
    # |         |-|         |
    # |  Foyer       Narrow |
    # |         |-|         |vlad
    # |---   ---------------+
    # | outside |
    # |         |\n""")

    print(current_room)
    print(f'\n{player}')
    if room_inventory == None:
        print(f'\n ~*~*~ There are no artifacts in this room ~*~*~')
    else:
        print('\n~*~*~ The following artifacts are in the room  ~*~*~\n')
        for i,y in room_inventory.items():
            print(i,":",y)
        print(f" ~*~ You can input 'get Item's name' to grab the item you want in the room or 'drop Item's name' right here any of those you carry with you. ~*~ ")
        # print(f'\n ~*~*~ The following artifacts are in the room: {room_inventory}~*~*~')

    # print('\nDirecions Available:\n',f'North: {north.name}\n' if north else '----Oops, you can/t go there!----', f'East: {east.name}\n' if east else '', f'South: {south.name}\n' if south else '', f'West: {west.name}\n' if west else '')


    direction = input("Please enter a cardinal direction or enter q to quit the game: ")
    directions_list = direction.split(' ')

    try: 
        if len(directions_list) == 2:
            item_input = directions_list[1]
            if (directions_list[0] == 'get') or (directions_list[0] =='take'):
                player.added_to_inventory(item_input)
                player.on_take(item_input)
            elif directions_list[0] != 'drop':
                print('Wrong command')
            if directions_list[0] == 'drop':
                if item_input in player.player_inventory():
                    player.remove_from_inventory(item_input)
                    player.on_drop(item_input)
                else:
                    print("You don't have that item on you!")

        if direction in directions:
            if direction == 'n':
                if north:
                    player.set_current_room(north)
                else:
                    print(" You can't go North")
            if direction == 'e':
                if east:
                    player.set_current_room(east)
                else:
                    print("You can't go East")
            if direction == 's':
                if south:
                    player.set_current_room(south)
                else:
                    print("You can't go South")
            if direction == 'w':
                if west:
                    player.set_current_room(west)
                else:
                    print("You can't go West")
            if direction == 'i' or 'inventory':
                print('You have the following items in your inventory:')
                print(player.player_inventory())
        if direction == 'q':
            print("Bye for now!")
            break
    except ValueError:
        print("Please enter a cardinal direction")
        


