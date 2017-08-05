import unittest
from db import count_game_kills
from db import get_players
from db import get_players_kills
from db import get_players_deaths_by_world
from db import get_kills


class TestQueriesMethods(unittest.TestCase):

    def setUp(self):
        self.game = {
            '_id': '5983c19b9d043c3b77e57de0',
            'game': 'game_x',
            'kills': [
                {'player_dead': 'Isgalamido',
                 'player_killer': '<world>',
                 'type_gun': 'MOD_TRIGGER_HURT'},
                {'player_dead': 'Isgalamido',
                 'player_killer': '<world>',
                 'type_gun': 'MOD_TRIGGER_HURT'},
                {'player_dead': 'Isgalamido',
                 'player_killer': '<world>',
                 'type_gun': 'MOD_TRIGGER_HURT'},
                {'player_dead': 'Mocinha',
                 'player_killer': 'Isgalamido',
                 'type_gun': 'MOD_ROCKET_SPLASH'},
                {'player_dead': 'Isgalamido',
                 'player_killer': 'Isgalamido',
                 'type_gun': 'MOD_ROCKET_SPLASH'}
                ]
        }

    def test_count_kills(self):
        self.assertEqual(count_game_kills(self.game), 5)

    def test_get_players(self):
        self.assertEqual(len(get_players(self.game)), 2)
        self.assertEqual(get_players(self.game), ['Isgalamido', 'Mocinha'])

    def test_get_all_kills_per_player(self):
        # test if get kill per player without <world>
        self.assertEqual(get_players_kills(self.game), {'Isgalamido': 2})

    def test_get_players_deaths_by_world(self):
        self.assertEqual(
            get_players_deaths_by_world(self.game), {'Isgalamido': 3})

    def test_get_kills(self):
        self.assertEqual(
            get_kills(self.game), {'Isgalamido': 0, 'Mocinha': 0})

if __name__ == '__main__':
    unittest.main()
