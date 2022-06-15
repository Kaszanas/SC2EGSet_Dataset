import json
import unittest
<<<<<<< HEAD
from src.dataset.replay_data.replay_parser.game_events.game_event import GameEvent
from src.dataset.replay_data.replay_parser.game_events.game_events_parser import (
=======
from src.dataset.replay_structures.game_events.game_event import GameEvent
from src.dataset.replay_structures.game_events.game_events_parser import (
>>>>>>> 1.0.0
    GameEventsParser,
)

import test.test_utils.test_utils as test_utils


class GameEventsParserTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.test_replay = test_utils.get_specific_asset(filename="test_replay.json")

    def test_game_events_parser(self):
        with open(self.test_replay) as f:
            loaded_file = json.load(f)

            # Iterating over all of the game events and verifying
            # If the parsing works correctly:
            for game_event in loaded_file["gameEvents"]:
                some_parsed_event = GameEventsParser.from_dict(d=game_event)
                self.assertIsInstance(some_parsed_event, GameEvent)
