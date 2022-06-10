class Node():

    def __init__(self, points, board, command):
        self.points = points
        self.board = board
        self.commands = [command]
        self.edgeNotes = []

    def getPoints(self):
        return self.points