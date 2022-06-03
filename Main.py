from View.KabaleView import display
from Model.Board import Board
from Model.Deck import Deck
from Model.Card import Card
from Model.DrawPile import DrawPile
from Model.CardFactory import CardFactory
from Model.Column import Column
from Model.Foundation import Foundation

gameOver = False
cardFactory = CardFactory()
cardFactory.makeCards()
cardFactory.randomizeCards()
board = Board(DrawPile(), cardFactory.cards)
board.allocateCards()
display(board)


def rowInterpreter(string):
    string = str(string)
    if 'c' in string or 'f' in string:
        rowNum = int(string[1])
        column = 0
        foundation = 0
        if string[0] == 'c':
            column = rowNum
        if string[0] == 'f':
            foundation = rowNum
        return column, foundation
    else:
        newInput = input("Forkert input, prøv igen")
        rowInterpreter(newInput)

def cardInterpreter(string):
    string = str(string)
    if 'H' in string or 'S' in string or 'D' in string or 'C' in string:
        cardRank = None
        cardSuit = None
        if len(string) == 3:
            oneString = string[2]
            cardRank = int("1" + oneString)
            cardSuit = string[0]
        elif len(string) == 2:
            cardRank = int(string[1])
            cardSuit = string[0]
        card = Card(cardRank, cardSuit)
        return card
    else:
        newInput = input("Forkert input, prøv igen")
        cardInterpreter(newInput)



def playPhase():
    while not gameOver:
        selectedColumn = input("Select column like (c1) or (f2):")
        column1, foundation1 = rowInterpreter(selectedColumn)
        selectCard = input("Select card to be moved:")
        card : Card = cardInterpreter(selectCard)
        somecard = None
        if column1 == 0:
            somecard : foundation1 = board.foundations.index(foundation1)
        elif foundation1 == 0:
            somecard = board.columns.pop(card)

        selectedColumn = input("Select column like (c1) or (f2):")
        column2 = rowInterpreter(selectedColumn)



def popFoundation(someint):
    if


    return board.foundations.index(someint)

def popColumn(someint):

    return board.columns.index(someint)



def gameOver():


