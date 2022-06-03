from Model.CardLogic import CardLogic
from Model.Deck import Deck


class DrawPile(CardLogic):

    def __init__(self):
        super().__init__()
        self.cards = []

    def pop(self, cards):
        newDeck = []
        for i in self.cards:
            newDeck.append(i)
            self.cards.pop(i)
        return newDeck

    def push(self, cards):
        self.cards.extend(cards)
