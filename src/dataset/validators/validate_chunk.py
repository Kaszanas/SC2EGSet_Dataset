from typing import List, Tuple

from src.dataset.replay_data.sc2_replay_data import SC2ReplayData


# TODO: Verify if it is possible to return two sets:
def validate_chunk(
    list_of_replays: List[str],
) -> List[Tuple[str, bool]]:
    """
    Attempts to parse a chunk of replays and validates the JSON structure using SC2ReplayData parser.

    :param list_of_replays: Specifies the list of replays that will be validated.
    :type list_of_replays: List[str]
    :return: Returns a tuple of SC2ReplayFile info and a boolean denoting if the file should be skipped in final processing.
    :rtype: List[Tuple[str, bool]]
    """

    result = []

    for file_path in list_of_replays:
        try:
            replay_data = SC2ReplayData.from_file(replay_filepath=file_path)
            result.append((file_path, True))
        except:
            result.append((file_path, False))

    return result