class Card():
    rank = -1
    suit = -1
    x = -1
    y = -1
    isVisible = True

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def makeVisible(self):
        self.isVisible = True

    def getCard(self):
        return self