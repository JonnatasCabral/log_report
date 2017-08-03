from ORM import MongoDB
from ORM import get_kills
from ORM import get_players
from ORM import count_game_kills
from collections import Counter


db = MongoDB(
    database_name='quake',
    collection_name='games'
)


def game_summary(game):
    return {
        'total_kills': count_game_kills(game),
        'players': get_players(game),
        'kills': get_kills(game)
    }


def players_ranking():
    ranking = Counter({})
    games_cursor = db.collection.find()
    for game in games_cursor:
        ranking += Counter(get_kills(game))

    ranking = dict(ranking)
    return ranking
