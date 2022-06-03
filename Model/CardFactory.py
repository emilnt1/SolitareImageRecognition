from Model.SuitType import SuitType as type
from Model.Card import Card


class CardFactory:
    cards = []

    def makeCards(self):
        for i in range(0, 13):
            self.cards.append(Card(i, type.H))

        for i in range(0, 13):
            self.cards.append(Card(i, type.C))

        for i in range(0, 13):
            self.cards.append(Card(i, type.S))

        for i in range(0, 13):
            self.cards.append(Card(i, type.D))
