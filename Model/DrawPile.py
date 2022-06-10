from Model.CardLogic import CardLogic
from Model.Deck import Deck


class DrawPile(CardLogic):

    def __init__(self):
        super().__init__()
        self.cards = []
        self.draws = 0

    def drawIncrement(self):
        self.draws += 1

    def drawReset(self):
        self.draws = 0

    def pop(self, cards):
        newDeck = []
        newDeck.append(self.cards.pop())
        return newDeck

    def push(self, cards):
        self.cards.extend(cards)
