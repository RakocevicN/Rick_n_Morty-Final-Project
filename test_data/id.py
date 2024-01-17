"""
Test data providers for character ID tests.
This data providers contains test data for character-related tests that require character IDs.
It is a dictionary where each key represents a character ID
"""


def get_test_case_data(test_case_name, data_dict):
    character_id = data_dict[test_case_name]['id']
    character_data = data_dict[test_case_name]['data']
    return character_id, character_data


# Positive test cases
id_positive_expected_data = {
    'RickSanchez': {
        'id': 1,
        'data': {
            'id': 1,
            'name': 'Rick Sanchez',
            'species': 'Human',
            'status': 'Alive',
            'type': '',
            'gender': 'Male'
        }
    },
    'MortySmith': {
        'id': 2,
        'data': {
            'id': 2,
            'name': 'Morty Smith',
            'species': 'Human',
            'status': 'Alive',
            'type': '',
            'gender': 'Male'
        }
    },
    'SummerSmith': {
        'id': 3,
        'data': {
            'id': 3,
            'name': 'Summer Smith',
            'species': 'Human',
            'status': 'Alive',
            'type': '',
            'gender': 'Female'
        }
    }
}


def generate_invalid_character_id_test_data():
    return negative_id_expected_data


# Negative test cases
negative_id_expected_data = {
    -1: "Character not found",
    -10: "Character not found",
    -100: "Character not found",
}
