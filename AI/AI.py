from Model.Card import Card
from Model.DrawPile import DrawPile
from Model.CardFactory import CardFactory
from View.KabaleView import display
from Model.Board import Board
from Model.SuitType import concludeFromString
from Model.SuitType import SuitType
from Model.GameRules import *
from Model.DrawPile import DrawPile
from Model.Deck import Deck

## Statefull board
stateful_board = Board(DrawPile(), None)

def nextMove(board):
    ## Merge board fra ML and stateful_board
   # curr_move = ""
    ##isAceFound, count_columns,count_foundation, card = findAce(board)
        #curr_move = putFoundation(board)
    #if ( len(curr_move) != 0):
    #    return  curr_move
    #

    moves = [putFoundation]
    
    for move in moves:
        curr_result = move(board)
        if ( len(curr_result) != 0):
            return curr_result
    
    return "No moves available."

    


def putFoundation(board):
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

