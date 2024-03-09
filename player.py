import random
from databank import Letters, Numbers


class Player:
    def __init__(self, deck):
        self.player_id = ''
        self.id_generator()
        self.player_deck = deck

    def __str__(self):
        # return (f"PLAYER ID : {self.player_id}")
        for card in self.player_deck:
            return (f"{card['name']} : {card['type']}")

    def __iter__(self):
        return iter(self.player_deck)

    def id_generator(self):
        user_id = []
        for _ in range(5):
            randomLetter = random.choice(Letters)
            randomNumber = random.choice(Numbers)
            user_id.append(randomLetter.upper())
            user_id.append(str(randomNumber))

        random.shuffle(user_id)

        for i in range(len(user_id)):
            self.player_id += user_id[i]

    def card_picking(self, remaining_deck, number_to_pick):
        picked_cards = remaining_deck[:number_to_pick]
        remaining_deck = remaining_deck[number_to_pick:]
        self.player_deck.extend(picked_cards)
        return remaining_deck

    def play(self):
        print('PLAYING GAME')
        ...
