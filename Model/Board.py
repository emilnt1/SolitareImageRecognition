from Model.Column import Column
from Model.Foundation import Foundation
from Model.DrawPile import DrawPile
from Model.Deck import Deck
from Model.CardLogic import CardLogic
from Model.Card import Card

class Board:

    def __init__(self, drawpile, deck):
        self.columns = [Column() for i in range(7)]
        self.foundations = [Foundation() for i in range(4)]
        self.deck = Deck()
        self.deck.cards = deck
        self.drawPile = drawpile
        self.cards = []
        self.cardsLeftDeckDrawPile = 24
        self.isLastDrawMade = False
        self.cardsLeftColumns = [0,1,2,3,4,5,6]

    def allocateCards(self):
        count = 1
        for i in self.columns:
            insertionArray = []
            for x in range(count):
                if x == count-1:
                    insertionArray.append(self.deck.cards.pop())
                else:
                    card = self.deck.cards[-1]
                    card.makeInvisible()
                    insertionArray.append(self.deck.cards.pop())

            i.cards.extend(insertionArray)
            count = count + 1

    def moveCard(self, origin, cards, place):
        place.push(origin.pop(cards))

    def updateCardsLeft(self):
        self.cardsLeftDeckDrawPile = len(self.deck.cards) + len(self.drawPile.cards)
        columnCards = 0
        for column in self.columns:
            columnCards += len(column.cards)
        self.cardsLeftColumns = columnCards

    def drawCards(self):
        self.drawPile.cards.append(self.deck.cards.pop())
        self.drawPile.cards.append(self.deck.cards.pop())
        self.drawPile.cards.append(self.deck.cards.pop())

    def mergeStatefulBoard(self, statefulBoard):
        self.cardsLeftColumns = statefulBoard.cardsLeftColumns
        self.cardsLeftDeckDrawPile = statefulBoard.cardsLeftDeckDrawPile
        self.foundations = statefulBoard.foundations

    def getCardsLeftColumn(self, c):
        if self.cardsLeftColumns[c] > 0:
            return self.cardsLeftColumns[c]
        return 0

    def __copy__(self):
        return type(self)(self.drawPile, self.deck.cards)