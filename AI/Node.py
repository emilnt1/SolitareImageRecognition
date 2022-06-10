class Node():

    def __init__(self, points, board, command):
        self.points = points
        self.board = board
        self.commands = []
        newCommand = [command]
        self.commands.extend(command)

    def getPoints(self):
        return self.points