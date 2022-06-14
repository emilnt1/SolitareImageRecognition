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
    # b1 = Board(DrawPile(), Deck())
    # b1.columns[0].cards.append(Card(6,type.D))
    # b1.columns[1].cards.append(Card(7,type.D))
    # b1.columns[2].cards.append(Card(8,type.D))
    # b1.columns[3].cards.append(Card(6,type.D))
    # b1.columns[4].cards.append(Card(3,type.D))
    # b1.columns[5].cards.append(Card(7,type.D))
    # b1.columns[6].cards.append(Card(2,type.D))
   # b1.drawPile.cards.append(Card(4,type.S))
    stateful_board.deck.cards = []
    stateful_board.deck.cards.append(Card(11, type.C))
    stateful_board.deck.cards.append(Card(13, type.H))
    stateful_board.deck.cards.append(Card(13, type.D))
    stateful_board.deck.cards.append(Card(11, type.D))
    stateful_board.drawPile.cards = []
   # nextMove(b1)
    #b1.mergeStatefulBoard(stateful_board)
    display(stateful_board)
    print(nextMove(stateful_board))
    #b1.mergeStatefulBoard(stateful_board)
    display(stateful_board)
    print(nextMove(stateful_board))
    #b1.mergeStatefulBoard(stateful_board)
    display(stateful_board)

def testMergeBoards():
    b1 = Board(DrawPile(), Deck())
    b1.columns[0].cards.append(Card(6,type.D))
    b1.columns[1].cards.append(Card(7,type.D))
    b1.columns[2].cards.append(Card(8,type.D))
    b1.columns[3].cards.append(Card(6,type.D))
    b1.columns[4].cards.append(Card(3,type.D))
    b1.columns[5].cards.append(Card(7,type.D))
    b1.columns[6].cards.append(Card(2,type.D))
    b1.drawPile.cards.append(Card(13,type.D))
    b1.mergeStatefulBoard(stateful_board)
    display(b1)
    print(nextMove(b1))
    b1.drawPile.cards = []
    b1.drawPile.cards.append(Card(13,type.H))
    b1.mergeStatefulBoard(stateful_board)
    display(b1)
    print(nextMove(b1))
    b1.drawPile.cards = []
    b1.drawPile.cards.append(Card(1,type.C))
    b1.mergeStatefulBoard(stateful_board)
    display(b1)
    print(nextMove(b1))
    b1.drawPile.cards = []
    b1.drawPile.cards.append(Card(11,type.D))
    b1.mergeStatefulBoard(stateful_board)
    display(b1)


#startGameWithBasicSetup()
testMergeBoards()