from re import match
from Model.Board import *
from Model.Card import *
from Model.Column import *
from Model.Deck import *
from Model.DrawPile import *
from Model.Foundation import *
from Model.SuitType import SuitType as type
import numpy as np

def convertPredictToBoard(det, names):
    columns = []

    # Separate to upper and lower cards.
    for *xyxy, conf, cls in reversed(det):
        xyxy_array = np.array(xyxy)
        c = int(cls)
        card = Card(int(names[c][1:]), convertSuitStrToEnum(names[c][0]))
        card.x = xyxy_array[0]
        card.y = xyxy_array[1]

        columns.append(card)
        # Opdele til foundations and columner. 
        #if xyxy_array[1] <= 100:
        #    upper_cards.append(card)
        #else :
        #    lower_cards.append(card)

    # Divide lower cards to columns

    board = Board(DrawPile(), Deck())
    for columns in columns:
        if columns.x <= 40.0:
            board.drawPile.cards.append(columns)
        elif columns.x > 40.0 and columns.x <= 120.0:
            board.columns[0].cards.append(columns)
        elif columns.x > 120.0 and columns.x <= 200.0:
            board.columns[1].cards.append(columns)
        elif columns.x > 200.0 and columns.x <= 280.0:
            board.columns[2].cards.append(columns)
        elif columns.x > 280.0 and columns.x <= 360.0:
            board.columns[3].cards.append(columns)
        elif columns.x > 360.0 and columns.x <= 440.0:
            board.columns[4].cards.append(columns)
        elif columns.x > 440.0 and columns.x <= 520.0:
            board.columns[5].cards.append(columns)
        elif columns.x > 520:
            board.columns[6].cards.append(columns)  


    for c in board.columns:
        c.cards.sort(key=lambda x : x.y)

    # Add foundations and DrawPile

    # for upper_card in columns:
    #         if upper_card.x <= 230.0:
    #             board.drawPile.cards.append(upper_card)
    #         elif upper_card.x > 230.0 and upper_card.x <= 330.0:
    #             board.foundations[0].cards.append(upper_card)
    #         elif upper_card.x > 330.0 and upper_card.x <= 420.0:
    #             board.foundations[1].cards.append(upper_card)
    #         elif upper_card.x > 420.0 and upper_card.x <= 510.0:
    #             board.foundations[2].cards.append(upper_card)
    #         elif upper_card.x > 510.0:
    #             board.foundations[3].cards.append(upper_card)
                
    return board
    
def convertSuitStrToEnum(suit):
    return {
        'H' : type.H,
        'S' : type.S,
        'R' : type.D,
        'K' : type.C
    }.get(suit)
