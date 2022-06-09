from Model.GameRules import *
from AI.Node import Node

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
        nextNode.commands += node.commands
        highestSuccessNode = treeSearchBackTracking(nextNode)
        if highestSuccessNode is None:
            highestSuccessNode = nextNode
        elif highestSuccessNode.points < node.points:
            highestSuccessNode = nextNode
    stateful_board.foundations = highestSuccessNode.board.foundations
    return highestSuccessNode


def deadEnd():
    return False


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
                        if card1.rank == 13:
                            boo, kmoves = kingToEmpty(board, card1, column1, col1)
                            if boo:
                                moves.extend(kmoves)
                        if allowedMoveColumn(card1, column2):
                            boardCopy = board.copy
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
                if card.rank == 13:
                    boo, kmoves = kingToEmpty(board, card, None, -1)
                    if boo:
                        moves.extend(kmoves)
                if allowedMoveColumn(card, column2):
                    boardCopy = board.copy
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
                if allowedMoveFoundation(card, foundation):
                    boardCopy = board.copy
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
                if allowedMoveFoundation(card, foundation):
                    boardCopy = board.copy
                    boardCopy.moveCard(board.drawPile, card, foundation)
                    moves.append(Node(5, boardCopy, "From drawpile to foundation " + str(i) + "\n"))
                i += 1
    return moves


def kingToEmpty(board, card, origin, originNum):
    moves = []
    boo = False
    if originNum == -1:
        col2 = 1
        for column2 in board.columns:
            if len(column2.cards) == 0:
                boo = True
                boardCopy = board.copy
                boardCopy.moveCard(board.drawPile, card, column2)
                moves.append(Node(4, boardCopy,
                                  "Card " + str(card) + " from drawpile to column " + str(
                                      col2) + "\n"))
            col2 += 1
    else:
        column1 = origin
        col2 = 1
        for column2 in board.columns:
            if column1 != column2 and len(column2.cards) == 0:
                boo = True
                boardCopy = board.copy
                boardCopy.moveCard(column1, card, column2)
                moves.append(Node(4, boardCopy,
                              "Card " + str(card) + " from column " + str(originNum) + " to column " + str(
                                  col2) + "\n"))
            col2 += 1
    return boo, moves
