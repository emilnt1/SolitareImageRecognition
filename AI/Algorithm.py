import copy

from Model.GameRules import *
from AI.Node import Node
import collections

stateful_board = Board(DrawPile(), None)


def starter(board):
    node = Node(0, board, "")
    last_node = treeSearchBackTracking(node)
    return last_node.commands


def treeSearchBackTracking(node):
    priorityQueue = []
    priorityQueue.extend(analyse_moves(node))
    highestSuccessNode = None

    while len(priorityQueue) != 0:
        nextNode = priorityQueue.pop()
        nextNode.points += node.points
        nextNode.commands.extend(node.commands)
        if deadEnd(node):
            print("OH SHIT, STOP!")

        #Delete the two lines below
        display(node.board)
        input("Press Enter ")

        highestSuccessNode = treeSearchBackTracking(nextNode)
        if highestSuccessNode is None:
            highestSuccessNode = nextNode
        elif highestSuccessNode.points < node.points:
            highestSuccessNode = nextNode
    stateful_board.foundations = highestSuccessNode.board.foundations
    return highestSuccessNode

# Prevents endless loop of AI.
def deadEnd(node):
    if len(node.commands) != len(set(node.commands)):
        return True
    else:
        return False

def evaluation(board1, board2):
    pass

def analyse_moves(node):
    moves = []
    moves.extend(columnToFoundation(node.board))
    moves.extend(drawpileToFoundation(node.board))
    moves.extend(columnToColumnMove(node.board))
    moves.extend(drawpileToColumnMove(node.board))
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
                            boardCopy = copy.deepcopy(board)
                            boardCopy.moveCard(column1, card1, column2)
                            moves.append(Node(2, boardCopy,
                                              "Card " + str(card1) + " from column " + str(col1) + " to column " + str(
                                                  col2) + "\n"))
                col2 += 1
        col1 += 1
    return moves


def drawpileToColumnMove(board):
    moves = []
    if len(board.drawPile.cards) != 0:
        i = 1
        for card in board.drawPile.cards:
            for column2 in board.columns:
                if allowedMoveColumn(card, column2) and card.isVisible:
                    boardCopy = copy.deepcopy(board)
                    boardCopy.moveCard(board.drawPile, card, column2)
                    moves.append(Node(1, boardCopy, "From drawpile to column " + str(i) + "\n"))
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
                    boardCopy = copy.deepcopy(board)
                    boardCopy.moveCard(column1, card, foundation)
                    moves.append(Node(5, boardCopy,
                                      "Card" + str(card) + " from column " + str(col1) + " to foundation " + str(
                                          found1) + "\n"))
                found1 += 1
        col1 += 1
    return moves


def drawpileToFoundation(board):
    moves = []
    if len(board.drawPile.cards) != 0:
        for card in board.drawPile.cards:
            i = 1
            for foundation in board.foundations:
                if allowedMoveFoundation(card, foundation) and card.isVisible:
                    boardCopy = copy.deepcopy(board)
                    boardCopy.moveCard(board.drawPile, card, foundation)
                    moves.append(Node(5, boardCopy, "From drawpile to foundation " + str(i) + "\n"))
                i += 1
    return moves

def drawCards():
    moves = []
