from Model.Column import Column
from Model.Foundation import Foundation
from Model.DrawPile import DrawPile
from Model.Card import Card


class Board:

    def __init__(self):
        self.columns = [Column, Column, Column, Column, Column, Column, Column]
        self.foundations = [Foundation, Foundation, Foundation, Foundation]

    def makeGame(self, cards):
        for i in self.columns:
            i.cards.append(cards.pop)
            for q in range(2):
                i.cards.append(cards.pop)
            for q in range(3):
                i.cards.append(cards.pop)
            for q in range(4):
                i.cards.append(cards.pop)
            for q in range(5):
                i.cards.append(cards.pop)
            for q in range(6):
                i.cards.append(cards.pop)
            for q in range(7):
                i.cards.append(cards.pop)

        DrawPile.cards = cards
