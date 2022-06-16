from View.KabaleView import display
from Model.Board import Board
from Model.Deck import Deck
from Model.Card import Card
from Model.DrawPile import DrawPile
from Model.CardFactory import CardFactory
from Model.Column import Column
from Model.Foundation import Foundation
from Model.GameRules import playPhase
from AI.Algorithm import *

cardFactory = CardFactory()
cardFactory.makeCards()
cardFactory.randomizeCards()
board = Board(DrawPile(), cardFactory.cards)
board.allocateCards()
display(board)
someNode = Node(0, board)
node = treeSearchBackTracking(someNode, someNode, 5)
boo = False
while not boo:
    st = input("Press Enter or write end")
    if st == "end":
        boo = True
    display(node.board)
    someNode = Node(0, node.board)
    node = treeSearchBackTracking(someNode, someNode, 5)
    print(node.commands[-1])
for command in reversed(node.commands):
    print(str(command))