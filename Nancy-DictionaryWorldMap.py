world_map = {
    'STATUE': {
        'NAME': "Tree Statue",
        'DESCRIPTION': "You're standing next to a tree statue, it appears to missing a heart shaped object in its "
                       "center, up North is the Library",
        'PATHS': {
            'NORTH': 'LIBRARY',
        }
    },
    'LIBRARY': {
        'NAME': "Library",
        'DESCRIPTION': "You are inside the library, standing in the center and there are two book shelves on the West "
                       "and East side of the library, up North is Combat Training room 1",
        'PATHS': {
            'SOUTH': 'STATUE',
            'NORTH': 'CT1',
            'WEST': 'BSE1',
            'EAST': 'BSE2'
        }
    },
    'BSE1': {
        'NAME': "Book shelves",
        'DESCRIPTION': "You approached the book shelves and they suddenly moved to reveal a secret room",
        'PATHS': {
            'WEST': 'SECRET1',
            'EAST': 'LIBRARY'
        }
    },
    'BSE2': {
        'NAME': "Book shelves",
        'DESCRIPTION': "You approached the book shelves and they suddenly moved to reveal a secret room",
        'PATHS': {
            'EAST': 'SECRET2',
            'WEST': 'LIBRARY'
        }
    },
    'SECRET1': {
        'NAME': "Secret Room #1",
        'DESCRIPTION': "You're inside a secret room and the only thing in there is a dusty old book on the ground",
        'PATHS': {
            'WEST': 'SECRET1',
            'EAST': 'BSE1'
        }
    },
    'SECRET2': {
        'NAME': "Secret Room #2",
        'DESCRIPTION': "You're inside a secret room and the only thing in there is letter on the ground",
        'PATHS': {
            'EAST': 'SECRET2',
            'WEST': 'BSE2'
        }
    },
    'CT1': {
        'NAME': "Combat Training Room 1",
        'DESCRIPTION': "You're inside the training room for 1st years, facing West is the training room for 3rd years, "
                       "facing East is the training room for 2nd years, and North is the training room for 4th years",
        'PATHS': {
            'WEST': 'CT3',
            'EAST': 'CT2',
            'NORTH': 'CT4',
            'SOUTH': 'LIBRARY'

        }
    },
    'CT2': {
        'NAME': "Combat Training Room 2",
        'DESCRIPTION': "You are inside the combat training room for 2nd years, on the East side is the office, "
                       "on the West side is the combat training room for 1st years",
        'PATHS': {
            'WEST': 'CT1',
            'EAST': 'OFFICE'
        }
    },
    'CT3': {
        'NAME': "Combat Training Room 3",
        'DESCRIPTION': "You are inside the combat training room for 3rd years, on the East side is the combat"
                       "training room for 1st years, on the West side are the dorms for 1st years",
        'PATHS': {
            'WEST': 'DORM1',
            'EAST': 'CT1'
        }
    },
    'CT4': {
        'NAME': "Combat Training Room 4",
        'DESCRIPTION': "You are inside the combat training room for 4th years and up North are the classrooms",
        'PATHS': {
            'NORTH': 'CLASS',
            'SOUTH': 'CT1'
        }
    },
    'OFFICE': {
        'NAME': "Office",
        'DESCRIPTION': "You are inside the office and facing east is the Nurse's room and facing West is the training "
                       "room for 2nd years",
        'PATHS': {
            'WEST': 'CT2',
            'EAST': 'NURSE'
        }
    },
    'NURSE': {
        'NAME': "Nurse's Room",
        'DESCRIPTION': "You are inside the Nurse's room and facing east is the Nurse's room and facing North in the "
                       "lounge room and facing West if the office",
        'PATHS': {
            'WEST': 'OFFICE',
            'NORTH': 'LOUNGE'
        }
    },
    'LOUNGE': {
        'NAME': "Lounge Room",
        'DESCRIPTION': "You're at the lounge room and there's a bag of metals on a sofa, facing West is the cafeteria",
        'PATHS': {
            'WEST': 'CAFE',
            'SOUTH': 'NURSE'
        }
    },
    'CAFE': {
        'NAME': "Cafeteria",
        'DESCRIPTION': "You are inside the cafeteria with many tables and chairs and some food trays. Facing East is "
                       "the lounge room",
        'PATHS': {
            'EAST': 'LOUNGE',
        }
    },
    'DORMS1': {
        'NAME': "Dorms for 1st years",
        'DESCRIPTION': "You are inside the dorm building, all the rooms are closed and facing North are the 2nd year "
                       "dorms",
        'PATHS': {
            'NORTH': 'DORMS2',
            'EAST': 'CT3'
        }
    },
    'DORMS2': {
        'NAME': "",
        'DESCRIPTION': "You are inside the dorm building, all the rooms are closed and facing North are the 3rd year "
                       "dorms",
        'PATHS': {
            'NORTH': 'DORMS3',
            'SOUTH': 'DORMS1'
        }
    },
    'DORMS3': {
        'NAME': "",
        'DESCRIPTION': "You are inside the dorm building, all the rooms are closed and facing North are the 4th year "
                       "dorms",
        'PATHS': {
            'NORTH': 'DORMS4',
            'SOUTH': 'DORMS2'
        }
    },
    'DORMS4': {
        'NAME': "",
        'DESCRIPTION': "You are inside the dorm building, all the rooms are closed and facing North is the power "
                       "training room",
        'PATHS': {
            'NORTH': 'PTR',
            'SOUTH': 'DORMS3'
        }
    },
    'PTR': {
        'NAME': "Power Training Room",
        'DESCRIPTION': "You're in the power training room and there is a station for creating items up North and facing"
                       "East is the weapon room",
        'PATHS': {
            'NORTH': 'STATION',
            'EAST': 'WEAPON',
            'SOUTH': 'DORMS4'
        }
    },
    'WEAPON': {
        'NAME': "Weapon Room",
        'DESCRIPTION': "You're inside the weapon room, there are some swords on the ground and their is an entrance to "
                       "a cave but it's locked and facing South are the classrooms",
        'PATHS': {
            'WEST': 'PTR',
            'EAST': 'CAVE',
            'SOUTH': 'CLASS'
        }
    },
    'CLASS': {
        'NAME': "Classroom",
        'DESCRIPTION': "You're inside the classrooms and all the rooms are locked facing North is the weapon room",
        'PATHS': {
            'NORTH': 'WEAPON',
            'SOUTH': 'CT4'
        }
    },
    'CAVE': {
        'NAME': "Cave",
        'DESCRIPTION': "You're inside the cave and according to what others say you could get lost or even die",
        'PATHS': {
            'WEST': 'WEAPON'
        }
    }
}

current_node = world_map['STATUE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("You cannot go this way.")
    else:
        print('Command not recognized')