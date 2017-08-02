def count_game_kills(game):
    return len(game['kills'])


def get_players(game):
    players = []
    for kill in game['kills']:
        player_killer = kill['player_killer']
        player_dead = kill['player_dead']
        if player_killer not in players:
            players.append(player_killer)
        elif player_dead not in players:
            players.append(player_dead)
    return players


def get_players_kills(game):

    players_kills = {}

    for kill in game['kills']:
        player_killer = kill['player_killer']
        if player_killer not in players_kills:
            players_kills[player_killer] = 1
        else:
            players_kills[player_killer] += 1
    return players_kills


def get_players_deads(game):
    players_deads = {}
    for kill in game['kills']:
        player_dead = kill['player_dead']
        if player_dead not in players_deads:
            players_deads[player_dead] = 1
        else:
            players_deads[player_dead] += 1
    return players_deads
