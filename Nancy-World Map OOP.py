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
CT1 = ("Combat Training Room #1", "You're inside the training room for 1st years, facing West is the training room for "
                                 "3rd years facing East is the training room for 2nd years, and North is the training "
                                 "room for 4th years", 'CT4', 'LIBRARY', 'CT2', 'CT3')
CT2 = ("Combat Training Room #2", "You are inside the combat training room for 2nd years, on the East side is the "
                                  "office on the West side is the combat training room for 1st years", None, None,
       'OFFICE', 'CT1')
CT3 = ("Combat Training Room #3", "You are inside the combat training room for 3rd years, on the East side is the "
                                  "combat training room for 1st years, on the West side are the dorms for 1st years",
       None, None, 'CT1', 'DORM1')
CT4 = ("Combat Training Room #4", "You are inside the combat training room for 4th years and up North are the "
                                  "classrooms",'CLASS', 'CT1', None, None)
OFFICE = ("Office", "You are inside the office and facing east is the Nurse's room and facing West is the training "
                       "room for 2nd years",None, None, 'NURSE', 'CT2')
NURSE = ("Nurse's Room", "You are inside the Nurse's room and facing east is the Nurse's room and facing North in the "
                       "lounge room and facing West if the office", 'LOUNGE', None, None, 'OFFICE')
LOUNGE = ("Lounge Room", "You're at the lounge room and there's a bag of metals on a sofa, facing West is the "
                         "cafeteria", None, 'NURSE', None, 'CAFE')
CAFE = ("Cafeteria", "You are inside the cafeteria with many tables and chairs and some food trays. Facing East is "
                       "the lounge room", None, None, 'LOUNGE', None)
DORMS1 = ("Dorms for 1st years", "You are inside the dorm building, all the rooms are closed and facing North are the "
                                 "2nd year dorms", 'DORMS2', None, 'CT3', None)

DORMS2 = ("Dorms for 2nd years", "You are inside the dorm building, all the rooms are closed and facing North are the "
                                 "3rd year dorms", 'DORMS3', 'DORMS1', None, None)
DORMS3 = ("Dorms for 3rd years", "You are inside the dorm building, all the rooms are closed and facing North are the "
                                 "4th year dorms", 'DORMS4', 'DORMS2', None, None)

DORMS4 = ("Dorms for 4th years", "You are inside the dorm building, all the rooms are closed and facing North is the "
                                 "power training room", 'PTR', 'DORMS3', None, None)
PTR = ("Power Training Room", "You're in the power training room and there is a station for creating items up North and "
                              "facing East is the weapon room", 'CREATION', 'DORMS4', 'WEAPON', None)
CREATION = ("Creation Table", "You're standing in front of a table that has four potions, you can create "
                               "anything you want with the right materials, facing East is the weapon room", None,
            'DORMS4', 'WEAPON', None)
WEAPON = ("Weapon Room", "You're inside the weapon room, there are some swords on the ground and there is an entrance "
                         "to a cave but it's locked and facing South are the classrooms", None, 'CLASS', 'CP1', 'PTR')
CLASS = ("Classroom", "You're inside the classrooms and all the rooms are locked facing North is the weapon room",
         'WEAPON', 'CT4', None, None)
CP1 = ("Cave Place #1", "You're inside the cave and people say that there are many dangerous things inside multiple "
                        "places in the cave, there's a light leading South and East", None, 'CP7', 'CP2', 'WEAPON')
CP2 = ("Cave PLace #2", "There is nothing here but a light leading East, South, and West", None, 'CP8', 'CP3', 'CP1')

CP3 = ("Cave PLace #3", "There is nothing here but a light leading East, South, and West", None, 'CP6', 'CP4', 'CP2')
CP4 = ("Cave PLace #4", "There is nothing here but a light leading East, South, and West", None, 'CP8', 'CP3', None)
CP5 = ("Cave PLace #5", "There is nothing here but a light leading South and West", None, 'CP10', None, 'CP4')
CP6 = ("Cave PLace #6", "There is nothing here but a light leading North", 'CP3', None, None, None)
CP7 = ("Cave PLace #7", "There is nothing here but a light leading North, South, and East", 'CP1', 'CP11', 'CP8', None)
CP8 = ("Cave PLace #8", "There is nothing here but a light leading North, South, and West", 'CP2', 'CP12', None, 'CP7')
CP9 = ("Cave PLace #9", "There is nothing here but a light leading North, South, and East", 'CP4', 'CP14', 'CP10', None)
CP10 = ("Cave PLace #10", "There is nothing here but a light leading North, South, and West", 'CP5', 'CP15', None,
        'CP9')
CP11 = ("Cave PLace #11", "There is nothing here but a light leading North and East", 'CP7', None, 'CP12', None)
CP12 = ("Cave PLace #12", "There is nothing here but a light leading North, East, and West", 'CP8', None,
        'CP13', 'CP11')
CP13 = ("Cave PLace #13", "There is nothing here but a light leading North, East, and West", 'TREE', None, 'CP14',
        'Cp12')
CP14 = ("Cave PLace #14",)
CP15 = ("Cave PLace #15",)
TREE = ("Crystal Heart Tree",)

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
            print("You cannot go this way")
    else:
        print('Command not recognized')