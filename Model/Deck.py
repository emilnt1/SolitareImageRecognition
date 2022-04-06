from Model.CardLogic import CardLogic


class Deck(CardLogic):
    cards = []

    def __init__(self):
        super.__init__()
        self.cards = []

    def pop(self, cards):
        self.cards.pop(len(cards))

    def push(self, cards):
        self.cards.extend(cards)
