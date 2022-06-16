from Model.SuitType import SuitType as type

class Card():
    rank = -1
    suit = -1
    x = -1
    y = -1
    conf = -1
    isVisible = True

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def makeInvisible(self):
        self.isVisible = False

    def makeVisible(self):
        self.isVisible = True

    def getCard(self):
        return self

    def __str__(self):
        return {
        type.H : "Hearts ",
        type.S : "Spades ",
        type.D : "Diamonds ",
        type.C : "Clubs "
    }.get(self.suit) + str(self.rank)