from Model.Column import Column
from Model.Foundation import Foundation
from Model.DrawPile import DrawPile
from Model.Deck import Deck


class Board:

    def __init__(self, drawpile, deck):
        self.columns = [Column() for i in range(8)]
        self.foundations = [Foundation() for i in range(5)]
        self.deck = Deck()
        self.deck.cards = deck
        self.drawPile = drawpile

    def allocateCards(self):
        count = 0
        for i in self.columns:
            insertionArray = []
            for x in range(count):
                insertionArray.append(self.deck.cards.pop())

            i.cards.extend(insertionArray)
            count = count + 1

    def moveCard(self, cards, place):
        if cards is not None:
            place.push(cards)
            return True
        else:
            return False

    def drawCards(self):
        self.drawPile.cards.extend(self.deck.cards.pop())
        self.drawPile.cards.extend(self.deck.cards.pop())
        self.drawPile.cards.extend(self.deck.cards.pop())


