import Column as Column
import Foundation as Foundation
import DrawPile as Drawpile
import Deck as Deck


class Board:
    columns = []
    foundations = []

    def __init__(self, Drawpile, Deck):
        self.columns = [Column, Column, Column, Column, Column, Column, Column]
        self.foundations = [Foundation, Foundation, Foundation, Foundation]
        self.drawPile = Drawpile
        self.deck = Deck