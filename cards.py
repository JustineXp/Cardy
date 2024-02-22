from random import random, choice, shuffle
from DeckClass import Deck
from databank import cards
from player import Player

# Function that calls all the other logic functions


def main():
    deck = Deck(cards)
    print(deck.length())
    shuffled_cards = deck.shuffle()
    players, no_of_cards = number_of_players()
    empty_player_decks = decks_creation(players)
    player_decks, remaining_deck = player_cards_assigner(
        shuffled_cards, players, empty_player_decks, no_of_cards)
    # picking_cards, starting_card = starting_card_generator(remaining_deck)
    starting_card, picking_cards = deck.starting_card(remaining_deck)
    #

    print(player)
    print('PICKING CARDS')
    print(len(picking_cards))

    print('STARTING CARD')
    print(f'{starting_card["name"]} : {starting_card["type"]}')
    #
    playing_player = who_is_to_play(1, player_decks)
    next_play(starting_card, picking_cards, playing_player)


# shuffling the deck of cards
def shuffle_cards(cards):
    shuffled_cards = cards[:]
    random.shuffle(shuffled_cards)
    return shuffled_cards


# create decks for the players
def decks_creation(players):
    player_decks = []
    rotation_list = list(range(1, players+1))
    shuffle(rotation_list)
    # print(rotation_numbers)

    for player in range(players):
        player_decks.append(
            {'player': player, 'deck': [], 'rotation_number': rotation_list[player]})

    # print(player_decks)

    return player_decks


# Generate cards for a player.
def player_cards_assigner(shuffled_cards, players, player_decks, no_of_cards):
    number_of_cards = players * no_of_cards
    shuffled_cards_copy = shuffled_cards[:]
    for deck in player_decks:
        deck['deck'] = shuffled_cards_copy[deck['player']:number_of_cards:players]

    remaining_deck = shuffled_cards[number_of_cards:]
    # print(shuffled_cards_copy)
    # for deck in player_decks:
    #     print(deck['deck'])

    # print(player_decks)
    for deck in player_decks:
        print('PLAYER : ' + str(deck['player']+1))
        # print(deck[0]['name'], ':', deck[0]['type'])
        print('*'*30)

        for card in deck['deck']:
            print(card['name'], ' : ', card['type'].title())
        print()
    # print('REMAINING CARDS IN THE DECK.')
    # print('*'*30)
    # for card in remaining_deck:
    #     print(card['name'], ':', card['type'].title())

    # print(len(remaining_deck))

    return player_decks, remaining_deck


def card_picking(remaining_deck, player_decks, number_to_pick, player):
    if number_to_pick == 1:
        picked_card = remaining_deck.pop[0]
        for deck in player_decks:
            if deck['player'] == deck[player]:
                deck['deck'].extend(picked_card)


# def starting_card_generator(remaining_deck):

#     non_start_card_names = ['K', 'Q', 'J', 8, 3, 2, 'A']
#     filtered_cards = [
#         card for card in remaining_deck if card['name'] not in non_start_card_names]

#     # print(filtered_cards)
#     starting_card = filtered_cards[0]

#     picking_cards = [card for card in remaining_deck if card != starting_card]

#     print('PICKING CARDS')
#     print(len(picking_cards))

#     print('STARTING CARD')
#     print(f'{starting_card["name"]} : {starting_card["type"]}')

#     return picking_cards, starting_card


def who_is_to_play(player_number, player_decks):
    playing_player = [
        player for player in player_decks if player['rotation_number'] == player_number]
    print(playing_player[0]['deck'])
    return playing_player[0]


def next_play(previous_card, picking_cards, playing_player):
    similar_name_cards = list(filter(
        lambda card: card['name'] == previous_card['name'], playing_player['deck']))
    similar_type_cards = list(filter(
        lambda card: card['type'] == previous_card['type'], playing_player['deck']))

    # print(similar_name_cards)
    possible_cards = similar_name_cards + similar_type_cards
    print(possible_cards)
    if len(possible_cards) > 0:
        card_to_play = choice(possible_cards)
        print(card_to_play)
        return card_to_play
    else:
        picked_card = picking_cards[0]
        picking_cards = picking_cards[1:]
        return picked_card, picking_cards

# How many players are playing the game


def number_of_players():
    number = int(input('How many players want to play : '))
    no_of_cards = int(input('How many cards for each player ? '))
    return number, no_of_cards


# Calling the main Function to Initiate the Logic
main()
