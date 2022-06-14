from Model.Debugger import *
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
from Model.Debugger import *



def testBasicBoard():
    b1 = Board(DrawPile(), Deck())
    b1.columns[0].cards.append(Card(4,type.D))
    b1.columns[1].cards.append(Card(5,type.D))
    b1.columns[2].cards.append(Card(6,type.H))
    b1.columns[3].cards.append(Card(7,type.C))
    b1.columns[4].cards.append(Card(8,type.S))
    b1.columns[5].cards.append(Card(9,type.S))
    b1.columns[6].cards.append(Card(10,type.S))
    b1.drawPile.cards.append(Card(11,type.S))

    stateful_board.foundations[0].cards.append(Card(1,type.H))
    stateful_board.foundations[1].cards.append(Card(1,type.C))
    stateful_board.foundations[2].cards.append(Card(1,type.D))
    stateful_board.foundations[3].cards.append(Card(1,type.S))
    b1.mergeStatefulBoard(stateful_board)
    display(b1)

    menu(b1)


testBasicBoard()