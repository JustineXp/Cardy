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
    picking_cards = deck.picking_cards
    players_with_decks = []

    print(len(deck))

    print('PICKING CARDS')
    print(len(picking_cards))
    print("*"*30)
    display_option(picking_cards)
    print("*"*30)

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
        display_option(player.player_deck)
        print("*"*30)


def display_option(specific_list):
    for card in specific_list:
        if card['name'] == '10':
            print(f"{card['name']}  : {card['type']}")
        else:
            print(f"{card['name']}   : {card['type']}")


def number_of_players():
    number = int(input('How many players want to play : '))
    no_of_cards = int(input('How many cards for each player ? '))
    return number, no_of_cards


# Calling the main Function to Initiate the Logic
main()
