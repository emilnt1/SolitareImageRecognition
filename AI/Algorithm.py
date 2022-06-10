import copy

from Model.GameRules import *
from AI.Node import Node
import collections


def starter(board):
    node = Node(0, board, "")
    last_node = treeSearchBackTracking(node, node)
    return last_node.commands

def treeSearchBackTracking(node, highestSuccessNode):
    if gameWon(node.board):
        display(node.board)
        print("won")
        node.points = + 600
        return node
    if endlessLoop(node):
        display(node.board)
        print("")
        return node
    if deadEnd(node.board):
        print("lost")
        return node

    node.edgeNotes.extend(analyse_moves(node))
    # Delete the two lines below
    display(node.board)
    for command in reversed(node.commands):
        print(command + "\n")
    input("Press Enter " + str(len(node.edgeNotes)))

    while len(node.edgeNotes) != 0:
        edgeNode = node.edgeNotes.pop()
        edgeNode.points += node.points
        edgeNode.commands.extend(node.commands)
        edgeNode.board.updateCardsLeft()
        highestSuccessNode = treeSearchBackTracking(edgeNode, highestSuccessNode)
        if highestSuccessNode.points < edgeNode.points:
            highestSuccessNode = edgeNode
    return highestSuccessNode


# Prevents endless loop of AI.
def endlessLoop(node):
    if len(node.commands) != len(set(node.commands)):
        return True
    else:
        return False


def deadEnd(board):
    if board.drawPile.draws == 9:
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
                            board = copy.deepcopy(board)
                            board.moveCard(board.columns[col1-1], card1, board.columns[col2-1])
                            moves.append(Node(2, board, "Card " + str(card1) + " from column " + str(col1) + " to column " + str(col2)))
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
                    board = copy.deepcopy(board)
                    board.drawPile.drawReset()
                    board.moveCard(board.drawPile, card, board.columns[i-1])
                    moves.append(Node(1, board, "From drawpile to column " + str(i)))
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
                    board = copy.deepcopy(board)
                    board.moveCard(board.columns[col1-1], card, board.foundations[found1-1])
                    moves.append(Node(5, board, "Card " + str(card) + " from column " + str(col1) + " to foundation " + str(found1)))
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
                board = copy.deepcopy(board)
                board.drawPile.drawReset()
                board.moveCard(board.drawPile, card, board.foundations[i-1])
                moves.append(Node(5, board, "From drawpile to foundation " + str(i)))
            i += 1
    return moves


def drawCardsFromBoard(board):
    moves = []
    if board.cardsLeftDeckDrawPile > 3:
        board = copy.deepcopy(board)
        board.drawPile.drawIncrement()
        board.drawCards()
        moves.append(Node(-3, board, "Draw cards"))
    return moves
