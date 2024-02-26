from random import shuffle, choice


class Deck:

    def __init__(self, cards):
        self.cards = cards
        self.shuffled_cards = []
        self.shuffle()

    def __repr__(self):
        print([f'{card["name"]} of {card["type"]}' for card in self.cards])

    def shuffle(self):
        shuffled_cards = self.cards[:]
        shuffle(shuffled_cards)
        self.shuffled_cards = shuffled_cards

    def length(self):
        return len(self.cards)

    def starting_card(self, shuffled_deck):
        non_start_cards = ['K', 'Q', 'J', '8', '3', '2', 'A']
        starting_card = choice(
            [card for card in shuffled_deck if card['name'] not in non_start_cards])
        remaining_deck = [
            card for card in shuffled_deck if card['name'] != starting_card['name']]
        return starting_card, remaining_deck

    def issue_cards(self, number, picking_cards):
        cards_issued = [
            card for card in picking_cards if picking_cards.index(card) < number]
        return cards_issued, picking_cards[number:]

    @classmethod
    def next_card(cls, played_card, player_deck):
        possible_cards = [card for card in player_deck if card['name']
                          == played_card['name'] or card['type'] == played_card['type']]
        grouped_possible_cards = {
            'same_name': [card for card in possible_cards if played_card['name'] == card['name']],
            'same_type': [card for card in possible_cards if played_card['type'] == card['type']]}

    # CREATION OF PLAYER DECKS
    @classmethod
    def decks_creation(cls, number_of_players):
        player_decks = []
        rotation_list = list(range(1, number_of_players+1))
        shuffle(rotation_list)

        for player in range(number_of_players):
            player_decks.append(
                {'player': player, 'deck': [], 'rotation_number': rotation_list[player]})

        print(player_decks)

        return player_decks

    # GENERATE CARDS FOR A PLAYER
    def player_cards_assigner(self, shuffled_cards, number_of_players, player_decks, no_of_cards):
        number_of_cards = number_of_players * no_of_cards
        shuffled_cards_copy = self.shuffled_cards[:]
        for deck in player_decks:
            deck['deck'] = shuffled_cards_copy[deck['player']:number_of_cards:number_of_players]

        remaining_deck = shuffled_cards[number_of_cards:]

        for deck in player_decks:
            print('PLAYER : ' + str(deck['player']+1))
            print('*'*30)

            for card in deck['deck']:
                print(card['name'], ' : ', card['type'].title())
            print()
        return player_decks, remaining_deck
