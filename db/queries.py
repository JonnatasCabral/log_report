from collections import Counter
from .utils import check_players_in_dict_of_kills
from .utils import check_negative_players

__all__ = [
    'count_game_kills', 'get_players', 'get_players_kills',
    'get_kills', 'get_players_deaths_by_world']


def count_game_kills(game):
    """
    Count kills in a match.
    """
    return len(game['kills'])


def get_players(game):
    """
    Get all players in a match.
    """
    players = []
    for kill in game['kills']:
        player_killer = kill['player_killer']
        player_dead = kill['player_dead']
        if player_killer not in players and player_killer != '<world>':
            players.append(player_killer)
        elif player_dead not in players and player_dead != '<world>':
            players.append(player_dead)
    return players


def get_players_kills(game):
    """
    Get all kills per player in a match.
    """

    players_kills = {}

    for kill in game['kills']:
        player_killer = kill['player_killer']
        if player_killer not in players_kills and player_killer != '<world>':
            players_kills[player_killer] = 1
        elif player_killer != '<world>':
            players_kills[player_killer] += 1
    return players_kills


def get_players_deaths_by_world(game):
    """
    Get all kills of <world> in a match.
    """
    players_deaths = {}
    for kill in game['kills']:
        player_killer = kill['player_killer']
        player_dead = kill['player_dead']
        if player_killer == '<world>':
            if player_dead not in players_deaths:
                players_deaths[player_dead] = 1
            else:
                players_deaths[player_dead] += 1
    return players_deaths


def get_kills(game):
    """
    Remove points from dead players by <world>.
    """
    kills = Counter(get_players_kills(game))
    deaths = Counter(get_players_deaths_by_world(game))
    kills.subtract(deaths)
    players_list = get_players(game)
    kills = check_players_in_dict_of_kills(players_list, kills)
    kills = check_negative_players(kills)
    return dict(kills)
