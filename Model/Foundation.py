from Model.CardLogic import CardLogic
from Model.Card import Card


class Foundation(CardLogic):
    cards = []

    def __init__(self):
        super().__init__()
        self.cards = []

    def pop(self):
        if len(self.cards) > 1:
            pass
        else:
            return self.cards.pop()

    def push(self, cards):
        if len(cards) < 1:
            if self.cards[len(cards)].rank == cards[0].rank - 1:
                self.cards.extend(cards)
            else:
                pass
