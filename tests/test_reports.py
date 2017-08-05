import unittest
from reports import get_game_summary


class TestReportsMethods(unittest.TestCase):

    def setUp(self):
        self.game = {
            '_id': '5983c19b9d043c3b77e57de0',
            'game': 'game_x',
            'kills': [
                {'player_dead': 'Isgalamido',
                 'player_killer': 'Mocinha',
                 'type_gun': 'MOD_TRIGGER_HURT'},
                {'player_dead': 'Isgalamido',
                 'player_killer': '<world>',
                 'type_gun': 'MOD_TRIGGER_HURT'},
                {'player_dead': 'Isgalamido',
                 'player_killer': 'Mocinha',
                 'type_gun': 'MOD_TRIGGER_HURT'},
                {'player_dead': 'Mocinha',
                 'player_killer': 'Isgalamido',
                 'type_gun': 'MOD_ROCKET_SPLASH'},
                {'player_dead': 'Isgalamido',
                 'player_killer': 'Isgalamido',
                 'type_gun': 'MOD_ROCKET_SPLASH'}
                ]
        }

    def test_get_summary(self):
        summary = get_game_summary(self.game)
        self.assertEqual(summary['total_kills'], 5)
        self.assertEqual(summary['players'], ['Mocinha', 'Isgalamido'])
        self.assertEqual(summary['kills'], {'Isgalamido': 1, 'Mocinha': 2})
