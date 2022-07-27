import os
import shutil
import unittest
from pathlib import Path

from sc2egset_dataset.dataset.pytorch_datasets.sc2_replaypack_dataset import (
    SC2ReplaypackDataset,
)
from sc2egset_dataset.dataset.replay_data.sc2_replay_data import SC2ReplayData
from sc2egset_dataset.dataset.utils.zip_utils import unpack_zipfile

from sc2egset_dataset.dataset.utils.download_utils import download_replaypack
from tests.settings_test import TEST_REPLAYPACKS
from tests.test_utils.test_utils import get_specific_asset, get_test_output_dir

# TODO: Rewrite or update these tests to better support validators:


class SC2ReplaypackDatasetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.test_replaypack_name = "2022_TestReplaypack"
        cls.replaypack_zip_path = get_specific_asset(
            filename=cls.test_replaypack_name + ".zip"
        )

        cls.test_output_path = get_test_output_dir()
        cls.unpack_dir_path = os.path.join(cls.test_output_path, "unpack")
        cls.download_dir_path = os.path.join(cls.test_output_path, "download")

        # Initializing the unpacked where it should be:
        cls.unpacked = Path(cls.unpack_dir_path, cls.test_replaypack_name)
        cls.download = Path(cls.download_dir_path, cls.test_replaypack_name)
        # If it doesn't exist, unpack the test .zip archive:
        if not cls.unpacked.exists():
            # Unpacks the replaypack that will be used for testing:
            cls.unpacked = Path(
                unpack_zipfile(
                    destination_dir=cls.unpack_dir_path,
                    subdir=cls.test_replaypack_name,
                    zip_path=cls.replaypack_zip_path,
                    n_workers=1,
                )
            )

    def setUp(self) -> None:

        if self.download.exists():
            shutil.rmtree(path=self.downloaded.as_posix())

        if self.unpacked.exists():
            shutil.rmtree(path=self.unpacked.as_posix())

    def test_unpack_replaypack(self):

        sc2_replaypack_dataset = SC2ReplaypackDataset(
            replaypack_name=self.test_replaypack_name,
            unpack_dir=self.unpack_dir_path,
            download_dir=self.download_dir_path,
        )

        # Replaypack was initialized:
        self.assertIsInstance(sc2_replaypack_dataset, SC2ReplaypackDataset)
        # Supplementary files were loaded properly:
        self.assertIsInstance(sc2_replaypack_dataset.replaypack_processed_failed, dict)
        self.assertIsInstance(sc2_replaypack_dataset.replaypack_dir_mapping, dict)
        self.assertIsInstance(sc2_replaypack_dataset.replaypack_summary, dict)

        # Files were properly indexed:
        self.assertNotEqual(len(sc2_replaypack_dataset), 0)
        # It is possible to retrieve a single file by index:
        self.assertIsInstance(sc2_replaypack_dataset[0], SC2ReplayData)

    def test_download_unpack_replaypack(self):

        sc2_replaypack_dataset = SC2ReplaypackDataset(
            replaypack_name=TEST_REPLAYPACKS[0][0],
            unpack_dir=self.unpack_dir_path,
            download_dir=self.download_dir_path,
            download=True,
            url=TEST_REPLAYPACKS[0][1],
        )

        # Replaypack was initialized:
        self.assertIsInstance(sc2_replaypack_dataset, SC2ReplaypackDataset)
        # Supplementary files were loaded properly:
        self.assertIsInstance(sc2_replaypack_dataset.replaypack_processed_failed, dict)
        self.assertIsInstance(sc2_replaypack_dataset.replaypack_dir_mapping, dict)
        self.assertIsInstance(sc2_replaypack_dataset.replaypack_summary, dict)

        # Files were properly indexed:
        self.assertNotEqual(len(sc2_replaypack_dataset), 0)
        # It is possible to retrieve a single file by index:
        self.assertIsInstance(sc2_replaypack_dataset[0], SC2ReplayData)

    def test_directory_not_exist_exception(self):
        with self.assertRaises(Exception) as e:
            sc2_replaypack_dataset = SC2ReplaypackDataset(
                replaypack_name=self.test_replaypack_name,
                unpack_dir="wrong",
                download_dir=self.download_dir_path
            )
        self.assertEqual(str(e.exception),"Replaypack unpack directory does not exist!")

    def test_url_not_set_exception(self):
        with self.assertRaises(Exception) as e:
            sc2_replaypack_dataset = SC2ReplaypackDataset(
                replaypack_name=TEST_REPLAYPACKS[0][0],
                unpack_dir=self.unpack_dir_path,
                download_dir=self.download_dir_path,
                download=True
            )
        self.assertEqual(str(e.exception),"Detected empty URL! Cannot download a replaypack!")