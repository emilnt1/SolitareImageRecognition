from Model.Card import Card
from Model.CardLogic import CardLogic


class Column(CardLogic):
    cards = []

    def __init__(self):
        super().__init__()
        self.cards = []

    def find(self, card):
        count = 0
        for i in self.cards:
            if i.isVisible and i.suit == card.suit and i.rank == card.rank:
                return count

            count = count + 1
        return False

    def pop(self, card):
        index = self.find(card)
        cardsToReturn = []
        if not card:
            pass
        else:
            for i in range(index, len(self.cards)):
                cardsToReturn.append(self.cards.pop())
            return cardsToReturn

    def push(self, cards):
        self.cards.extend(cards)
