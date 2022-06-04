from Model.CardFactory import makeCards, randomizeCards, initCards
from Model.Board import Board

playing = True

cards = makeCards()
randomizeCards(cards)
board = Board()
board.makeGame(cards)


def display():
    length = checkLargestColumnLength()
    for i in range(length):
        print(board.columns[0].cards[i])
        print(board.columns[1].cards[i])
        print(board.columns[2].cards[i])
        print(board.columns[3].cards[i])
        print(board.columns[4].cards[i])
        print(board.columns[5].cards[i])
        print(board.columns[6].cards[i] + "\n")


def checkLargestColumnLength():
    length = 0
    for i in range(board.columns):
        if len(board.columns[i].cards) > length:
            length = len(board.columns[i].cards)

    return length


display()
