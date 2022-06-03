from re import match
from Model.Board import *
from Model.Card import *
from Model.Column import *
from Model.Deck import *
from Model.DrawPile import *
from Model.Foundation import *
from Model.SuitType import SuitType as type
import numpy as np

def convertToMatrix(det, names):

    upper_cards = []
    lower_cards = []

    # Separate to upper and lower cards.
    for *xyxy, conf, cls in reversed(det):
        xyxy_array = np.array(xyxy)
        c = int(cls)
        card = Card()
        card.suit = convertSuitStrToEnum(names[c][0]) # TODO: Should it be number?
        card.rank = names[c][1:]
        card.x = xyxy_array[0]
        card.y = xyxy_array[1]
     #   card.conf = conf.item()

        # Opdele til foundations and columner. 
        if xyxy_array[1] <= 100:
            upper_cards.append(card)
        else :
            lower_cards.append(card)

    # Divide lower cards to columns
    column1 = Column()
    column2 = Column()
    column3 = Column()
    column4 = Column()
    column5 = Column()
    column6 = Column()
    column7 = Column()
    for lower_card in lower_cards:
        if lower_card.x <= 50.0:
            column1.cards.append(lower_card)
        elif lower_card.x > 50.0 and lower_card.x <= 140.0:
            column2.cards.append(lower_card)
        elif lower_card.x > 140.0 and lower_card.x <= 230.0:
            column3.cards.append(lower_card)
        elif lower_card.x > 230.0 and lower_card.x <= 320.0:
            column4.cards.append(lower_card)
        elif lower_card.x > 320.0 and lower_card.x <= 420.0:
            column5.cards.append(lower_card)
        elif lower_card.x > 420.0 and lower_card.x <= 510.0:
            column6.cards.append(lower_card)
        elif lower_card.x > 510:
            column7.cards.append(lower_card)    


    board = Board()
    board.columns.append(column1)
    board.columns.append(column2)
    board.columns.append(column3)
    board.columns.append(column4)
    board.columns.append(column5)
    board.columns.append(column6)
    board.columns.append(column7)

    for c in board.columns:
        c.cards.sort(key=lambda x : x.y)

    # Add foundations and DrawPile
    foundation1 = Foundation()
    foundation2 = Foundation()
    foundation3 = Foundation()
    foundation4 = Foundation()

    for upper_card in upper_cards:
            if upper_card.x <= 230.0:
                board.drawPile.cards.append(upper_card)
            elif upper_card.x > 230.0 and upper_card.x <= 330.0:
                foundation1.cards.append(upper_card)
            elif upper_card.x > 330.0 and upper_card.x <= 420.0:
                foundation2.cards.append(upper_card)
            elif upper_card.x > 420.0 and upper_card.x <= 510.0:
                foundation3.cards.append(upper_card)
            elif upper_card.x > 510.0:
                foundation4.cards.append(upper_card)
                

    board.foundations.append(foundation1)
    board.foundations.append(foundation2)
    board.foundations.append(foundation3)
    board.foundations.append(foundation4)

    
def convertSuitStrToEnum(suit):
    return {
        'H' : type.H,
        'S' : type.S,
        'R' : type.D,
        'K' : type.C
    }.get(suit)


    # match suit:
    #     case 'H':
    #         return type.H
    #     case 'S':
    #         return type.S
    #     case 'R':
    #         return type.D
    #     case 'K':
    #         return type.C 


