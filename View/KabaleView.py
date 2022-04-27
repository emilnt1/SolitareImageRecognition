def display(Board):
    cardAmount = 0
    for i in Board.columns:
        if len(i.cards) > cardAmount:
            cardAmount = len(i.cards)

    rowString = ""
    for y in range(cardAmount):
        for x in range(8):
            if y >= len(Board.columns[x].cards):
                rowString = rowString + "    "
            else:
                rowString = rowString + cardPrint(Board.columns[x].cards[y])
        print(rowString)
        rowString = ""


def cardPrint(Card):
    if
    return str(Card.rank) + Card.suit.name + " "
