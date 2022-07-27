import logging
import os
import shutil
import unittest
import zipfile
from pathlib import Path

from sc2egset_dataset.dataset.utils.zip_utils import unpack_chunk, unpack_zipfile

from tests.test_utils.test_utils import get_specific_asset, get_test_output_dir

"""
    **Incorrect Usage Examples:**

    >>> wrong_type_object = int(2)
    >>> unpack_chunk_object = unpack_chunk(
    ... zip_path=wrong_type_object,
    ... filenames="./directory/filenames",
    ... path_to_extract="./directory/path_to_extract")
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) ...

    If you don't set parameters or paste incorect parameters' type.

    **Incorrect Usage Examples:**

    Setting number of workers to zero or less than zero will result in failure.

    >>> unpack_zipfile_object = unpack_zipfile(
    ... destination_dir="./directory/destination_dir",
    ... subdir="./directory/subdir",)
    ... zip_path="./directory/zip_path",)
    ... n_workers=0)
    Traceback (most recent call last):
    ...
    Exception: Number of workers cannot be equal or less than zero!
"""


class ZipUtilsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:

        cls.test_replaypack_name = "2022_TestReplaypack"
        cls.replaypack_zip_path = get_specific_asset(
            filename=cls.test_replaypack_name + ".zip"
        )

        cls.test_output_path = get_test_output_dir()
        cls.unpack_dir_path = os.path.join(cls.test_output_path, "unpack")

        cls.unpacked = Path("not_existing_path")

    def setUp(self) -> None:
        if self.unpacked.exists():
            shutil.rmtree(path=self.unpacked.as_posix())

    def test_unpack_zipfile_correct(self):

        path_to_unpacked = unpack_zipfile(
            destination_dir=self.unpack_dir_path,
            subdir=self.test_replaypack_name,
            zip_path=self.replaypack_zip_path,
            n_workers=1,
        )
        self.unpacked = Path(path_to_unpacked)

    def test_unpack_zipfile_incorrect(self):
        parameters = [-1, 0]
        for n_workers in parameters:
            with self.subTest(n_workers):
                with self.assertRaises(Exception):
                    _ = unpack_zipfile(
                        destination_dir=self.unpack_dir_path,
                        subdir=self.test_replaypack_name,
                        zip_path=self.replaypack_zip_path,
                        n_workers=n_workers,
                    )

    def test_unpack_chunk_correct(self):

        with zipfile.ZipFile(self.replaypack_zip_path, "r") as zip_file:
            file_list = zip_file.namelist()

        extraction_path = Path(
            os.path.join(self.unpack_dir_path, self.test_replaypack_name)
        )
        if not extraction_path.exists():
            extraction_path.mkdir()

        self.unpacked = extraction_path.as_posix()

        unpack_chunk(
            zip_path=self.replaypack_zip_path,
            filenames=file_list,
            path_to_extract=extraction_path.as_posix(),
        )

    def test_unpack_chunk_should_throw_zipfile_error(self):
        # given
        with zipfile.ZipFile(self.replaypack_zip_path, "r") as zip_file:
            file_list = zip_file.namelist()

        extraction_path = Path(
            os.path.join(self.unpack_dir_path, self.test_replaypack_name)
        )
        if not extraction_path.exists():
            extraction_path.mkdir()
        self.unpacked = extraction_path.as_posix()

        # when
        # then
        with self.assertRaises(Exception) as e:
            unpack_chunk(
                zip_path=self.replaypack_zip_path,
                filenames=file_list,
                path_to_extract=1
            )

