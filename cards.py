from random import random, choice, shuffle
from DeckClass import Deck
from databank import cards
from player import Player

# Function that calls all the other logic functions


def main():
    players, no_of_cards = number_of_players()
    deck = Deck(cards, players, no_of_cards)
    player_decks = deck.player_decks
    starting_card = deck.the_starting_card
    picking_cards = deck.remaining_cards
    players_with_decks = []

    print('PICKING CARDS')
    print(len(picking_cards))

    print('STARTING CARD')
    print(f'{starting_card["name"]} : {starting_card["type"]}')
    print("*"*30)

    for deck in player_decks:
        specific_deck = deck['deck']
        player_ = Player(specific_deck)
        players_with_decks.append(player_)

    for player in players_with_decks:
        # print(player)
        print(f"PLAYER ID : {player.player_id}")
        for card in player.player_deck:
            print(f"{card['name']} : {card['type']}")
        print("*"*30)


def card_picking(remaining_deck, player_decks, number_to_pick, player):
    if number_to_pick == 1:
        picked_card = remaining_deck.pop[0]
        for deck in player_decks:
            if deck['player'] == deck[player]:
                deck['deck'].extend(picked_card)


def number_of_players():
    number = int(input('How many players want to play : '))
    no_of_cards = int(input('How many cards for each player ? '))
    return number, no_of_cards


# Calling the main Function to Initiate the Logic
main()
