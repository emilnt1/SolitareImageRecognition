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
from AI.AI import *




def startGameWithBasicSetup():
    stateful_board[-1].cardsLeftDeckDrawPile = 4
    stateful_board[-1].drawPile.cards = []
    # stateful_board[-1].drawPile.cards.append(Card(8,type.H))
    # stateful_board[-1].drawPile.cards.append(Card(7,type.S))
    # stateful_board[-1].drawPile.cards.append(Card(5,type.H))
    stateful_board[-1].drawPile.cards.append(Card(5,type.H))
    stateful_board[-1].drawPile.cards.append(Card(1,type.S))

    stateful_board[-1].deck.cards = []
    # stateful_board[-1].deck.cards.append(Card(1,type.S))
    stateful_board[-1].deck.cards.append(Card(7,type.S))
    stateful_board[-1].deck.cards.append(Card(8,type.H))

    b1 = Board(DrawPile(), Deck())
    b1.columns[0].cards.append(Card(6,type.S))
    b1.columns[1].cards.append(Card(7,type.S))
    b1.columns[2].cards.append(Card(7,type.S))
    b1.columns[3].cards.append(Card(7,type.S))
    b1.columns[4].cards.append(Card(7,type.S))
    b1.columns[5].cards.append(Card(7,type.S))
    b1.columns[6].cards.append(Card(7,type.S))
    b1.drawPile.cards.append(Card(1,type.S))
    b1.mergeStatefulBoard(stateful_board[-1])
    display(b1)
    print(nextMove(b1))
    display(stateful_board[-1])

    b2 = Board(DrawPile(), Deck())
    b2.columns[0].cards.append(Card(6,type.S))
    b2.columns[1].cards.append(Card(7,type.S))
    b2.columns[2].cards.append(Card(7,type.S))
    b2.columns[3].cards.append(Card(7,type.S))
    b2.columns[4].cards.append(Card(7,type.S))
    b2.columns[5].cards.append(Card(7,type.S))
    b2.columns[6].cards.append(Card(7,type.S))
    b2.drawPile.cards.append(Card(1,type.S))
    b2.mergeStatefulBoard(stateful_board[-1])

    print(nextMove(b2))
    display(stateful_board[-1])


    b3 = Board(DrawPile(), Deck())
    b3.columns[0].cards.append(Card(6,type.S))
    b3.columns[1].cards.append(Card(7,type.S))
    b3.columns[2].cards.append(Card(7,type.S))
    b3.columns[3].cards.append(Card(7,type.S))
    b3.columns[4].cards.append(Card(7,type.S))
    b3.columns[5].cards.append(Card(7,type.S))
    b3.columns[6].cards.append(Card(7,type.S))
    b3.drawPile.cards.append(Card(5,type.H))
    b3.mergeStatefulBoard(stateful_board[-1])

    print(nextMove(b3))
    display(stateful_board[-1])

    b4 = Board(DrawPile(), Deck())
    b4.columns[0].cards.append(Card(6,type.S))
    b4.columns[1].cards.append(Card(7,type.S))
    b4.columns[2].cards.append(Card(7,type.S))
    b4.columns[3].cards.append(Card(7,type.S))
    b4.columns[4].cards.append(Card(7,type.S))
    b4.columns[5].cards.append(Card(7,type.S))
    b4.columns[6].cards.append(Card(7,type.S))
    b4.drawPile.cards.append(Card(5,type.H))
    b4.mergeStatefulBoard(stateful_board[-1])

    print(nextMove(b4))
    display(stateful_board[-1])


    # print(nextMove(b1))
    # display(stateful_board[-1])
    # print(nextMove(b1))
    # display(stateful_board[-1])
    # print(nextMove(b1))
    # display(stateful_board[-1])
    # print(nextMove(b1))
    # display(stateful_board[-1])
    # print(nextMove(b1))
    # print(nextMove(b1))
    # print(nextMove(b1))
    # print(nextMove(b1))

    # print("Expected: kun to kort tilbage på drawpile")


