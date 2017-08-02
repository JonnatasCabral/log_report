from ORM import MongoDB
from ORM import get_players
from ORM import count_game_kills


db = MongoDB(
    database_name='quake',
    collection_name='games'
)
db.collection.find()


def game_summary(game):
    return {
        'total_kills': count_game_kills(game),
        'players': get_players(game)
    }
