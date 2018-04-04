class Room(object):
    def __init__(self, name, description, north, south, east, west):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# north, south, east, west
# Initialize Rooms
STATUE = Room("Tree Statue", "You're standing next to a tree statue, it appears to missing a heart shaped object in "
                             "its center, up North is the Library", 'LIBRARY', None, None, None)
LIBRARY = Room("Library", "You are inside the library, standing in the center and there are two book shelves on the "
                          "West and East side of the library, up North is Combat Training room 1", 'CT1', 'STATUE',
               'BSE2', 'BSE1')
BSE1 = Room("Book shelves", "You approached the book shelves and they suddenly moved to reveal a secret room", None,
            None, 'LIBRARY', 'SECRET1')
BSE2 = Room("Book shelves", "You approached the book shelves and they suddenly moved to reveal a secret room", None,
            None, 'SECRET2', 'LIBRARY')
SECRET1 = Room("Secret Room #1", "You're inside a secret room and the only thing in there is a dusty old book on the "
                                 "ground", None, None, 'BSE1', 'SECRET1')
SECRET2 = Room("Secret Room #2", "You're inside a secret room and the only thing in there is letter on the ground",
               None, None, 'SECRET2', 'BSE2')
CT1 = Room("Combat Training Room #1", "You're inside the training room for 1st years, facing West is the training "
                                      "room for 3rd years facing East is the training room for 2nd years, and North is "
                                      "the training room for 4th years", 'CT4', 'LIBRARY', 'CT2', 'CT3')
CT2 = Room("Combat Training Room #2", "You're inside the combat training room for 2nd years, on the East side is the "
                                      "office on the West side is the combat training room for 1st years", None, None,
           'OFFICE', 'CT1')
CT3 = Room("Combat Training Room #3", "You're inside the combat training room for 3rd years, on the East side is the "
                                      "combat training room for 1st years, on the West side are the dorms for 1st "
                                      "years", None, None, 'CT1', 'DORMS1')
CT4 = Room("Combat Training Room #4", "You are inside the combat training room for 4th years and up North are the "
                                      "classrooms", 'CLASS', 'CT1', None, None)
OFFICE = Room("Office", "You are inside the office and facing east is the Nurse's room and facing West is the training "
                        "room for 2nd years", None, None, 'NURSE', 'CT2')
NURSE = Room("Nurse's Room", "You're inside the Nurse's room and facing east is the Nurse's room and facing North is "
                             "the lounge room and facing West is the office", 'LOUNGE', None, None, 'OFFICE')
LOUNGE = Room("Lounge Room", "You're at the lounge room and there is a bag of carbon on a sofa, facing West is the "
                             "Cafeteria", None, 'NURSE', None, 'CAFE')
CAFE = Room("Cafeteria", "You are inside the Cafeteria with many tables and chairs and some food trays. Facing East is "
                         "the lounge room", None, None, 'LOUNGE', None)
DORMS1 = Room("Dorms for 1st years", "You are inside a dorm building, all the rooms are closed and facing North are "
                                     "the 2nd year dorms", 'DORMS2', None, 'CT3', None)

DORMS2 = Room("Dorms for 2nd years", "You are inside a dorm building, all the rooms are closed and facing North are "
                                     "the 3rd year dorms", 'DORMS3', 'DORMS1', None, None)
DORMS3 = Room("Dorms for 3rd years", "You are inside a dorm building, all the rooms are closed and facing North are "
                                     "the 4th year dorms", 'DORMS4', 'DORMS2', None, None)

DORMS4 = Room("Dorms for 4th years", "You are inside a dorm building, all the rooms are closed and facing North is "
                                     "the power training room", 'PTR', 'DORMS3', None, None)
PTR = Room("Power Training Room", "You're in the power training room and there is a station for creating items up "
                                  "North and facing East is the weapon room", 'CREATION', 'DORMS4', 'WEAPON', None)
CREATION = Room("Creation Table", "You're standing in front of a table that has four potions, you can create anything "
                                  "you want with the right materials, facing East is the weapon room", None, 'DORMS4',
                'WEAPON', None)
WEAPON = Room("Weapon Room", "You're inside the weapon room, there's a sword and bow/arrow on a table and there is an "
                             "entrance to a cave but it's locked and facing South are the classrooms", None, 'CLASS',
              'CP1', 'PTR')
CLASS = Room("Classroom", "You're inside the classrooms and all the rooms are locked facing North is the weapon room",
             'WEAPON', 'CT4', None, None)
CP1 = Room("Cave Place #1", "You're inside the cave and people say that there are many dangerous things inside and "
                            "multiple places in the cave, there's a light leading South and East", None, 'CP7', 'CP2',
           'WEAPON')
CP2 = Room("Cave PLace #2", "There is nothing here but a light leading East, South, and West", None, 'CP8', 'CP3',
           'CP1')

CP3 = Room("Cave PLace #3", "There is nothing here but a light leading East, South, and West", None, 'CP6', 'CP4',
           'CP2')
CP4 = Room("Cave PLace #4", "There is nothing here but a light leading East, South, and West", None, 'CP8', 'CP3', None)
CP5 = Room("Cave PLace #5", "There is nothing here but a light leading South and West", None, 'CP10', None, 'CP4')
CP6 = Room("Cave PLace #6", "There is nothing here but a light leading North", 'CP3', None, None, None)
CP7 = Room("Cave PLace #7", "There is nothing here but a light leading North, South, and East", 'CP1', 'CP11', 'CP8',
           None)
CP8 = Room("Cave PLace #8", "There is nothing here but a light leading North, South, and West", 'CP2', 'CP12', None,
           'CP7')
CP9 = Room("Cave PLace #9", "There is nothing here but a light leading North, South, and East", 'CP4', 'CP14', 'CP10',
           None)
CP10 = Room("Cave PLace #10", "There is nothing here but a light leading North, South, and West", 'CP5', 'CP15', None,
            'CP9')
CP11 = Room("Cave PLace #11", "There is nothing here but a light leading North and East", 'CP7', None, 'CP12', None)
CP12 = Room("Cave PLace #12", "There is nothing here but a light leading North, East, and West", 'CP8', None, 'CP13',
            'CP11')
CP13 = Room("Cave PLace #13", "There is nothing here but a light leading North, East, and West", 'TREE', None, 'CP14',
            'Cp12')
CP14 = Room("Cave PLace #14", "There is nothing here but a light leading North, East, and West", 'CP9', None, 'CP15',
            'Cp13')
CP15 = Room("Cave PLace #15", "There is nothing here but a light leading North and West", 'CP10', None, None, 'Cp14')
TREE = Room("Crystal Heart Tree", "You're standing in front of a big light tree and in it's center it has a crystal "
                                  "heart", None, 'CP13', None, None)

current_node = STATUE
directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way")
    else:
        print('Command not recognized')