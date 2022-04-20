from Model.Board import Board

class KabaleView(Board):

    def __init__(self):
        self.cards = []

    def display(self, Board):
        for i in Board.columns:
            print(Board.columns[1])
            print(Board.columns[2])
            print(Board.columns[3])
            print(Board.columns[4])
            print(Board.columns[5])
            print(Board.columns[6])
        pass
