from Model.Card import Card
from Model.DrawPile import DrawPile
from Model.CardFactory import CardFactory
from View.KabaleView import display
from Model.Board import Board
from Model.SuitType import concludeFromString
from Model.SuitType import SuitType as type
from Model.GameRules import *
from Model.DrawPile import DrawPile
from Model.Deck import Deck
from Model.Column import Column

## Statefull board only with foundations
stateful_board = Board(DrawPile(), None)
#global cardsLeftDeckDrawPile,isLastDrawMade
#cardsLeftDeckDrawPile = 24
#isLastDrawMade = False

def nextMove(board):
    ## Merge board fra ML and stateful_board
   # curr_move = ""
    ##isAceFound, count_columns,count_foundation, card = findAce(board)
        #curr_move = putFoundation(board)
    #if ( len(curr_move) != 0):
    #    return  curr_move
    #

    ### DELETE ME
    #card = Card(1,type.H)
    #stateful_board.foundations[0].cards.append(card)
    ###

    moves = [makeLastDraw, 
            putFoundation, 
            # putKingToEmptyColumnIfQueenAvailable,
            putColumn, 
            fromFoundationToColumn,
            makeDraw]

    for move in moves:
        if move.__name__ == "putFoundation" and stateful_board.isLastMoveFromFoundationToColumn:
            stateful_board.isLastMoveFromFoundationToColumn = False
            continue
        curr_result = move(board)
        if curr_result is not None and len(curr_result) != 0:
            return curr_result
        #if ( len(curr_result) != 0):
        #    return curr_result
    


    return "No moves available."

    


def putFoundation(board):
    
    # Search in drawpile
    if board.drawPile.cards:
        drawPileCard = board.drawPile.cards[-1]
        count_foundation = 0
        for foundation in stateful_board.foundations:
            count_foundation += 1
            if(allowedMoveFoundation(drawPileCard, foundation)):
                foundation.cards.append(drawPileCard)
                stateful_board.cardsLeftDeckDrawPile -= 1
                return "Move " + str(drawPileCard) + " from drawpile " + "to foundation:" + str(count_foundation) 

    # Search in columns
    count_columns = 0
    for c in board.columns:
        count_columns += 1
        count_foundation = 0
        for foundation in stateful_board.foundations:
            count_foundation += 1
            if c.cards:
                if allowedMoveFoundation(c.cards[-1], foundation):
                    #return "Move " +  str(c.cards[-1].rank) + str(c.cards[-1].suit) +  "  from column: " + str(count_columns) + " to foundation:" + str(count_foundation) + "."
                    curr_card =  c.cards[-1]
                    board.moveCard(c, c.cards[-1], foundation)
                    stateful_board.cardsLeftColumns[count_columns-1] -= 1
                    #stateful_board.foundations = board.foundations
                    #stateful_board.foundations[count_foundation-1].append
                    #return "Move " + str(c.cards[-1]) +   " from column: " + str(count_columns) + " to foundation: " + str(count_foundation) + "." 
                    return "Move " + str(curr_card) +   " from column: " + str(count_columns) + " to foundation: " + str(count_foundation) + "." 
                #return (True, count_columns,count_foundation, c.cards[-1])
    return ""        


def putColumn(board):

    # Search in columns
    possibleFromColumn = []
    count_columns_from = 0
    for column_from in board.columns:

        count_columns_from += 1
        count_columns_to = 0


        for column_to in board.columns:
            count_columns_to += 1
            if(count_columns_from==count_columns_to):
                continue
            #for c in column_outer.cards:
            # Only the first card
            if column_from.cards:
                c = column_from.cards[0]
                if c.rank == 13 and stateful_board.columns[count_columns_from-1].isKingMovedTo:
                    continue

                if allowedMoveColumn(c, column_to):
                    possibleFromColumn.append((c, count_columns_from, count_columns_to, board.getCardsLeftColumn(count_columns_from-1)))
                    #stateful_board.cardsLeftColumns[count_columns_from-1] -= 1
                    #if(c.rank == 13):
                    #    stateful_board.columns[count_columns_to-1].isKingMovedTo = True
                    #return "Move " + str(c) +   " from column: " + str(count_columns_from) + " to column: " + str(count_columns_to) + "."
    
    # Find the best move with the most hidden cards
    if possibleFromColumn:
        bestMoveWithMostHiddenCards = max(possibleFromColumn, key = lambda item: item[3])
        (c, count_columns_from, count_columns_to, numberHiddenCards) = bestMoveWithMostHiddenCards
        stateful_board.cardsLeftColumns[count_columns_from-1] -= 1
        if(c.rank == 13):
           stateful_board.columns[count_columns_to-1].isKingMovedTo = True
        return "Move " + str(c) +   " from column: " + str(count_columns_from) + " to column: " + str(count_columns_to) + "."
        

    
    # Search in drawpile
    if board.drawPile.cards:
        drawPileCard = board.drawPile.cards[-1]
        count_column = 0
        for column in board.columns:
            count_column += 1
            if(allowedMoveColumn(drawPileCard, column)):
                stateful_board.cardsLeftDeckDrawPile -= 1
                return "Move " + str(drawPileCard) +  " from drawpile to column: " + str(count_column) 


    return ""        


def makeLastDraw(board):
    if stateful_board.cardsLeftDeckDrawPile == 3 and not stateful_board.isLastDrawMade:
        stateful_board.isLastDrawMade = True
        return "Make a draw"
    return ""

def makeDraw(board):
    if stateful_board.cardsLeftDeckDrawPile > 3:
        return "Make a draw"
    return ""

def fromFoundationToColumn(board):
    for f_idx, foundation in enumerate(board.foundations):
        if foundation.cards:
            c = foundation.cards[-1]

            for c_idx, column in enumerate(board.columns):
                if allowedMoveColumn(c, column):
                    stateful_board.isLastMoveFromFoundationToColumn = True
                    stateful_board.foundations[f_idx].cards.pop()
                    return "Move " + str(c) +  " from foundation:" + str(f_idx+1) + " to column: " + str(c_idx+1) + "."
    return ""

# def putKingToEmptyColumnIfQueenAvailable(board):
#     # Search for empty columns
#     emptyColumns = []
#     column_count = 0
#     for column in board.columns:
#         if not column.cards:
#             emptyColumns.append(column_count)
#         column_count += 1
    
#     if not emptyColumns :
#         return ""

#     # Search for kings availble to move 
#     columnWithKingsToMove = []
#     count_columns_from = 0
#     for column in board.columns:
#         count_columns_from += 1        
#         if column.cards:
#             c = column.cards[0]
#             if c.rank == 13 and not stateful_board.columns[count_columns_from-1].isKingMovedTo:
#                 columnWithKingsToMove.append((count_columns_from-1, c))

#     # Search for queen
#     for columnWithKing, kingCard in columnWithKingsToMove:
#         temp_column = Column()
#         temp_column.cards.append(kingCard)

#         for columnForPossibleQueen in board.columns:
#             if columnForPossibleQueen.cards:
#                 possibleQueen = column.cards[0]
#                 if allowedMoveColumn(possibleQueen, temp_column):
#                     stateful_board.columns[emptyColumns[0]].isKingMovedTo = True
#                     return "Move " + str(kingCard) +   " from column: " + str(columnWithKing) + " to column: " + str(emptyColumns[0]) + "." 

#     return ""
 