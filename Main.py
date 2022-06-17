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

someNode = Node(0, board)
node = treeSearchBackTracking(someNode, someNode, [1, 2, 3, 4, 5, 6], 10)
for command in reversed(node.commands):
    print(str(command))
display(node.board)

