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
    b1 = Board(DrawPile(), Deck())
    b1.columns[0].cards.append(Card(2,type.D))
    b1.columns[1].cards.append(Card(1,type.D))
    b1.columns[2].cards.append(Card(1,type.H))
    b1.columns[3].cards.append(Card(1,type.C))
    b1.columns[4].cards.append(Card(1,type.S))
    b1.columns[5].cards.append(Card(2,type.S))
    b1.columns[6].cards.append(Card(3,type.S))
    b1.drawPile.cards.append(Card(4,type.S))
    b1.mergeStatefulBoard(stateful_board[-1])

    print("################ Initial Prev stateful board ################")
    display(prev_stateful_boards[-1])
    print("################ Initial  Curr stateful board ################")
    display(stateful_board[-1]) # Skulle være efter move, så D1 i foundations 

    print(nextMove(b1))
    print("################ After 1. move Prev stateful board ################")
    display(prev_stateful_boards[-1])
    print("################ After 1. move  Curr stateful board ################")
    display(stateful_board[-1]) # Skulle være efter move, så D1 i foundations 


    b2 = Board(DrawPile(), Deck())
    b2.columns[0].cards.append(Card(2,type.D))
    b2.columns[2].cards.append(Card(1,type.H))
    b2.columns[3].cards.append(Card(1,type.C))
    b2.columns[4].cards.append(Card(1,type.S))
    b2.columns[5].cards.append(Card(2,type.S))
    b2.columns[6].cards.append(Card(3,type.S))
    b2.drawPile.cards.append(Card(4,type.S))
    b2.mergeStatefulBoard(stateful_board[-1])
    print(nextMove(b2))
    print("################ After 2. move Prev stateful board ################")
    display(prev_stateful_boards[-1])
    print("################ After 2. move Curr stateful board ################")
    display(stateful_board[-1])
    

def testDrawPile():
    b1 = Board(DrawPile(), Deck())
    b1.columns[0].cards.append(Card(8,type.D))
    b1.columns[1].cards.append(Card(8,type.D))
    b1.columns[2].cards.append(Card(8,type.H))
    b1.columns[3].cards.append(Card(8,type.C))
    b1.columns[4].cards.append(Card(8,type.S))
    b1.columns[5].cards.append(Card(8,type.S))
    b1.columns[6].cards.append(Card(8,type.S))
    b1.drawPile.cards.append(Card(1,type.S))
    b1.mergeStatefulBoard(stateful_board[-1])

    print("################ Initial Prev stateful board ################")
    display(prev_stateful_boards[-1])
    print("################ Initial  Curr stateful board ################")
    display(stateful_board[-1]) # Skulle være efter move, så D1 i foundations 

    print(nextMove(b1))
    print("################ After 1. move Prev stateful board ################")
    display(prev_stateful_boards[-1])
    print("################ After 1. move  Curr stateful board ################")
    display(stateful_board[-1]) # Skulle være efter move, så D1 i foundations 


    b2 = Board(DrawPile(), Deck())
    b2.columns[0].cards.append(Card(8,type.D))
    b2.columns[2].cards.append(Card(8,type.H))
    b2.columns[3].cards.append(Card(8,type.C))
    b2.columns[4].cards.append(Card(8,type.S))
    b2.columns[5].cards.append(Card(8,type.S))
    b2.columns[6].cards.append(Card(8,type.S))
    b2.drawPile.cards.append(Card(2,type.S))
    b2.mergeStatefulBoard(stateful_board[-1])
    print(nextMove(b2))
    print("################ After 2. move Prev stateful board ################")
    display(prev_stateful_boards[-1])
    print("################ After 2. move Curr stateful board ################")
    display(stateful_board[-1])

    undoMove()
    #### Lave nyt board med fixet drawpile eller lignende
    ### Merge og undoMove
    print("################ After 2. move Prev stateful board ################")
    display(prev_stateful_boards[-1])
    print("################ After 2. move Curr stateful board ################")
    display(stateful_board[-1])


def testUndo():
    b1 = Board(DrawPile(), Deck())
    b1.columns[0].cards.append(Card(8,type.D))
    b1.columns[1].cards.append(Card(8,type.D))
    b1.columns[2].cards.append(Card(1,type.H))
    b1.columns[3].cards.append(Card(8,type.C))
    b1.columns[4].cards.append(Card(8,type.S))
    b1.columns[5].cards.append(Card(8,type.S))
    b1.columns[6].cards.append(Card(8,type.S))
    b1.drawPile.cards.append(Card(5,type.S))
    
    ##### CLICK NEXT MOVE
    b1.mergeStatefulBoard(stateful_board[-1])
    display(b1)
    print(nextMove(b1))


    b2 = Board(DrawPile(), Deck())
    b2.columns[0].cards.append(Card(8,type.D))
    b2.columns[1].cards.append(Card(8,type.D))
    b2.columns[2].cards.append(Card(4,type.H))
    b2.columns[3].cards.append(Card(8,type.C))
    b2.columns[4].cards.append(Card(8,type.S))
    b2.columns[5].cards.append(Card(8,type.S))
    b2.columns[6].cards.append(Card(8,type.S))
    b2.drawPile.cards.append(Card(1,type.S))
    ##### CLICK NEXT MOVE 
    b2.mergeStatefulBoard(stateful_board[-1])
    display(b2)
    print(nextMove(b2))  ##### HER OPDAGER MAN AT DER EN FEJL I INSTRUKTIONER
    


   
    
    b3 = Board(DrawPile(), Deck())
    b3.columns[0].cards.append(Card(8,type.D))
    b3.columns[1].cards.append(Card(8,type.D))
    b3.columns[2].cards.append(Card(4,type.H))
    b3.columns[3].cards.append(Card(8,type.C))
    b3.columns[4].cards.append(Card(8,type.S))
    b3.columns[5].cards.append(Card(8,type.S))
    b3.columns[6].cards.append(Card(8,type.S))
    b3.drawPile.cards.append(Card(5,type.S)) 


    ### CLICK UNDO / EDIT 
    undoMove()
    b3.mergeStatefulBoard(stateful_board[-1])
    display(b3)
    print(nextMove(b3))
    
    

    ##### FORVENTET MAKE A DRAW OG FOUNDATIONS HAR KUN H1



#startGameWithBasicSetup()
#testDrawPile()
testUndo()
