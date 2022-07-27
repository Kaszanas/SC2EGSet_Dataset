import json
import tempfile
import unittest
from pathlib import Path
from typing import Tuple

from sc2egset_dataset.dataset.validators.multiprocess_validator import (
    validate_integrity_mp,
    validate_integrity_persist_mp,
)
from sc2egset_dataset.dataset.validators.singleprocess_validator import (
    validate_integrity_persist_sp,
    validate_integrity_sp,
)

import tests.test_utils.test_utils as test_utils


class IntegrityValidatorTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.not_working_test_replay = Path(
            test_utils.get_specific_asset(filename="test_bit_flip_example.json")
        ).as_posix()
        cls.working_test_replay = Path(
            test_utils.get_specific_asset(filename="test_replay.json")
        ).as_posix()
        cls.list_of_replays = [
            cls.working_test_replay,
            cls.not_working_test_replay,
        ]

    def test_singleprocess_integrity_validator(self):
        validated, skip_files = validate_integrity_sp(
            list_of_replays=self.list_of_replays
        )
        self.assertIsInstance(next(iter(skip_files)), str)
        self.assertEqual(len(validated), 1)
        self.assertEqual(len(skip_files), 1)

    def test_multiprocessing_integrity_validator(self):
        validated, skip_files = validate_integrity_mp(
            list_of_replays=self.list_of_replays, n_workers=2
        )
        self.assertIsInstance(next(iter(skip_files)), str)
        self.assertEqual(len(validated), 1)
        self.assertEqual(len(skip_files), 1)

    def test_persistent_mp_integrity_validator(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file_path = Path(temp_dir, "test_file.json")
            # This function should create a file containing persisted information
            # on validation:
            skip_files = validate_integrity_persist_mp(
                list_of_replays=self.list_of_replays,
                n_workers=2,
                validation_file_path=temp_file_path,
            )
            # The file that persists validation needs to be opened and assertions are made:
            with open(temp_file_path, mode="r") as tf:
                deserialized = json.load(tf)
                validated = deserialized["validated_files"]
                skipped = deserialized["skip_files"]
                self.assertEqual(len(validated), 1)
                self.assertEqual(len(skipped), 1)

        self.assertIsInstance(next(iter(skip_files)), str)
        self.assertEqual(len(skip_files), 1)

    def test_persistent_sp_integrity_validator(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file_path = Path(temp_dir, "test_file.json")

            # This function should create a file containing persisted information
            # on validation:
            skip_files = validate_integrity_persist_sp(
                list_of_replays=self.list_of_replays,
                validation_file_path=temp_file_path,
            )

            # The file that persists validation needs to be opened and assertions are made:
            with open(temp_file_path, mode="r") as tf:
                deserialized = json.load(tf)
                validated = deserialized["validated_files"]
                skipped = deserialized["skip_files"]
                self.assertEqual(len(validated), 1)
                self.assertEqual(len(skipped), 1)

        self.assertIsInstance(next(iter(skip_files)), str)
        self.assertEqual(len(skip_files), 1)

    def test_should_raise_exception_if_worker_less_equal_zero(self):
        with self.assertRaises(Exception) as e:
            validated_replays = validate_integrity_mp(
                list_of_replays=[
                    "./test/test_files/single_replay/test_replay.json",
                    "./test/test_files/single_replay/test_bit_flip_example.json"],
                n_workers=0)

        self.assertEqual(str(e.exception), "Number of workers cannot be equal or less than zero!")

    def test_should_set_a_set_if_empty_list_of_replays(self):
        # given
        validated_replays = validate_integrity_mp(
            list_of_replays=[],
            n_workers=1)
        # when
        # then
        assert(isinstance(validated_replays, Tuple))
