from Model.Card import Card
from Model.DrawPile import DrawPile
from Model.CardFactory import CardFactory
from View.KabaleView import display
from Model.Board import Board
from Model.SuitType import concludeFromString
from Model.SuitType import SuitType


def rowInterpreter(string, board):
    string = str(string)
    if 'c' in string or 'f' in string or 'd' in string:
        if 'd' not in string:
            rowNum = int(string[1])
        column = None
        type = -1
        if string[0] == 'c':
            column = board.columns[rowNum]
            type = 0
        elif string[0] == 'f':
            column = board.foundations[rowNum]
            type = 1
        else:
            if len(board.drawPile.cards) == 0:
                errorInput(board)
            column = board.drawPile
            type = 2
        return column, type
    else:
        errorInput(board)


def cardInterpreter(string, board):
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
        errorInput(board)


def errorInput(board):
    print("Wrong input or illegal move")
    playPhase(board)


def playPhase(board):
    gameOver = False
    while not gameOver:
        userOption = input("Draw or move a card (d or m):")
        if userOption == "m":
            moveCard(board)
        elif userOption == "d":
            drawCard(board)
        else:
            errorInput(board)
        gameOver = gameEnd(board)
        display(board)


def allowedMoveColumn(card, column):
    if len(column.cards) == 0:
        if card.rank == 13:
            return True
        else:
            return False
    else:
        if card.rank == column.cards[-1].rank - 1:
            if column.cards[-1].suit == SuitType.D or column.cards[-1].suit == SuitType.H:
                if card.suit == SuitType.C or card.suit == SuitType.S:
                    return True
                else:
                    return False
            elif column.cards[-1].suit == SuitType.C or column.cards[-1].suit == SuitType.S:
                if card.suit == SuitType.D or card.suit == SuitType.H:
                    return True
                else:
                    return False
            else:
                print("Card identity failure!")
                return False

        else:
            return False


def allowedMoveFoundation(card, foundation):
    if isinstance(card, list):
        return False
    if len(foundation.cards) == 0:
        if card.rank == 1:
            #print(str(len(foundation.cards)))
            return True
        else:
            return False
    else:
        if card.rank == foundation.cards[-1].rank + 1 and card.suit == foundation.cards[-1].suit:
            return True
        else:
            return False


def drawCard(board):
    if len(board.deck.cards) < 3:
        board.deck.cards.extend(board.drawPile.cards)
        board.drawPile.cards = []
    board.drawCards()


def moveCard(board):
    selectedColumn = input("Select column (c0) or foundation (f0) or drawpile (d):")
    fromColumn, type = rowInterpreter(selectedColumn, board)
    card = None
    if type == 0:
        selectCard = input("Select card to be moved:")
        card = cardInterpreter(selectCard, board)
        boo, card = fromColumn.find(card)
        if not boo:
            errorInput(board)
    elif type == 1:
        card = fromColumn.cards[-1]
    else:
        card = fromColumn.cards[-1]
    selectedColumn = input("Select column like (c1) or (f2):")
    toColumn, type = rowInterpreter(selectedColumn, board)
    if type == 0:
        if allowedMoveColumn(card, toColumn):
            toColumn.push(fromColumn.pop(card))
        else:
            errorInput(board)
    elif type == 1:
        if allowedMoveFoundation(card, toColumn):
            toColumn.push(fromColumn.pop(card))
        else:
            errorInput(board)
    else:
        errorInput(board)


def gameEnd(board):
    for i in board.foundations:
        if len(i.cards) == 0 or i.cards[-1].rank != 13:
            return False
    return True
