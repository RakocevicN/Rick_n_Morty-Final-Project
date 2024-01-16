# Test data providers for character ID tests.
# This data provider contains test data for character-related tests that require character IDs.
# It is a dictionary where each key represents a character ID.


# Positive test cases
positive_id_expected_data = {
    1: {
        'name': 'Rick Sanchez',
        'species': 'Human',
        'status': 'Alive',
        'type': '',
        'gender': 'Male'
    },
    2: {
        'name': 'Morty Smith',
        'species': 'Human',
        'status': 'Alive',
        'type': '',
        'gender': 'Male'
    },
    3: {
        'name': 'Summer Smith',
        'species': 'Human',
        'status': 'Alive',
        'type': '',
        'gender': 'Female'
    },

}


def generate_invalid_character_id_test_data():
    return negative_id_expected_data


# Negative test cases
negative_id_expected_data = {
    -1: "Character not found",
    -10: "Character not found",
    -100: "Character not found",
}
