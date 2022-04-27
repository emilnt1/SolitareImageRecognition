from Model.CardLogic import CardLogic


class Deck(CardLogic):

    def __init__(self):
        super().__init__()
        self.cards = []

    """
    def pop(self, cards):
        self.cards.pop(len(cards))
        return self.cards.pop(len(cards))
    """

    def pop(self):
        return self.cards.pop()

    def push(self, cards):
        self.cards.extend(cards)
