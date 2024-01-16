"""
Needs to be updated

"""

from rick_n_morty import get_all_locations

locations_response = get_all_locations()

location_expected_data = {

    1: {
        'id': 1,
        'name': 'Earth (C-137)',
        'type': 'Planet',
        'dimension': 'Dimension C-137'
    },
    2: {
        'id': 2,
        'name': 'Abadango',
        'type': 'Cluster',
        'dimension': 'unknown'
    },
    3: {
        'id': 3,
        'name': 'Citadel of Ricks',
        'type': 'Space station',
        'dimension': 'unknown'
    }
}
