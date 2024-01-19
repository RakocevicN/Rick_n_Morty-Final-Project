"""
This file provides data related to episodes, specifically
designed for testing purposes involving episodes.
Episode data provider dictionary contains detailed information about each episode
"""


def get_test_case_data(test_case_name, data_from_dic):
    episode_id = data_from_dic[test_case_name]['id']
    episode_data = data_from_dic[test_case_name]['data']
    return episode_id, episode_data


episode_expected_data = {
    'Pilot': {
        'id': 1,
        'data': {
            'id': 1,
            'name': 'Pilot',
            'air_date': 'December 2, 2013',
            'episode': 'S01E01',
        }
    },
    'Lawnmower Dog': {
        'id': 2,
        'data': {
            'id': 2,
            'name': 'Lawnmower Dog',
            'air_date': 'December 9, 2013',
            'episode': 'S01E02'
        }
    },
    'Anatomy Park': {
        'id': 3,
        'data': {
            'id': 3,
            'name': 'Anatomy Park',
            'air_date': 'December 16, 2013',
            'episode': 'S01E03'
        }
    },
    'M. Night Shaym-Aliens!': {
        'id': 4,
        'data': {
            'id': 4,
            'name': 'M. Night Shaym-Aliens!',
            'air_date': 'January 13, 2014',
            'episode': 'S01E04'
        }
    },
    'Meeseeks and Destroy': {
        'id': 5,
        'data': {
            'id': 5,
            'name': 'Meeseeks and Destroy',
            'air_date': 'January 20, 2014',
            'episode': 'S01E05'
        }
    },
    'Rick Potion #9': {
        'id': 6,
        'data': {
            'id': 6,
            'name': 'Rick Potion #9',
            'air_date': 'January 27, 2014',
            'episode': 'S01E06'
        }
    },
    'Raising Gazorpazorp': {
        'id': 7,
        'data': {
            'id': 7,
            'name': 'Raising Gazorpazorp',
            'air_date': 'March 10, 2014',
            'episode': 'S01E07'
        }
    },
    'Rixty Minutes': {
        'id': 8,
        'data': {
            'id': 8,
            'name': 'Rixty Minutes',
            'air_date': 'March 17, 2014',
            'episode': 'S01E08'
        }
    },
    'Something Ricked This Way Comes': {
        'id': 9,
        'data': {
            'id': 9,
            'name': 'Something Ricked This Way Comes',
            'air_date': 'March 24, 2014',
            'episode': 'S01E09'
        }
    },
    'Close Rick-counters of the Rick Kind': {
        'id': 10,
        'data': {
            'id': 10,
            'name': 'Close Rick-counters of the Rick Kind',
            'air_date': 'April 7, 2014',
            'episode': 'S01E10'
        }
    },
    'Ricksy Business': {
        'id': 11,
        'data': {
            'id': 11,
            'name': 'Ricksy Business',
            'air_date': 'April 14, 2014',
            'episode': 'S01E11'
        }
    },
    'A Rickle in Time': {
        'id': 12,
        'data': {
            'id': 12,
            'name': 'A Rickle in Time',
            'air_date': 'July 26, 2015',
            'episode': 'S02E01'
        }
    },
    'Mortynight Run': {
        'id': 13,
        'data': {
            'id': 13,
            'name': 'Mortynight Run',
            'air_date': 'August 2, 2015',
            'episode': 'S02E02'
        }
    },
    'Auto Erotic Assimilation': {
        'id': 14,
        'data': {
            'id': 14,
            'name': 'Auto Erotic Assimilation',
            'air_date': 'August 9, 2015',
            'episode': 'S02E03'
        }
    },
    'Total Rickall': {
        'id': 15,
        'data': {
            'id': 15,
            'name': 'Total Rickall',
            'air_date': 'August 16, 2015',
            'episode': 'S02E04'
        }
    },
    'Get Schwifty': {
        'id': 16,
        'data': {
            'id': 16,
            'name': 'Get Schwifty',
            'air_date': 'August 23, 2015',
            'episode': 'S02E05'
        }
    },
    'The Ricks Must Be Crazy': {
        'id': 17,
        'data': {
            'id': 17,
            'name': 'The Ricks Must Be Crazy',
            'air_date': 'August 30, 2015',
            'episode': 'S02E06'
        }
    },
    'Big Trouble in Little Sanchez': {
        'id': 18,
        'data': {
            'id': 18,
            'name': 'Big Trouble in Little Sanchez',
            'air_date': 'September 13, 2015',
            'episode': 'S02E07'
        }
    },
    'Interdimensional Cable 2: Tempting Fate': {
        'id': 19,
        'data': {
            'id': 19,
            'name': 'Interdimensional Cable 2: Tempting Fate',
            'air_date': 'September 20, 2015',
            'episode': 'S02E08'
        }
    },
    "Look Who's Purging Now": {
        'id': 20,
        'data': {
            'id': 20,
            'name': "Look Who's Purging Now",
            'air_date': 'September 27, 2015',
            'episode': 'S02E09'
        }
    },
}
