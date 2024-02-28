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

    def id_generator(self):
        uid = []

        for _ in range(5):
            randomLetter = random.choice(Letters)
            randomNumber = random.choice(Numbers)
            uid.append(randomLetter.upper())
            uid.append(str(randomNumber))

        random.shuffle(uid)

        for i in range(len(uid)):
            self.player_id += uid[i]

    def play(self):
        print('PLAYING GAME')
        ...
