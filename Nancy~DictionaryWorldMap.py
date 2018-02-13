world_map = {
    'STATUE': {
        'NAME': "Tree Statue",
        'DESCRIPTION': "You're standing next to a tree statue, it appears to missing a heart shaped object in its "
                       "center",
        'PATHS': {
            'NORTH': 'LIBRARY',
        }
    },
    'LIBRARY': {
        'NAME': "Library",
        'DESCRIPTION': "You are at the front of the library and the doors are wide open",
        'PATHS': {
            'SOUTH': 'STATUE',
            'NORTH': 'LIBRARY'
        }
    },
    'SOUTHHOUSE': {
        'NAME': "South of House",
        'DESCRIPTION': "Insert Description here",
        'PATHS': {
            'NORTH': 'WESTHOUSE'
        }
    }
}