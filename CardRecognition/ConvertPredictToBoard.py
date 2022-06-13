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
    cards = []

    # Separate to upper and lower cards.
    for *xyxy, conf, cls in reversed(det):
        xyxy_array = np.array(xyxy)
        c = int(cls)
        card = Card(int(names[c][1:]), convertSuitStrToEnum(names[c][0]))
        card.x = xyxy_array[0]
        card.y = xyxy_array[1]
        card.conf = conf

        cards.append(card)
        # Opdele til foundations and columner. 
        #if xyxy_array[1] <= 100:
        #    upper_cards.append(card)
        #else :
        #    lower_cards.append(card)

    # Divide lower cards to columns

    removeTwoGuesses(cards)

    board = Board(DrawPile(), Deck())
    for card in cards:
        if card.x <= 40.0:
            board.drawPile.cards.append(card)
        elif card.x > 40.0 and card.x <= 120.0:
            board.columns[0].cards.append(card)
        elif card.x > 120.0 and card.x <= 200.0:
            board.columns[1].cards.append(card)
        elif card.x > 200.0 and card.x <= 280.0:
            board.columns[2].cards.append(card)
        elif card.x > 280.0 and card.x <= 360.0:
            board.columns[3].cards.append(card)
        elif card.x > 360.0 and card.x <= 440.0:
            board.columns[4].cards.append(card)
        elif card.x > 440.0 and card.x <= 520.0:
            board.columns[5].cards.append(card)
        elif card.x > 520:
            board.columns[6].cards.append(card)  


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

def removeTwoGuesses(cards):
    cardsToRemove = []
    for i in range(len(cards)):
        for j in range(i + 1, len(cards)):
            if(abs((cards[i].x - cards[j].x)) < 10) and (abs(cards[i].y - cards[j].y) < 10):
                if cards[i].conf < cards[j].conf:
                    cardsToRemove.append(i)
                    print("Double guess, removing:" + str(cards[i]) + " instead of " + cards[j])
                else:
                    cardsToRemove.append(j)
                    print("Double guess, removing:" + str(cards[j]) + " instead of " + cards[i])
    for index in sorted(cardsToRemove, reverse=True):
        del cards[index]