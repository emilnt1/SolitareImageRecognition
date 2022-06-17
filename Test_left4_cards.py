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
from AI.Algorithm import *




def startGameWithBasicSetup():
    stateful_board[-1].cardsLeftDeckDrawPile = 4
    stateful_board[-1].drawPile.cards = []
    stateful_board[-1].drawPile.cards.append(Card(8,type.H))
    stateful_board[-1].drawPile.cards.append(Card(7,type.S))
    stateful_board[-1].drawPile.cards.append(Card(5,type.H))

    stateful_board[-1].deck.cards = []
    stateful_board[-1].deck.cards.append(Card(1,type.S))

    b1 = Board(DrawPile(), Deck())
    b1.columns[0].cards.append(Card(6,type.S))
    b1.columns[1].cards.append(Card(7,type.S))
    b1.columns[2].cards.append(Card(7,type.S))
    b1.columns[3].cards.append(Card(7,type.S))
    b1.columns[4].cards.append(Card(7,type.S))
    b1.columns[5].cards.append(Card(7,type.S))
    b1.columns[6].cards.append(Card(7,type.S))
    b1.drawPile.cards.append(Card(5,type.H))
    b1.mergeStatefulBoard(stateful_board[-1])
    display(b1)
    arrayOfFunctions = [2, 5, 4]
    node = Node(0, b1)
    accomplishednode = treeSearchBackTracking(node, node, arrayOfFunctions, 7)
    succesArray = getArrayOfMoves(accomplishednode)
    for succesNode in reversed(succesArray):
        display(succesNode.board)
        print(succesNode.commands[0])
    print("Expected: kun to kort tilbage på drawpile")

    
    
startGameWithBasicSetup()