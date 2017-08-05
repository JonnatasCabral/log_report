import sys
sys.path.insert(0, '..')
from log_report.db import MongoDB
from log_report.db import get_kills
from log_report.db import get_players
from collections import Counter
from log_report.db import count_game_kills
import operator
import pymongo


def get_game_summary(game):
    return {
        'total_kills': count_game_kills(game),
        'players': get_players(game),
        'kills': get_kills(game)
    }


def get_players_ranking(db):
    ranking = Counter({})
    games_cursor = db.collection.find()
    for game in games_cursor:
        ranking += Counter(get_kills(game))
    ranking = dict(ranking)
    # sort ranking by value dict and return list of tuples ascending order
    sorted_ranking = sorted(ranking.items(), key=operator.itemgetter(1))
    # return opposite of list : descending ascending
    return sorted_ranking[::-1]


def get_all_games_summary(db):
    games_summary = {}
    games_cursor = db.collection.find()
    for game in games_cursor:
        games_summary[game['game']] = get_game_summary(game)
    return games_summary


if __name__ == '__main__':
    db = MongoDB(
        database_name='quake',
        collection_name='games'
        )
    print(get_all_games_summary(db))
