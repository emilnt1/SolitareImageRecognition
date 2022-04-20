from Model.Board import Board

class KabaleView(Board):

    def __init__(self):
        self.cards = []

    def display(self, Board):
        for i in Board.columns:
            print(Board.columns[1])

        pass
