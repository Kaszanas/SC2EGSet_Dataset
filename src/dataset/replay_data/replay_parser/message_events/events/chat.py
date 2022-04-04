from typing import Dict

import torch
from src.dataset.replay_data.replay_parser.message_events.message_event import (
    MessageEvent,
)

# TODO: Docstrings


class Chat(MessageEvent):

    """
    _summary_

    :param id: _description_
    :type id: int
    :param loop: _description_
    :type loop: int
    :param recipient: _description_
    :type recipient: int
    :param string: _description_
    :type string: str
    :param userid: _description_
    :type userid: int
    """

    @staticmethod
    def from_dict(d: Dict) -> "Chat":
        """
        _summary_

        :param d: _description_
        :type d: Dict
        :return: _description_
        :rtype: Chat
        """
        return Chat(
            id=d["id"],
            loop=d["loop"],
            recipient=d["recipient"],
            string=d["string"],
            userid=d["userid"]["userId"],
        )

    def __init__(
        self,
        id: int,
        loop: int,
        recipient: int,
        string: str,
        userid: int,
    ) -> None:

        self.id = id
        self.loop = loop
        self.recipient = recipient
        self.string = string
        self.userid = userid

    def to_tensor(self) -> torch.Tensor:
        pass