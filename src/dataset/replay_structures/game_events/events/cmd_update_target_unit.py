from src.dataset.replay_structures.game_events.events.nested.target_unit import (
    TargetUnit,
)


class CmdUpdateTargetUnit:

    """_summary_

    :param id: _description_
    :type id: int
    :param loop: _description_
    :type loop: int
    :param target: _description_
    :type target: TargetUnit
    :param userid: _description_
    :type userid: int
    """

    def __init__(
        self,
        id: int,
        loop: int,
        target: TargetUnit,
        userid: int,
    ) -> None:

        self.id = id
        self.loop = loop
        self.target = target
        self.userid = userid