from Model.Column import Column
from Model.Foundation import Foundation
from Model.DrawPile import DrawPile
from Model.Deck import Deck


class Board:

    def __init__(self, drawpile, deck):
        self.columns = [Column() for i in range(8)]
        self.foundations = [Foundation, Foundation, Foundation, Foundation]
        self.drawPile = drawpile
        self.deck = deck

    def allocateCards(self):
        count = 0
        for i in self.columns:
            insertionArray = []
            for x in range(count):
                insertionArray.append(self.deck.pop())

            i.cards.extend(insertionArray)
            count = count + 1
