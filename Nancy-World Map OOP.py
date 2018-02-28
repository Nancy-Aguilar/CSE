class Room(object):
    def __init__(self, name, north, south, east, west):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Initialize Rooms
STATUE = ("Tree Statue", 'LIBRARY')
LIBRARY = ("Library", 'STATUE', 'CT1', 'BSE1', 'BSE2')
BSE1 = ("Book shelves", 'SECRET1', 'LIBRARY')
BSE2 = ("Book shelves", 'SECRET2', 'LIBRARY')
SECRET1 = ("Secret room #1", 'BSE1')
SECRET2 = ("Secret room #2", 'BSE2')
CT1 = ("Combat Training Room 1", 'CT2', 'CT3', 'CT4', 'LIBRARY')
CT2 = ("Combat Training Room 2", 'CT1', 'OFFICE')
CT3 = ("Combat Training Room 3", 'DORM1', 'CT1')
CT4 = ("Combat Training Room 4", 'CLASS', 'CT1')
OFFICE = ("Office", 'CT2', 'NURSE')
NURSE = ("Nurse's Room", 'OFFICE', 'LOUNGE')
LOUNGE = ("Lounge Room", 'CAFE', 'NURSE')

