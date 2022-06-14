class Node():

    def __init__(self, points, board):
        self.points = points
        self.board = board
        self.commands = []
        self.edgeNodes = []
        self.previousNode = None
        self.draws = 0

    def getPoints(self):
        return self.points