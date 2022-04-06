
import SuitType as type
from Model.Card import Card


class CardFactory:
    cards = []
    def makeCards(self):
        for i in range(0,13):
            self.cards.append(Card(i, type.SuitType.HEART))

        for i in range(0,13):
            self.cards.append(Card(i, type.SuitType.CLUBS))

        for i in range(0,13):
            self.cards.append(Card(i, type.SuitType.SPADES))

        for i in range(0,13):
            self.cards.append(Card(i, type.SuitType.DIAMONDS))
