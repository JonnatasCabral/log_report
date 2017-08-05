def check_players_in_dict_of_kills(player_list, dict_kills):
    for player in player_list:
        if not dict_kills.get(player):
            dict_kills[player] = 0
    return dict_kills


def check_negative_players(dict_kills):
    for key, value in dict_kills.items():
        if value < 0:
            dict_kills[key] = 0
    return dict_kills


# def remove_world(dict_kills):
#     if '<world>' in dict_kills:
#         dict_kills.pop('<world>')
#     return dict_kills
