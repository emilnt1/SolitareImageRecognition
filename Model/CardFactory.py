import random
from Model.SuitType import SuitType as type
from Model.Card import Card

initCards = []


def makeCards():
    for i in range(0, 13):
        initCards.append(Card(i, type.HEART))
        initCards.append(Card(i, type.CLUBS))
        initCards.append(Card(i, type.SPADES))
        initCards.append(Card(i, type.DIAMONDS))

    return initCards


def randomizeCards(cards):
    random.shuffle(cards)
