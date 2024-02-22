from random import shuffle, choice


class Deck:

    def __init__(self, cards):
        self.cards = cards

    def __repr__(self):
        print([f'{card["name"]} of {card["type"]}' for card in self.cards])

    def shuffle(self):
        shuffled_cards = self.cards[:]
        shuffle(shuffled_cards)
        return shuffled_cards

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