def testWithUnknownCard():
    stateful_board[-1].cardsLeftDeckDrawPile = 4
    stateful_board[-1].drawPile.cards = []
    # stateful_board[-1].drawPile.cards.append(Card(8,type.H))
    # stateful_board[-1].drawPile.cards.append(Card(7,type.S))
    # stateful_board[-1].drawPile.cards.append(Card(5,type.H))
    stateful_board[-1].drawPile.cards.append(Card(7,type.H))
    stateful_board[-1].drawPile.cards.append(Card(8,type.H))

    stateful_board[-1].deck.cards = []
    # stateful_board[-1].deck.cards.append(Card(1,type.S))
    stateful_board[-1].deck.cards.append(Card(-1,type.H))
    stateful_board[-1].deck.cards.append(Card(3,type.H))

    b1 = Board(DrawPile(), Deck())
    b1.columns[0].cards.append(Card(6,type.S))
    b1.columns[1].cards.append(Card(7,type.S))
    b1.columns[2].cards.append(Card(7,type.S))
    b1.columns[3].cards.append(Card(7,type.S))
    b1.columns[4].cards.append(Card(7,type.S))
    b1.columns[5].cards.append(Card(7,type.S))
    b1.columns[6].cards.append(Card(7,type.S))
    b1.drawPile.cards.append(Card(1,type.S))
    b1.mergeStatefulBoard(stateful_board[-1])
    display(b1)
    print(nextMove(b1))
    display(stateful_board[-1])

    b2 = Board(DrawPile(), Deck())
    b2.columns[0].cards.append(Card(6,type.S))
    b2.columns[1].cards.append(Card(7,type.S))
    b2.columns[2].cards.append(Card(7,type.S))
    b2.columns[3].cards.append(Card(7,type.S))
    b2.columns[4].cards.append(Card(7,type.S))
    b2.columns[5].cards.append(Card(7,type.S))
    b2.columns[6].cards.append(Card(7,type.S))
    b2.drawPile.cards.append(Card(7,type.H))
    b2.mergeStatefulBoard(stateful_board[-1])
    print(nextMove(b2))
    display(stateful_board[-1])

    b3 = Board(DrawPile(), Deck())
    b3.columns[0].cards.append(Card(6,type.S))
    b3.columns[1].cards.append(Card(7,type.S))
    b3.columns[2].cards.append(Card(7,type.S))
    b3.columns[3].cards.append(Card(7,type.S))
    b3.columns[4].cards.append(Card(7,type.S))
    b3.columns[5].cards.append(Card(7,type.S))
    b3.columns[6].cards.append(Card(7,type.S))
    b3.drawPile.cards.append(Card(9,type.H))
    b3.mergeStatefulBoard(stateful_board[-1])
    print(nextMove(b2))
    display(stateful_board[-1])

    b3 = Board(DrawPile(), Deck())
    b3.columns[0].cards.append(Card(6,type.S))
    b3.columns[1].cards.append(Card(7,type.S))
    b3.columns[2].cards.append(Card(7,type.S))
    b3.columns[3].cards.append(Card(7,type.S))
    b3.columns[4].cards.append(Card(7,type.S))
    b3.columns[5].cards.append(Card(7,type.S))
    b3.columns[6].cards.append(Card(7,type.S))
    b3.drawPile.cards.append(Card(3,type.H))
    b3.mergeStatefulBoard(stateful_board[-1])
    print(nextMove(b3))
    display(stateful_board[-1])


    b4 = Board(DrawPile(), Deck())
    b4.columns[0].cards.append(Card(6,type.S))
    b4.columns[1].cards.append(Card(7,type.S))
    b4.columns[2].cards.append(Card(7,type.S))
    b4.columns[3].cards.append(Card(7,type.S))
    b4.columns[4].cards.append(Card(7,type.S))
    b4.columns[5].cards.append(Card(7,type.S))
    b4.columns[6].cards.append(Card(7,type.S))
    b4.drawPile.cards.append(Card(1,type.S))
    b4.mergeStatefulBoard(stateful_board[-1])
    print(nextMove(b4))
    display(stateful_board[-1])


#testWithUnknownCard()   
startGameWithBasicSetup()