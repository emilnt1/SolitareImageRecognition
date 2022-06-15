from Model.CardLogic import CardLogic
from Model.Card import Card


class Foundation(CardLogic):
    cards = []

    def __init__(self):
        super().__init__()
        self.cards = []

    def pop(self, cards):
        return [self.cards.pop()]

    def push(self, cards):
        if len(cards) < 2:
            if len(self.cards) == 0:
                self.cards.extend(cards)
            elif self.cards[-1].rank == cards[0].rank - 1:
                self.cards.extend(cards)
            else:
                pass
