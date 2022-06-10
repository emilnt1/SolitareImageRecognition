from Model.Card import Card
from Model.CardLogic import CardLogic


class Column(CardLogic):
    cards = []
    isKingMovedTo = False

    def __init__(self):
        super().__init__()
        self.cards = []

    def find(self, card):
        count = 0
        for i in self.cards:
            if i.isVisible and i.suit == card.suit and i.rank == card.rank:
                return True, i

            count = count + 1
        return False, i

    def pop(self, card):
        cardsToReturn = []
        boo = False
        for i in reversed(self.cards):
            if card.rank == i.rank and card.suit == i.suit:
                boo = True
            else:
                cardsToReturn.append(self.cards.pop())
            if boo:
                cardsToReturn.append(self.cards.pop())
                if len(self.cards) != 0 and not self.cards[-1].isVisible:
                    self.cards[-1].makeVisible()
                return cardsToReturn

    def push(self, cards):
        cardsReversed = cards[::-1]
        self.cards.extend(cardsReversed)
