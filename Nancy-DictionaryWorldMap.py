world_map = {
    'WESTHOUSE': {
        'NAME': "West of House",
        'DESCRIPTION': "You are west of a white house",
        'PATHS': {
            'NORTH': 'NORTHHOUSE',
            'SOUTH': 'NORTHHOUSE'
        }
    },
    'NORTHHOUSE': {
        'NAME': "North of House",
        'DESCRIPTION': "Insert Description here",
        'PATHS': {
            'SOUTH': 'WESTHOUSE'
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