"""
Test data providers for character ID tests.
This data providers contains test data for character-related tests that require character IDs.
It is a dictionary where each key represents a character ID
"""


def get_test_case_data(test_case_name, data_from_dic):
    character_id = data_from_dic[test_case_name]['id']
    character_data = data_from_dic[test_case_name]['data']
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
    },

    'BethSmith': {
        'id': 4,
        'data': {
            'id': 4,
            'name': 'Beth Smith',
            'species': 'Human',
            'status': 'Alive',
            'type': '',
            'gender': 'Female'
        }
    },

    'JerrySmith': {
        'id': 5,
        'data': {
            'id': 5,
            'name': 'Jerry Smith',
            'species': 'Human',
            'status': 'Alive',
            'type': '',
            'gender': 'Male'
        }
    },

    'AbadangoClusterPrincess': {
        'id': 6,
        'data': {
            'id': 6,
            'name': 'Abadango Cluster Princess',
            'species': 'Alien',
            'status': 'Alive',
            'type': '',
            'gender': 'Female'
        }
    },

    'AbradolfLincler': {
        'id': 7,
        'data': {
            'id': 7,
            'name': 'Abradolf Lincler',
            'species': 'Human',
            'status': 'unknown',
            'type': 'Genetic experiment',
            'gender': 'Male'
        }
    },

    'AdjudicatorRick': {
        'id': 8,
        'data': {
            'id': 8,
            'name': 'Adjudicator Rick',
            'species': 'Human',
            'status': 'Dead',
            'type': '',
            'gender': 'Male'
        }
    },

    'AgencyDirector': {
        'id': 9,
        'data': {
            'id': 9,
            'name': 'Agency Director',
            'species': 'Human',
            'status': 'Dead',
            'type': '',
            'gender': 'Male'
        }
    },

    'AlanRails': {
        'id': 10,
        'data': {
            'id': 10,
            'name': 'Alan Rails',
            'species': 'Human',
            'status': 'Dead',
            'type': 'Superhuman (Ghost trains summoner)',
            'gender': 'Male'
        }
    },

    'AlbertEinstein': {
        'id': 11,
        'data': {
            'id': 11,
            'name': 'Albert Einstein',
            'species': 'Human',
            'status': 'Dead',
            'type': '',
            'gender': 'Male'
        }
    },

    'Alexander': {
        'id': 12,
        'data': {
            'id': 12,
            'name': 'Alexander',
            'species': 'Human',
            'status': 'Dead',
            'type': '',
            'gender': 'Male'
        }
    },

    'AlienGoogah': {
        'id': 13,
        'data': {
            'id': 13,
            'name': 'Alien Googah',
            'species': 'Alien',
            'status': 'unknown',
            'type': '',
            'gender': 'unknown'
        }
    },

    'AlienMorty': {
        'id': 14,
        'data': {
            'id': 14,
            'name': 'Alien Morty',
            'species': 'Alien',
            'status': 'unknown',
            'type': '',
            'gender': 'Male'
        }
    },

    'AlienRick': {
        'id': 15,
        'data': {
            'id': 15,
            'name': 'Alien Rick',
            'species': 'Alien',
            'status': 'unknown',
            'type': '',
            'gender': 'Male'
        }
    },

    'AmishCyborg': {
        'id': 16,
        'data': {
            'id': 16,
            'name': 'Amish Cyborg',
            'species': 'Alien',
            'status': 'Dead',
            'type': 'Parasite',
            'gender': 'Male'
        }
    },

    'Annie': {
        'id': 17,
        'data': {
            'id': 17,
            'name': 'Annie',
            'species': 'Human',
            'status': 'Alive',
            'type': '',
            'gender': 'Female'
        }
    },
    'AntennaMorty': {
        'id': 18,
        'data': {
            'id': 18,
            'name': 'Antenna Morty',
            'species': 'Human',
            'status': 'Alive',
            'type': 'Human with antennae',
            'gender': 'Male'
        }
    },

    'AntennaRick': {
        'id': 19,
        'data': {
            'id': 19,
            'name': 'Antenna Rick',
            'species': 'Human',
            'status': 'unknown',
            'type': 'Human with antennae',
            'gender': 'Male'
        }
    },

    'AntsInMyEyesJohnson': {
        'id': 20,
        'data': {
            'id': 20,
            'name': 'Ants in my Eyes Johnson',
            'species': 'Human',
            'status': 'unknown',
            'type': 'Human with ants in his eyes',
            'gender': 'Male'
        }
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
