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

## Statefull board only with foundations
stateful_board = Board(DrawPile(), None)
cardsLeftDeckDrawPile = 24
isLastDrawMade = False

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

    moves = [makeLastDraw, putFoundation, putColumn, makeDraw]

    for move in moves:
        curr_result = move(board)
        if ( len(curr_result) != 0):
            return curr_result
    


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
                cardsLeftDeckDrawPile -= 1
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
                    #stateful_board.foundations = board.foundations
                    #stateful_board.foundations[count_foundation-1].append
                    #return "Move " + str(c.cards[-1]) +   " from column: " + str(count_columns) + " to foundation: " + str(count_foundation) + "." 
                    return "Move " + str(curr_card) +   " from column: " + str(count_columns) + " to foundation: " + str(count_foundation) + "." 
                #return (True, count_columns,count_foundation, c.cards[-1])
    return ""        


def putColumn(board):

    # Search in columns
    count_columns_outer = 0
    for column_outer in board.columns:

        count_columns_outer += 1
        count_columns_inner = 0


        for column_inner in board.columns:
            count_columns_inner += 1
            if(count_columns_outer==count_columns_inner):
                continue
            #for c in column_outer.cards:
            # Only the first card
            if column_outer.cards:
                c = column_outer.cards[0]
                if c.rank == 13 and stateful_board.columns[count_columns_outer-1].isKingMovedTo:
                    continue

                if allowedMoveColumn(c, column_inner):
                    if(c.rank == 13):
                        stateful_board.columns[count_columns_inner-1].isKingMovedTo = True
                    return "Move " + str(c) +   " from column: " + str(count_columns_outer) + " to column: " + str(count_columns_inner) + "."

    
    # Search in drawpile
    if board.drawPile.cards:
        drawPileCard = board.drawPile.cards[-1]
        count_column = 0
        for column in board.columns:
            count_column += 1
            if(allowedMoveColumn(drawPileCard, column)):
                cardsLeftDeckDrawPile -= 1
                return "Move " + str(drawPileCard) +  " from drawpile to column: " + str(count_column) 


    return ""        


def makeLastDraw(board):
    if cardsLeftDeckDrawPile == 3 and not isLastDrawMade:
        isLastDrawMade = True
        return "Make a draw"

def makeDraw(board):
    if cardsLeftDeckDrawPile > 3:
        return "Make a draw"

#def putKingToEmptyColumn(board):
    # if there is an empty column. search king