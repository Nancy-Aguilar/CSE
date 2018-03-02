class Room(object):
    def __init__(self, name, description, north, south, east, west):
        self.name = name
        self.name = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def move(self, direction):
        current_node = globals()[getattr(self, direction)]
        global current_node


# north, south, east, west
# Initialize Rooms
STATUE = ("Tree Statue", "You're standing next to a tree statue, it appears to missing a heart shaped object in its "
                         "center, up North is the Library", 'LIBRARY', None, None, None)
LIBRARY = ("Library", "You are inside the library, standing in the center and there are two book shelves on the West "
                      "and East side of the library, up North is Combat Training room 1", 'CT1', 'STATUE', 'BSE2',
           'BSE1')
BSE1 = ("Book shelves", "You approached the book shelves and they suddenly moved to reveal a secret room", None, None,
        'LIBRARY', 'SECRET1')
BSE2 = ("Book shelves", "You approached the book shelves and they suddenly moved to reveal a secret room", None, None,
        'SECRET2', 'LIBRARY')
SECRET1 = ("Secret Room #1", "You're inside a secret room and the only thing in there is a dusty old book on the "
                             "ground", None, None, 'BSE1', 'SECRET1')
SECRET2 = ("Secret Room #2", "You're inside a secret room and the only thing in there is letter on the ground", None,
           None, 'SECRET2', 'BSE2')
CT1 = ("Combat Training Room 1", "You're inside the training room for 1st years, facing West is the training room for "
                                 "3rd years facing East is the training room for 2nd years, and North is the training "
                                 "room for 4th years", 'CT4', 'LIBRARY', 'CT2', 'CT3')
CT2 = ("Combat Training Room #2", "You are inside the combat training room for 2nd years, on the East side is the"
                                  "office on the West side is the combat training room for 1st years", None, None,
       'OFFICE', 'CT1')

current_node = STATUE
directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']

while True:
    print(current_node[name])
    print(current_node[descriptions])
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        # Look for which command we typed in
        pos = short_directions.index(command)
        # Change the command to be the long form
        command = directions[pos]
    if command in directions:
        try:
           ************
        except KeyError:
            print("You cannot go this way.")
    else:
        print('Command not recognized')