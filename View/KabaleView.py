def display(Board):
    cardAmount = 0
    for i in Board.columns:
        if len(i.cards) > cardAmount:
            cardAmount = len(i.cards)

    printTopRow(Board)
    print("")
    rowString = ""
    for y in range(cardAmount):
        for x in range(8):
            if y >= len(Board.columns[x].cards):
                rowString = rowString + "    "
            else:
                rowString = rowString + cardPrint(Board.columns[x].cards[y])
        print(rowString)
        rowString = ""



#    def display(Board):
#        for i in Board.columns:
#            print(Board.columns[i])
#            pass

def printTopRow(Board):
    print("[?]  " + "  " + lastElement(Board.drawPile) + "\t\t"
          + lastElement(Board.foundations[0]) + " "
          + lastElement(Board.foundations[1]) + " "
          + lastElement(Board.foundations[2]) + " "
          + lastElement(Board.foundations[3]))


def cardPrint(Card):
    if Card.rank > 9:
        return Card.suit.name + str(Card.rank) + " "
    else:
        return Card.suit.name + str(Card.rank) + "  "


def lastElement(cardObj):
    if len(cardObj.cards) == 0:
        return "[*]"
    else:
        return cardPrint(cardObj.cards[len(cardObj.cards)])
