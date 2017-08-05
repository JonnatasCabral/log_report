import unittest
from db.utils import check_players_in_dict_of_kills
from db import get_players_deaths_by_world
from db import get_players_kills
from db import get_players
from collections import Counter


class TestutilsMethods(unittest.TestCase):

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
        self.player_deaths_by_world = Counter(get_players_deaths_by_world(
            self.game))
        self.dict_kills = Counter(get_players_kills(self.game))
        self.dict_kills.subtract(self.player_deaths_by_world)
        self.players = get_players(self.game)

    def test_check_players_in_dict_of_kills(self):
        current_dict = dict(self.dict_kills)
        self.assertEqual(current_dict, {'Isgalamido': -1})
        updated_dict = dict(
            check_players_in_dict_of_kills(self.players, self.dict_kills))
        self.assertEqual(updated_dict, {'Mocinha': 0, 'Isgalamido': -1})

if __name__ == '__main__':
    unittest.main()
