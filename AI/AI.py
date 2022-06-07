from Model.Card import Card
from Model.DrawPile import DrawPile
from Model.CardFactory import CardFactory
from View.KabaleView import display
from Model.Board import Board
from Model.SuitType import concludeFromString
from Model.SuitType import SuitType
from Model.GameRules import *

def nextMove(board):
    ##isAceFound, count_columns,count_foundation, card = findAce(board)
    curr_move = findAce(board)
    if ( len(curr_move) != 0):
        return  curr_move

    


def findAce(board):
    count_columns = 0
    for c in board.columns:
        count_columns += 1
        count_foundation = 0
        for foundation in board.foundations:
            count_foundation = +1
            if allowedMoveFoundation(c.cards[-1], foundation):
                return "Move " +  str(c.cards[-1].rank) + str(c.cards[-1].suit) +  "  from column: " + str(count_columns) + " to foundation:" + str(count_foundation) + "." 
                #return (True, count_columns,count_foundation, c.cards[-1])
            

