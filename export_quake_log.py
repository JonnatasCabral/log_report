import re
from patterns import KILL_PATTERN
from patterns import INIT_GAME
from enums import GroupPattern
from db import MongoDB


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
        started_game = False
        for row in f:
            if INIT_GAME in row and started_game:
                db.save(game)
                game_count += 1
                game_name = 'game_{}'.format(game_count)
                game = {
                    'game': game_name,
                    'kills': []
                }
            if INIT_GAME in row:
                started_game = True
            if 'Kill:' in row and started_game:
                regex_groups = re.search(pattern, row).groups()
                kill_row = {
                    'player_killer': regex_groups[GroupPattern.PLAYER_KILLER.value],
                    'player_dead': regex_groups[GroupPattern.PLAYER_DEAD.value],
                    'type_gun': regex_groups[GroupPattern.TYPE_GUN.value]
                }
                game['kills'].append(kill_row)
        db.save(game)

file = '2-games.txt'
export_quake_log(file, KILL_PATTERN)
