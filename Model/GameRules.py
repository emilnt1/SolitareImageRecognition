from Model.Card import Card
from Model.DrawPile import DrawPile
from Model.CardFactory import CardFactory
from View.KabaleView import display
from Model.Board import Board
from Model.SuitType import concludeFromString


def rowInterpreter(string, board):
    string = str(string)
    if 'c' in string or 'f' in string:
        rowNum = int(string[1])
        column = None
        foundation = False
        if string[0] == 'c':
            column = board.columns[rowNum]
        elif string[0] == 'f':
            column = board.foundations[rowNum]
            foundation = True
        return column, foundation
    else:
        newInput = input("Wrong input, try again")
        rowInterpreter(newInput, board)


def cardInterpreter(string):
    string = str(string)
    if 'H' in string or 'S' in string or 'D' in string or 'C' in string:
        cardRank = None
        cardSuit = None
        if len(string) == 3:
            oneString = string[2]
            cardRank = int("1" + oneString)
            cardSuit = concludeFromString(string[0])
        elif len(string) == 2:
            cardRank = int(string[1])
            cardSuit = concludeFromString(string[0])
        card = Card(cardRank, cardSuit)
        return card
    else:
        newInput = input("Wrong input, try again")
        cardInterpreter(newInput)

def errorInput(board):
    print("Wrong input, try again")
    playPhase(board)

def playPhase(board):
    gameOver = False
    while not gameOver:
        selectedColumn = input("Select column like (c1) or (f2):")
        fromColumn, isFoundation = rowInterpreter(selectedColumn, board)
        card = None
        if not isFoundation:
            selectCard = input("Select card to be moved:")
            card = cardInterpreter(selectCard)
            boo, card = fromColumn.find(card)
            if not boo:
                errorInput(board)
        else:
            card = fromColumn.cards[-1]
        selectedColumn = input("Select column like (c1) or (f2):")
        toColumn, isFoundation = rowInterpreter(selectedColumn, board)
        if not isFoundation:
            if allowedMoveColumn(card, toColumn):
                toColumn.push(fromColumn.pop(card))
        elif isFoundation:
            if allowedMoveFoundation(card, toColumn):
                toColumn.push(fromColumn.pop(card))
        else:
            errorInput(board)
        display(board)


def allowedMoveColumn(card, column):
    if card.rank == column.cards[-1].rank - 1:
        return True
    else:
        return False


def allowedMoveFoundation(card, foundation):
    if len(foundation.cards) == 0:
        return True
    else:
        if card.rank == foundation.cards[-1].rank + 1:
            return True
        else:
            return False


def gameOver():
    return True
