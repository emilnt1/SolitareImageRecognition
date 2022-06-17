from Model.Column import Column
from Model.Foundation import Foundation
from Model.DrawPile import DrawPile
from Model.Deck import Deck
from Model.CardLogic import CardLogic
from Model.Card import Card
from Model.SuitType import SuitType as type

class Board:

    def __init__(self, drawpile, deck):
        self.columns = [Column() for i in range(7)]
        self.foundations = [Foundation() for i in range(4)]
        #self.deck = Deck()
        #self.deck.cards = deck
        self.drawPile = drawpile # Face up
        self.deck = deck # Face down
        self.cards = []
        self.cardsLeftDeckDrawPile = 24
        self.isLastDrawMade = False
        self.cardsLeftColumns = [0,1,2,3,4,5,6]
        self.isLastMoveFromFoundationToColumn = False


        for x in range(21):
        # for x in range(1):
           deck.cards.append(Card(-1, type.H))
        for y in range(3):
           drawpile.cards.append(Card(-1, type.H))

    def changeCardsLeftDeckDrawPile(self, integer):
        self.cardsLeftDeckDrawPile += integer

    def changeCardsLeftColumns(self, columnNmb, integer):
        self.cardsLeftColumns[columnNmb-1] += integer


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

    def drawCards(self):
        if len(self.deck.cards) >= 3:
            for i in range(3): self.drawPile.cards.append(self.deck.cards.pop(0))
        else:
            newDeck = list(reversed(self.drawPile.cards))
            newDeck.extend(self.deck.cards)

            #self.deck.cards = newDeck
            self.deck.cards = list(reversed(newDeck))
            self.drawPile.cards = []
            self.drawCards()

            # Temp list
            # Reverse drawpile
            # Append last cards to the end of the list
            # Assign temp list.

    def mergeStatefulBoard(self, statefulBoard):
        self.cardsLeftColumns = statefulBoard.cardsLeftColumns
        self.cardsLeftDeckDrawPile = statefulBoard.cardsLeftDeckDrawPile
        self.foundations = statefulBoard.foundations
        self.isLastMoveFromFoundationToColumn = statefulBoard.isLastMoveFromFoundationToColumn
        if statefulBoard.drawPile.cards and self.drawPile.cards:
            statefulBoard.drawPile.cards[-1] = self.drawPile.cards[-1]
        self.drawPile.cards = statefulBoard.drawPile.cards
        self.deck.cards = statefulBoard.deck.cards

    def getCardsLeftColumn(self, c):
        if self.cardsLeftColumns[c] > 0:
            return self.cardsLeftColumns[c]
        return 0

    def __copy__(self):
        return type(self)(self.drawPile, self.deck.cards)