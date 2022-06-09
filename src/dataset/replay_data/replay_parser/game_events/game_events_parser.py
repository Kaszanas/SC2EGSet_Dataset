#  { event["evtTypeName"] for event in json_obj["gameEvents"]}
#
# event_type_to_example = {}
# for event in json_obj["gameEvents"]:
#     if event["evtTypeName"] not in event_type_to_example:
#         event_type_to_example[event["evtTypeName"]] = event


# Abstract game event type. Needs to support at least the following:
# {'UserOptions', 'CameraUpdate', 'ControlGroupUpdate', 'GameUserLeave', 'CommandManagerState', 'CameraSave', 'CmdUpdateTargetPoint', 'CmdUpdateTargetUnit', 'Cmd', 'SelectionDelta'}
from typing import Dict

from src.dataset.replay_data.replay_parser.game_events.events.camera_save import (
    CameraSave,
)
from src.dataset.replay_data.replay_parser.game_events.events.camera_update import (
    CameraUpdate,
)
from src.dataset.replay_data.replay_parser.game_events.events.cmd import Cmd
from src.dataset.replay_data.replay_parser.game_events.events.cmd_update_target_point import (
    CmdUpdateTargetPoint,
)
from src.dataset.replay_data.replay_parser.game_events.events.cmd_update_target_unit import (
    CmdUpdateTargetUnit,
)
from src.dataset.replay_data.replay_parser.game_events.events.command_manager_state import (
    CommandManagerState,
)
from src.dataset.replay_data.replay_parser.game_events.events.control_group_update import (
    ControlGroupUpdate,
)
from src.dataset.replay_data.replay_parser.game_events.events.game_user_leave import (
    GameUserLeave,
)
from src.dataset.replay_data.replay_parser.game_events.events.selection_delta import (
    SelectionDelta,
)
from src.dataset.replay_data.replay_parser.game_events.events.user_options import (
    UserOptions,
)
from src.dataset.replay_data.replay_parser.game_events.game_event import GameEvent


class GameEventsParser:
    @staticmethod
    def from_dict(d: Dict) -> GameEvent:
        """
        Static method returning initialized GameEvent class from a dictionary. This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file that is a result of pre-processing some .SC2Replay file.
        :type d: Dict
        :return: Returns an initialized GameEvent class.
        :rtype: GameEvent
        """
        type_name = d["evtTypeName"]

        match type_name:
            case CameraSave.__name__:
                return CameraSave.from_dict(d=d)
            case CameraUpdate.__name__:
                return CameraUpdate.from_dict(d=d)
            case CmdUpdateTargetPoint.__name__:
                return CmdUpdateTargetPoint.from_dict(d=d)
            case CmdUpdateTargetUnit.__name__:
                return CmdUpdateTargetUnit.from_dict(d=d)
            case Cmd.__name__:
                return Cmd.from_dict(d=d)
            case CommandManagerState.__name__:
                return CommandManagerState.from_dict(d=d)
            case ControlGroupUpdate.__name__:
                return ControlGroupUpdate.from_dict(d=d)
            case GameUserLeave.__name__:
                return GameUserLeave.from_dict(d=d)
            case SelectionDelta.__name__:
                return SelectionDelta.from_dict(d=d)
            case UserOptions.__name__:
                return UserOptions.from_dict(d=d)
