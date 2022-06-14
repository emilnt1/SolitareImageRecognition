import copy

from Model.GameRules import *
from AI.Node import Node
import collections


def starter(board):
    node = Node(0, board)
    last_node = treeSearchBackTracking(node, node)
    return last_node.commands

def treeSearchBackTracking(node, highestSuccessNode):
    if gameWon(node.board):
        display(node.board)
        node.commands.extend(["Won"])
        node.won = True
        node.points = + 600
        return node
    if endlessLoop(node):
        display(node.board)
        print("")
        return node
    if deadEnd(node.board):
        node.commands.extend(["Lost"])
        return node


    node.edgeNotes.extend(analyse_moves(node))
    while len(node.edgeNotes) != 0:
        edgeNode = node.edgeNotes.pop()
        edgeNode.points += node.points
        edgeNode.commands.extend(node.commands)
        edgeNode.board.updateCardsLeft()
        val = treeSearchBackTracking(edgeNode, highestSuccessNode)
        if val.won:
            highestSuccessNode = val
    return highestSuccessNode


# Prevents endless loop of AI.
def endlessLoop(node):
    if len(node.commands) == 0:
        return False
    if len(node.commands) != len(set(node.commands)):
        return True
    else:
        return False


def deadEnd(board):
    if board.drawPile.draws == 17:
        return True
    else:
        return False


def analyse_moves(node):
    moves = []
    moves.extend(columnToFoundation(node.board))
    moves.extend(drawpileToFoundation(node.board))
    moves.extend(columnToColumnMove(node.board))
    moves.extend(drawpileToColumnMove(node.board))
    moves.extend(drawCardsFromBoard(node.board))
    moves.extend(foundationToColumn(node.board))
    return reversed(moves)


def columnToColumnMove(board):
    moves = []
    col1 = 1
    for column1 in board.columns:
        if len(column1.cards) != 0:
            col2 = 1
            for column2 in board.columns:
                if column1 != column2 and len(column2.cards) != 0:
                    for card1 in column1.cards:
                        if allowedMoveColumn(card1, column2) and card1.isVisible:
                            boardcopy = copy.deepcopy(board)
                            boardcopy.moveCard(boardcopy.columns[col1-1], card1, boardcopy.columns[col2-1])
                            newMove = Node(2, boardcopy)
                            newMove.commands.append("Card " + str(card1) + " from column " + str(col1) + " to column " + str(col2))
                            moves.append(newMove)
                col2 += 1
        col1 += 1
    return moves


def drawpileToColumnMove(board):
    moves = []
    if len(board.drawPile.cards) != 0:
        for card in board.drawPile.cards:
            i = 1
            for column2 in board.columns:
                if allowedMoveColumn(card, column2) and card.isVisible:
                    boardcopy = copy.deepcopy(board)
                    boardcopy.drawPile.drawReset()
                    boardcopy.moveCard(boardcopy.drawPile, card, boardcopy.columns[i-1])
                    newMove = Node(1, boardcopy)
                    newMove.commands.append("From drawpile to column " + str(i))
                    moves.append(newMove)
                i += 1
    return moves


def columnToFoundation(board):
    moves = []
    col1 = 1
    for column1 in board.columns:
        if len(column1.cards) != 0:
            found1 = 1
            for foundation in board.foundations:
                card = column1.cards[-1]
                if allowedMoveFoundation(card, foundation) and card.isVisible:
                    boardcopy = copy.deepcopy(board)
                    boardcopy.moveCard(boardcopy.columns[col1-1], card, boardcopy.foundations[found1-1])
                    newMove = Node(5, boardcopy)
                    newMove.commands.append("Card " + str(card) + " from column " + str(col1) + " to foundation " + str(found1))
                    moves.append(newMove)
                found1 += 1
        col1 += 1
    return moves


def drawpileToFoundation(board):
    moves = []
    if len(board.drawPile.cards) != 0:
        i = 1
        card = board.drawPile.cards[-1]
        for foundation in board.foundations:
            if allowedMoveFoundation(card, foundation) and card.isVisible:
                boardcopy = copy.deepcopy(board)
                boardcopy.drawPile.drawReset()
                boardcopy.moveCard(boardcopy.drawPile, card, boardcopy.foundations[i-1])
                newMove = Node(5, boardcopy)
                newMove.commands.append("From drawpile to foundation " + str(i))
                moves.append(newMove)
            i += 1
    return moves


def drawCardsFromBoard(board):
    moves = []
    if board.cardsLeftDeckDrawPile > 3:
        boardcopy = copy.deepcopy(board)
        boardcopy.drawPile.drawIncrement()
        boardcopy.drawCards()
        moves.append(Node(-3, boardcopy))
    return moves

def foundationToColumn(board):
    moves = []
    found = 1
    for foundation in board.foundations:
        if len(foundation.cards) != 0:
            card = foundation.cards[-1]
            col2 = 1
            for column in board.columns:
                if allowedMoveColumn(card, column):
                    boardcopy = copy.deepcopy(board)
                    boardcopy.columns[col2-1].cards.append(boardcopy.foundations.cards[found-1].po)
                    newMove = Node(-5, boardcopy)
                    newMove.commands.append("From foundation " + str(found) + " to column " + str(col2))
                    moves.append(newMove)
                col2 += 1
        found += 1
    return moves
