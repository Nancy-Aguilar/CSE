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

    # 'CT3':
    #     'NAME': "Combat Training Room 3",
    #     'DESCRIPTION': "You are inside the combat training room for 3rd years, on the East side is the combat"
    #                    "training room for 1st years, on the West side are the dorms for 1st years",
    #     '':
    #         'WEST': 'DORM1',
    #         'EAST': 'CT1'
    #
    # ,
    # 'CT4':
    #     'NAME': "Combat Training Room 4",
    #     'DESCRIPTION': "You are inside the combat training room for 4th years and up North are the classrooms",
    #     '':
    #         'NORTH': 'CLASS',
    #         'SOUTH': 'CT1'
    #
    # ,
    # 'OFFICE':
    #     'NAME': "Office",
    #     'DESCRIPTION': "You are inside the office and facing east is the Nurse's room and facing West is the training "
    #                    "room for 2nd years",
    #     '':
    #         'WEST': 'CT2',
    #         'EAST': 'NURSE'
    #
    # ,
    # 'NURSE':
    #     'NAME': "Nurse's Room",
    #     'DESCRIPTION': "You are inside the Nurse's room and facing east is the Nurse's room and facing North in the "
    #                    "lounge room and facing West if the office",
    #     '':
    #         'WEST': 'OFFICE',
    #         'NORTH': 'LOUNGE'
    #
    # ,
    # 'LOUNGE':
    #     'NAME': "Lounge Room",
    #     'DESCRIPTION': "You're at the lounge room and there's a bag of metals on a sofa, facing West is the cafeteria",
    #     '':
    #         'WEST': 'CAFE',
    #         'SOUTH': 'NURSE'
    #
    # ,
    # 'CAFE':
    #     'NAME': "Cafeteria",
    #     'DESCRIPTION': "You are inside the cafeteria with many tables and chairs and some food trays. Facing East is "
    #                    "the lounge room",
    #     '':
    #         'EAST': 'LOUNGE',
    #
    # ,
    # 'DORMS1':
    #     'NAME': "Dorms for 1st years",
    #     'DESCRIPTION': "You are inside the dorm building, all the rooms are closed and facing North are the 2nd year "
    #                    "dorms",
    #     '':
    #         'NORTH': 'DORMS2',
    #         'EAST': 'CT3'
    #
    # ,
    # 'DORMS2':
    #     'NAME': "Dorms for 2nd years",
    #     'DESCRIPTION': "You are inside the dorm building, all the rooms are closed and facing North are the 3rd year "
    #                    "dorms",
    #     '':
    #         'NORTH': 'DORMS3',
    #         'SOUTH': 'DORMS1'
    #
    # ,
    # 'DORMS3':
    #     'NAME': "Dorms for 3rd years",
    #     'DESCRIPTION': "You are inside the dorm building, all the rooms are closed and facing North are the 4th year "
    #                    "dorms",
    #     '':
    #         'NORTH': 'DORMS4',
    #         'SOUTH': 'DORMS2'
    #
    # ,
    # 'DORMS4':
    #     'NAME': "Dorms for 4th years",
    #     'DESCRIPTION': "You are inside the dorm building, all the rooms are closed and facing North is the power "
    #                    "training room",
    #     '':
    #         'NORTH': 'PTR',
    #         'SOUTH': 'DORMS3'
    #
    # ,
    # 'PTR':
    #     'NAME': "Power Training Room",
    #     'DESCRIPTION': "You're in the power training room and there is a station for creating items up North and facing"
    #                    "East is the weapon room",
    #     '':
    #         'NORTH': 'STATION',
    #         'EAST': 'WEAPON',
    #         'SOUTH': 'DORMS4'
    #
    # ,
    # 'WEAPON':
    #     'NAME': "Weapon Room",
    #     'DESCRIPTION': "You're inside the weapon room, there are some swords on the ground and their is an entrance to "
    #                    "a cave but it's locked and facing South are the classrooms",
    #     '':
    #         'WEST': 'PTR',
    #         'EAST': 'CAVE',
    #         'SOUTH': 'CLASS'
    #
    # ,
    # 'CLASS':
    #     'NAME': "Classroom",
    #     'DESCRIPTION': "You're inside the classrooms and all the rooms are locked facing North is the weapon room",
    #     '':
    #         'NORTH': 'WEAPON',
    #         'SOUTH': 'CT4'
    #
    # ,
    # 'CAVE':
    #     'NAME': "Cave",
    #     'DESCRIPTION': "You're inside the cave and according to what others say you could get lost or even die",
    #     '':
    #         'WEST': 'WEAPON' 