from Model.Column import Column
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

    def allocateCards(self):
        count = 1
        for i in self.columns:
            for l in range(count):
                i.push(self.deck.pop())
                count += 1
