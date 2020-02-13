from room import Room
from player import Player

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
name = input("What is your name? ")
player = Player(name, room['outside'])

while True:
    print(f'{name} is currently in room: {player.current_room.name}\n')
    print(f'{player.current_room.description}\n')
    command = input('Which direction do you want to move? (n, e, s, w, q to quit)')

    if(command != 'q'):
        if (player.current_room == room['outside']):
            if(command != 'n'):
                print('There is nothing in that direction 1\n')
            else:
                player.current_room = player.current_room.n_to
        elif (player.current_room == room['foyer']):
            if(command == 'w'):
                print('There is nothing in that direction 2\n')
            elif(command == 's'):
                player.current_room = player.current_room.s_to
            elif(command == 'e'):
                player.current_room = player.current_room.e_to
            elif(command == 'n'):
                player.current_room = player.current_room.n_to
        elif (player.current_room == room['overlook']):
            if(command != 's'):
                print('There is nothing in that direction 3\n')
            else:
                player.current_room = player.current_room.s_to
        elif (player.current_room == room['narrow']):
            if(command != 'w' and command != 'n'):
                print('There is nothing in that direction 4\n')
            elif(command == 'w'):
                player.current_room = player.current_room.w_to
            elif(command == 'n'):
                player.current_room = player.current_room.n_to
        elif(player.current_room == room['treasure']):
            if(command != 's'):
                print('There is nothing in that direction 5\n')
            else:
                player.current_room = player.current_room.s_to
    else:
        print('Thanks for playing!')
        exit()
