from typing import Tuple

import torch

from src.dataset.replay_data.sc2_replay_data import SC2ReplayData
from src.dataset.transforms.utils import average_player_stats


def economy_average_vs_outcome(
    sc2_replay: SC2ReplayData,
) -> Tuple[torch.Tensor, int]:
    """
    Transform that exposes logic for obtaining averaged economy statistics.

    :param sc2_replay: Specifies the parsed structure of a replay.
    :type sc2_replay: SC2ReplayData
    :return: Returns a tensor containing features and a target.
    :rtype: Tuple[torch.Tensor, torch.Tensor]
    """

    average_player_features = average_player_stats(
        player_tracker_events=sc2_replay.trackerEvents
    )
    feature_list = [
        player_features for player_features in average_player_features.values()
    ]

    # Creating feature tensor:
    feature_tensor = torch.tensor(feature_list, dtype=torch.float32)

    result_dict = {"Loss": 0, "Win": 1}
    target = result_dict[sc2_replay.toonPlayerDescMap[0].toon_player_info.result]

    return feature_tensor, target