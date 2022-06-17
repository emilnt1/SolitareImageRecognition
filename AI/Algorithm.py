import copy

from Model.GameRules import *
from AI.Node import Node
import collections

def treeSearchBackTracking(node, highestSuccessNode, functions, depth):
    depth += -1
    node.depth = depth
    #display(node.board)
    #if len(node.commands) != 0:
    #    print(node.commands[0])
    #input("Press Enter. Node points: " + str(node.points) + " depth: " + str(depth))
    if gameWon(node.board):
        node.commands.append("Won")
        node.points += 600
        return node
    if endlessLoop(node) and node.commands[0] != "Draw cards":
        return node
    if deadEnd(node):
        node.commands.append("Lost")
        return node
    if depth == 0:
        return node

    node.edgeNodes.extend(analyse_moves(functions, node))
    if len(node.edgeNodes) != 0:
        highestSuccessNode = node.edgeNodes[0]
    while len(node.edgeNodes) != 0:
        edgeNode = node.edgeNodes.pop()
        edgeNode.previousNode = node
        edgeNode.points += node.points
        edgeNode.commands.extend(node.commands)
        val = treeSearchBackTracking(edgeNode, highestSuccessNode, functions, depth)
        if pointsAnalysis(highestSuccessNode) < pointsAnalysis(val) or pointsAnalysis(highestSuccessNode) == pointsAnalysis(val) and val.depth > highestSuccessNode.depth:
            highestSuccessNode = val
    depth += 1
    return highestSuccessNode


# Prevents endless loop of AI.
def endlessLoop(node):
    if node.previousNode is not None and node.previousNode.previousNode is not None:
        return checkForEndless(node.previousNode.previousNode.board, node.board)
    else:
        return False

def deadEnd(node):
    if node.draws == 18:
        return True
    else:
        return False


def analyse_moves(functions, node):
    moves = []
    for func in functions:
        if func == 1:
            moves.extend(columnToFoundation(node.board))
        if func == 2:
            moves.extend(drawpileToFoundation(node.board))
        if func == 3:
            moves.extend(columnToColumnMove(node.board))
        if func == 4:
            moves.extend(drawpileToColumnMove(node.board))
        if func == 5:
            moves.extend(drawCardsFromBoard(node.board))
        if func == 6:
            moves.extend(foundationToColumn(node.board))
    return reversed(moves)


def columnToColumnMove(board):
    moves = []
    col1 = 1
    for column1 in board.columns:
        if len(column1.cards) != 0:
            col2 = 1
            for column2 in board.columns:
                if column1 != column2:
                    for card1 in column1.cards:
                        if allowedMoveColumn(card1, column2) and card1.isVisible:
                            if card1.rank == 13 and column1.cards[0] == card1:
                                pass
                            else:
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
        card = board.drawPile.cards[-1]
        i = 1
        for column2 in board.columns:
            if allowedMoveColumn(card, column2) and card.isVisible:
                if board.cardsLeftDeckDrawPile == 3 and len(board.drawPile.cards) != 3:
                    break
                boardcopy = copy.deepcopy(board)
                boardcopy.moveCard(boardcopy.drawPile, card, boardcopy.columns[i-1])
                newMove = Node(1, boardcopy)
                newMove.board.updateCardsLeft()
                newMove.commands.append("From drawpile to column " + str(i))
                moves.append(newMove)
            i += 1
    return moves


def columnToFoundation(board):
    moves = []
    col1 = 1
    for column1 in board.columns:
        if len(column1.cards) != 0:
            card = column1.cards[-1]
            found1 = 1
            for foundation in board.foundations:
                if allowedMoveFoundation(card, foundation) and card.isVisible:
                    boardcopy = copy.deepcopy(board)
                    boardcopy.moveCard(boardcopy.columns[col1-1], card, boardcopy.foundations[found1-1])
                    newMoves = Node(5, boardcopy)
                    newMoves.commands.append("Card " + str(card) + " from column " + str(col1) + " to foundation " + str(found1))
                    moves.append(newMoves)
                    break
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
                if board.cardsLeftDeckDrawPile == 3 and len(board.drawPile.cards) != 3:
                    break
                boardcopy = copy.deepcopy(board)
                boardcopy.moveCard(boardcopy.drawPile, card, boardcopy.foundations[i-1])
                newMove = Node(5, boardcopy)
                newMove.board.updateCardsLeft()
                newMove.commands.append("From drawpile to foundation " + str(i))
                moves.append(newMove)
                break
            i += 1
    return moves


def drawCardsFromBoard(board):
    moves = []
    if drawAllowed(board):
        boardcopy = copy.deepcopy(board)
        boardcopy.drawCards()
        newMove = Node(0, boardcopy)
        newMove.board.updateCardsLeft()
        newMove.commands.append("Draw cards")
        moves.append(newMove)
    return moves

def foundationToColumn(board):
    moves = []
    for fRange in range(len(board.foundations)):
        if len(board.foundations[fRange].cards) != 0:
            card = board.foundations[fRange].cards[-1]
            for cRange in range(len(board.columns)):
                if allowedMoveColumn(card, board.columns[cRange]):
                    boardcopy = copy.deepcopy(board)
                    boardcopy.moveCard(boardcopy.foundations[fRange], card, boardcopy.columns[cRange])
                    newMove = Node(-5, boardcopy)
                    newMove.commands.append("From foundation " + str(fRange + 1) + " move card " + str(card) + " to column " + str(cRange + 1))
                    moves.append(newMove)
    return moves

def checkForEndless(preBoard, nextBoard):
    for cRange in range(7):
        col1 = preBoard.columns[cRange]
        col2 = nextBoard.columns[cRange]
        if len(col1.cards) == len(col2.cards):
            for cardRange in range(len(col1.cards)):
                if col1.cards[cardRange].rank != col2.cards[cardRange].rank:
                    if col1.cards[cardRange].suit != col2.cards[cardRange].suit:
                        return False
        else:
            return False
    return True

def pointsAnalysis(node):
    num = 0
    for foundation in node.board.foundations:
        if len(foundation.cards) != 0:
            for card in foundation.cards:
                num += card.rank
    for column in node.board.columns:
        if len(column.cards) != 0:
            for card in column.cards:
                num += card.rank
    return num

def getArrayOfMoves(node):
    nodeArray = []
    while node.previousNode is not None:
        nodeArray.append(node)
        node = node.previousNode
    return nodeArray
