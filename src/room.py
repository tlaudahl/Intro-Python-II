# Implement a class to hold room information. This should have name and
# description attributes.
import random

class Room:
    '''
    Room class that takes a name and description
    Ex: Room('Foyer', 'Dim light filters in from the south. Dusty
passages run north and east.')
    '''
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = self.__generate_items()
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
        return f"{self.name}\n\n{self.description}"
    def __generate_items(self):
        '''
        Generate a random set of loot for the room.
        Treasure room generates 10 items, all other rooms generate only 5
        Only called when class is initialized
        '''
        loot = ['Folder with intelligence', 'Classic matches', 'Dogtag', 'Paracord', 'Corrugated hose', 'Crickent lighter', 'A pack of nails', 'A pack of screws', 'Screw nut', 'Bolts', 'Piece of plexiglass', 'Zibbo lighter', 'Horse figurine', 'Cat figurine', 'Bronze lion', 'Wooden clock', 'Gas analyzer', 'SSD drive', 'SAS drive', 'Military COFDM wireless Signal Transmitter', 'UHF RFID Reader', 'VPX Flash Storage Module', 'Virtex programmable processor', 'Capacitors', 'Wires', 'Broken GPhone X', 'Car battery', 'Power supply unit', 'Graphics card', 'Electric drill', 'Antique vase', 'Antique teapot', 'Silver Badge', 'Golden neck chain', 'Physical bitcoin', 'Portable defibrillator', 'LEDX Skin Transilluminator', '5L propane tank', 'Fuel conditioner', 'A set of tools', 'Secure Flash drive', 'Roler submariner gold wrist watch', 'Battered antique Book', 'Tetriz portable game', 'Chain with Prokill medallion', 'Metal cutting scissors', 'Handdrill', '6-STEN-140-M military battery', 'NIXXOR lens', 'Expeditionary fuel tank', 'FP-100 filter absorber', 'Electric motor', 'Water filter', 'Gunpowder "Eagle"', 'Phased array element', 'Military circuit board', 'Military thermal vision module Iridium', 'Military gyrotachometer', 'OFZ 30x160mm shell', 'Military cable', 'Military power filter', 'Pressure gauge', 'Analog thermometer', 'Gold skull ring', 'Phase control relay']
        if self.name == 'Treasure Chamber':
            return random.choices(loot, k=10)
        else:
            return random.choices(loot, k=5)
