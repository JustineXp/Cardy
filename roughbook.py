# played_card = {'name': 'J', 'type': 'Flowers'}

# possible_cards = [
#     card for card in cards if card['type'] == played_card['type'] or card['name'] == played_card['name']]

# grouped_possible_cards = [{'same_name_cards': [
#     card for card in possible_cards if played_card['name'] == card['name']], 'same_type_cards': [card for card in possible_cards if played_card['type'] == card['type']]}]

# # print(grouped_possible_cards['same_name_cards'])

# grouped = grouped_possible_cards[0]

# print(grouped)

# print(grouped['same_name_cards'])
# print(grouped['same_type_cards'])

# import random
# player_decks = []
# decks = []
# rotation_list = list(range(1, 5))
# random.shuffle(rotation_list)

# for player in range(4):
#     decks.append(
#         {'player': player, 'deck': [], 'rotation_number': rotation_list[player]})
#     player_decks = decks

# print(player_decks)
