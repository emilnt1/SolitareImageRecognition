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
    b1 = Board(DrawPile(), None)
    b1.columns[0].cards.append(Card(2,type.D))
    b1.columns[1].cards.append(Card(1,type.D))
    b1.columns[2].cards.append(Card(1,type.H))
    b1.columns[3].cards.append(Card(1,type.C))
    b1.columns[4].cards.append(Card(1,type.S))
    b1.columns[5].cards.append(Card(2,type.S))
    b1.columns[6].cards.append(Card(3,type.S))
    b1.drawPile.cards.append(Card(4,type.S))
    display(b1)
    print(nextMove(b1))
    b1.mergeStatefulBoard(stateful_board[-1])
    display(b1)
    
def lenNoneTypeBug():
    stateful_board[-1].cardsLeftDeckDrawPile = 2
    print(nextMove(stateful_board[-1]))
    

def moveFromFoundationToColumn():
    stateful_board[-1].cardsLeftDeckDrawPile = 2
    stateful_board[-1].foundations[0].cards.append(Card(9,type.H))
    stateful_board[-1].foundations[0].cards.append(Card(10,type.H))
    b1 = Board(DrawPile(), None)
    b1.columns[0].cards.append(Card(13,type.C))
    b1.columns[0].cards.append(Card(12,type.D))
    b1.columns[0].cards.append(Card(11,type.C))
    b1.columns[1].cards.append(Card(9,type.C))
    b1.columns[2].cards.append(Card(13,type.D))
    b1.columns[3].cards.append(Card(13,type.D))
    b1.columns[4].cards.append(Card(13,type.D))
    b1.columns[5].cards.append(Card(13,type.D))
    b1.columns[6].cards.append(Card(13,type.D))
    b1.mergeStatefulBoard(stateful_board[-1])
    display(b1)
    print(nextMove(b1))
    display(stateful_board[-1])

    b2 = Board(DrawPile(), None)
    b2.columns[0].cards.append(Card(13,type.C))
    b2.columns[0].cards.append(Card(12,type.D))
    b2.columns[0].cards.append(Card(11,type.C))
    b2.columns[0].cards.append(Card(10,type.H))
    b2.columns[1].cards.append(Card(9,type.C))
    b2.columns[2].cards.append(Card(13,type.D))
    b2.columns[3].cards.append(Card(13,type.D))
    b2.columns[4].cards.append(Card(13,type.D))
    b2.columns[5].cards.append(Card(13,type.D))
    b2.columns[6].cards.append(Card(13,type.D))
    b2.mergeStatefulBoard(stateful_board[-1])
    display(b2)
    print(nextMove(b2))
    display(stateful_board[-1])

    b3 = Board(DrawPile(), None)
    b3.columns[0].cards.append(Card(13,type.C))
    b3.columns[0].cards.append(Card(12,type.D))
    b3.columns[0].cards.append(Card(11,type.C))
    b3.columns[0].cards.append(Card(10,type.H))
    b3.columns[0].cards.append(Card(9,type.C))
    b3.columns[1].cards.append(Card(1,type.D))
    b3.columns[2].cards.append(Card(13,type.D))
    b3.columns[3].cards.append(Card(13,type.D))
    b3.columns[4].cards.append(Card(13,type.D))
    b3.columns[5].cards.append(Card(13,type.D))
    b3.columns[6].cards.append(Card(13,type.D))
    b3.mergeStatefulBoard(stateful_board[-1])
    display(b3)
    print(nextMove(b3))
    display(stateful_board[-1])


  #  if stateful_board.foundations[0].cards[0].rank == 9 and
  #      Card(9,type.H) and stateful_board.foundations[1].cards[0] == Card(1,type.D):
  #      print("PASSED")


def kingMovesTwoTime():
    stateful_board[-1].cardsLeftColumns = [0,0,2,2,2,2,2]
    b1 = Board(DrawPile(), None)
    b1.mergeStatefulBoard(stateful_board[-1])
    b1.columns[2].cards.append(Card(2,type.H))
    b1.columns[3].cards.append(Card(6,type.C))
    b1.columns[4].cards.append(Card(8,type.S))
    b1.columns[5].cards.append(Card(10,type.S))
    b1.columns[6].cards.append(Card(12,type.S))
    b1.drawPile.cards.append(Card(13,type.S))
   # display(b1)
    print(nextMove(b1))
    display(b1)

    b2 = Board(DrawPile(), None)
    b2.mergeStatefulBoard(stateful_board[-1])
    b2.columns[0].cards.append(Card(13,type.S))
    b2.columns[2].cards.append(Card(2,type.H))
    b2.columns[3].cards.append(Card(6,type.C))
    b2.columns[4].cards.append(Card(8,type.S))
    b2.columns[5].cards.append(Card(10,type.S))
    b2.columns[6].cards.append(Card(12,type.S))
  #  display(b2)
    print(nextMove(b2))
    display(b2)

startGameWithBasicSetup()
#lenNoneTypeBug()
#moveFromFoundationToColumn()
#kingMovesTwoTime()