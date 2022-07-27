import unittest

from sc2egset_dataset.dataset.replay_data.replay_parser.details.details import Details
"""
    **Incorrect Usage Examples:**

    Passing a Python dictionary with missing or incorrect
    fields would result in a failure as follows:

    >>> details_dict = {"WRONG_FIELD": "Faster"}
    >>> details_object = Details.from_dict(d=details_dict)
    Traceback (most recent call last):
    ...
    KeyError: 'gameSpeed'
"""
class TestDetails(unittest.TestCase):

    def test_from_dict_correct(self):
        #given
        details_dict = {"gameSpeed": "Faster",
                        "isBlizzardMap": True,
                        "timeUTC": "2017-04-29T05:15:32.4903483+02:00"
                        }
        #when
        details_object = Details.from_dict(d=details_dict)
        # then
        self.assertTrue(details_object)

    def test_from_dict_incorrect_parameter(self):
        #given
        details_dict = {
                        "gameSpeed": "Fasterrr",
                        "isBlizzardMap": True,
                        "timeUTC": "2017-04-29T05:15:32.4903483+02:00"
                        }
        #when
        details_object = Details.from_dict(d=details_dict)
        #then
        self.assertRaises(TypeError,details_object)