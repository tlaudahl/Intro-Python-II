# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    '''
    Player class that takes a name, a room, and a stash
    Ex: Player('Travis', 'Foyer', ['List', 'Of', 'Items'])
    '''
    def __init__(self, name, current_room, stash):
        self.name = name
        self.current_room = current_room
        self.stash = stash
    def travel(self, direction):
        next_room = getattr(self.current_room, f'{direction}_to')
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print('You cannot move in that direction')
    def modify_stash(self, command, item):
        '''
        Method that allows you to modify the stash of the player. Takes in a command, and an item.
        Ex: modify_stash('take', sword)
        That will add a sword to the player's items and remove the sword from that room
        '''
        if command == 'take' and item == 'all':
            if (len(self.stash) + len(self.current_room.items) <= 6):
                self.stash.extend(self.current_room.items)
                self.current_room.items = []
                print(f'You currently have {str(self.stash).strip("[]")} ')
                return
            else:
                print(f'You are carrying too many items, you can only carry 6, you currently are carrying {len(self.stash)}')
                return
        elif command == 'take' and len(self.stash) <= 6:
            try:
                self.current_room.items.remove(item)
                self.stash.append(item)
                print(f'You currently have {str(self.stash).strip("[]")} ')
                return
            except ValueError:
                print('That item does not exist in the room')
                return
        elif command == 'drop':
            try:
                self.stash.remove(item)
                self.current_room.items.append(item)
                return
            except ValueError:
                print('That item does not exist in your stash')
                print(f'\nYou currently have {str(self.stash).strip("[]")}')
                return
        else:
            print('You are holding to many items! Drop some more before taking others')
            return
            
