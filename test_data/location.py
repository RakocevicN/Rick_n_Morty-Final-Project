"""
Test data for location tests.
This data includes positive test cases for location tests.
The data is organized as a dictionary, where each key represents a location name.
"""
import allure
from api_file.main_apis import get_all_locations

locations_response = get_all_locations()


@allure.step("Get test case data")
def get_test_case_data(test_case_name, data_from_dic):
    """
        Get test case data for a given test case name from a data dictionary and returns
        test case id and ID DATA
        Parametars:
            test_case_name (str)
            data_from_dic (dict): test case data
        """

    location_id = data_from_dic[test_case_name]['id']
    location_data = data_from_dic[test_case_name]['data']
    allure.attach("Test Case name", test_case_name, allure.attachment_type.TEXT)
    allure.attach("Location ID", str(location_id), allure.attachment_type.TEXT)
    allure.attach("Location Data", str(location_data), allure.attachment_type.JSON)
    return location_id, location_data


location_expected_data = {
    'Earth (C-137)': {
        'id': 1,
        'data': {
            'id': 1,
            'name': 'Earth (C-137)',
            'type': 'Planet',
            'dimension': 'Dimension C-137'
        }
    },
    'Abadango': {
        'id': 2,
        'data': {
            'id': 2,
            'name': 'Abadango',
            'type': 'Cluster',
            'dimension': 'unknown'
        }
    },
    'Citadel of Ricks': {
        'id': 3,
        'data': {
            'id': 3,
            'name': 'Citadel of Ricks',
            'type': 'Space station',
            'dimension': 'unknown'
        }
    },
    "Worldender's lair": {
        'id': 4,
        'data': {
            'id': 4,
            'name': "Worldender's lair",
            'type': 'Planet',
            'dimension': 'unknown'
        }
    },
    'Anatomy Park': {
        'id': 5,
        'data': {
            'id': 5,
            'name': 'Anatomy Park',
            'type': 'Microverse',
            'dimension': 'Dimension C-137'
        }
    },
    'Interdimensional Cable': {
        'id': 6,
        'data': {
            'id': 6,
            'name': 'Interdimensional Cable',
            'type': 'TV',
            'dimension': 'unknown'
        }
    },
    'Immortality Field Resort': {
        'id': 7,
        'data': {
            'id': 7,
            'name': 'Immortality Field Resort',
            'type': 'Resort',
            'dimension': 'unknown'
        }
    },
    'Post-Apocalyptic Earth': {
        'id': 8,
        'data': {
            'id': 8,
            'name': 'Post-Apocalyptic Earth',
            'type': 'Planet',
            'dimension': 'Post-Apocalyptic Dimension'
        }
    },
    'Purge Planet': {
        'id': 9,
        'data': {
            'id': 9,
            'name': 'Purge Planet',
            'type': 'Planet',
            'dimension': 'Replacement Dimension'
        }
    },
    'Venzenulon 7': {
        'id': 10,
        'data': {
            'id': 10,
            'name': 'Venzenulon 7',
            'type': 'Planet',
            'dimension': 'unknown'
        }
    },
    'Bepis 9': {
        'id': 11,
        'data': {
            'id': 11,
            'name': 'Bepis 9',
            'type': 'Planet',
            'dimension': 'unknown'
        }
    },
    'Cronenberg Earth': {
        'id': 12,
        'data': {
            'id': 12,
            'name': 'Cronenberg Earth',
            'type': 'Planet',
            'dimension': 'Cronenberg Dimension'
        }
    },
    'Nuptia 4': {
        'id': 13,
        'data': {
            'id': 13,
            'name': 'Nuptia 4',
            'type': 'Planet',
            'dimension': 'unknown'
        }
    },
    "Giant's Town": {
        'id': 14,
        'data': {
            'id': 14,
            'name': "Giant's Town",
            'type': 'Fantasy town',
            'dimension': 'Fantasy Dimension'
        }
    },
    'Bird World': {
        'id': 15,
        'data': {
            'id': 15,
            'name': 'Bird World',
            'type': 'Planet',
            'dimension': 'unknown'
        }
    },
    'St. Gloopy Noops Hospital': {
        'id': 16,
        'data': {
            'id': 16,
            'name': 'St. Gloopy Noops Hospital',
            'type': 'Space station',
            'dimension': 'unknown'
        }
    },
    'Earth (5-126)': {
        'id': 17,
        'data': {
            'id': 17,
            'name': 'Earth (5-126)',
            'type': 'Planet',
            'dimension': 'Dimension 5-126'
        }
    },
    "Mr. Goldenfold's dream": {
        'id': 18,
        'data': {
            'id': 18,
            'name': "Mr. Goldenfold's dream",
            'type': 'Dream',
            'dimension': 'Dimension C-137'
        }
    },
    'Gromflom Prime': {
        'id': 19,
        'data': {
            'id': 19,
            'name': 'Gromflom Prime',
            'type': 'Planet',
            'dimension': 'Replacement Dimension'
        }
    },
    'Earth (Replacement Dimension)': {
        'id': 20,
        'data': {
            'id': 20,
            'name': 'Earth (Replacement Dimension)',
            'type': 'Planet',
            'dimension': 'Replacement Dimension'
        }
    },
}
