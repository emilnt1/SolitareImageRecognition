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
commands = starter(board)

