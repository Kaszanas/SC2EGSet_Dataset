import unittest

from sc2egset_dataset.dataset.replay_data.sc2_replay_data import SC2ReplayData
import tests.test_utils.test_utils as test_utils

"""
    **Incorrect Usage Examples:**

    Providing incorrect path to some ``replay.json`` file will result
    in failure to parse which can be seen as below:

    >>> replay_data = SC2ReplayData.from_file("file_doesnt_exist.json")
    Traceback (most recent call last):
    ...
    FileNotFoundError: [Errno 2] No such file or directory: 'file_doesnt_exist.json'
"""


class SC2ReplayDataTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.test_replay = test_utils.get_specific_asset(filename="test_replay.json")

    def test_loading_json(self):

        sc2_replay_data = SC2ReplayData.from_file(replay_filepath=self.test_replay)
        self.assertIsInstance(sc2_replay_data, SC2ReplayData)

    def test_empty_json(self):

        # Empty json should raise a KeyError:
        with self.assertRaises(KeyError):
            _ = SC2ReplayData(loaded_replay_object={})
