world_map = {
    'STATUE': {
        'NAME': "Tree Statue",
        'DESCRIPTION': "You're standing next to a tree statue, it appears to missing a heart shaped object in its "
                       "center, straight ahead is the library",
        'PATHS': {
            'NORTH': 'LIBRARY',
        }
    },
    'LIBRARY': {
        'NAME': "Library",
        'DESCRIPTION': "You're inside of the library, there are only two book shelves on each side of the library, "
                       "straight ahead is combat training room 1",
        'PATHS': {
            'SOUTH': 'STATUE',
            'NORTH': 'CT1',
            'WEST': 'SECRET1',
            'EAST': 'SECRET2'
        }
    },
    'BSE1': {
        'NAME': "Book shelf",
        'DESCRIPTION': "You're near the book shelves which are now starting to move, revealing a secret room",
        'PATHS': {
            'WEST': 'SECRET1',
            'EAST': 'LIBRARY'
        }
    },
    'BSE2': {
        'NAME': "Book shelves",
        'DESCRIPTION': "You're near the book shelves which are now starting to move, revealing a secret room",
        'PATHS': {
            'EAST': 'SECRET2',
            'WEST': 'LIBRARY'
        }
    },
    'SECRET1': {
        'NAME': "Secret room #1",
        'DESCRIPTION': "You're inside a secret room, on the ground is a big book covered in dust",
        'PATHS': {
            'EAST': 'BSE1'
        }
    },
    'SECRET2': {
        'NAME': "Secret room #2",
        'DESCRIPTION': "You're inside a secret room, on the ground a ripped page for a special heart object",
        'PATHS': {
            'WEST': 'BSE2'
        }
    },
    'CT1': {
        'NAME': "Secret room #2",
        'DESCRIPTION': "You're inside a secret room, ",
        'PATHS': {
            'EAST': 'SECRET2',
            'WEST': 'LIBRARY'

        }
    }
}
