from collections import Counter


def count_game_kills(game):
    return len(game['kills'])


def get_players(game):
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

    players_kills = {}

    for kill in game['kills']:
        player_killer = kill['player_killer']
        if player_killer not in players_kills and player_killer != '<world>':
            players_kills[player_killer] = 1
        elif player_killer != '<world>':
            players_kills[player_killer] += 1
    return players_kills


def get_players_deaths_by_world(game):
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
    kills = Counter(get_players_kills(game))
    deaths = Counter(get_players_deaths_by_world(game))
    return dict(kills - deaths)

