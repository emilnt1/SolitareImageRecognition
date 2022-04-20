from Model.SuitType import SuitType as type
from Model.Card import Card


class CardFactory:
    cards = []

    def makeCards(self):
        for i in range(0, 13):
            self.cards.append(Card(i, type.HEART))

        for i in range(0, 13):
            self.cards.append(Card(i, type.CLUBS))

        for i in range(0, 13):
            self.cards.append(Card(i, type.SPADES))

        for i in range(0, 13):
            self.cards.append(Card(i, type.DIAMONDS))
