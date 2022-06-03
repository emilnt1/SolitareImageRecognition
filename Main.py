from View.KabaleView import display
from Model.Board import Board
from Model.Deck import Deck
from Model.DrawPile import DrawPile
from Model.CardFactory import CardFactory

gameOver = False
cardFactory = CardFactory()
cardFactory.makeCards()
cardFactory.randomizeCards()
board = Board(DrawPile(), cardFactory.cards)
board.allocateCards()
display(board)
