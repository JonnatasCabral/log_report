import re
from patterns import KILL_PATTERN
from patterns import END_GAME
from enums import GroupPattern
from .db import MongoDB


def export_quake_log(file, pattern):
    db = MongoDB(
        database_name='quake',
        collection_name='games'
    )

    game_count = 0
    game_name = 'game_{}'.format(game_count)
    game = {
        'game': game_name,
        'kills': []
    }
    with open(file, "r") as f:
        for row in f:
            if 'Kill:' in row:
                regex_groups = re.search(pattern, row).groups()
                kill_row = {
                    'player_killer': regex_groups[GroupPattern.PLAYER_KILLER.value],
                    'player_dead': regex_groups[GroupPattern.PLAYER_DEAD.value],
                    'type_gun': regex_groups[GroupPattern.TYPE_GUN.value]
                }
                game['kills'].append(kill_row)
            elif END_GAME in row:
                db.save(game)
                game_count += 1
                game_name = 'game_{}'.format(game_count)
                game = {
                    'game': game_name,
                    'kills': []
                }

file = '2-games.txt'
export_quake_log(file, KILL_PATTERN)
