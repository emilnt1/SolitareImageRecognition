def display(Board):
    cardAmount = 0
    for i in Board.columns:
        if len(i.cards) > cardAmount:
            cardAmount = len(i.cards)

    printTopRow(Board)
    print("")
    print("c0  " + "c1  " + "c2  " + "c3  " + "c4  " + "c5  " + "c6  ")
    print(str(Board.getCardsLeftColumn(0)) + "   " + 
            str(Board.getCardsLeftColumn(2)) +"   " + 
            str(Board.getCardsLeftColumn(1)) +"   " + 
            str(Board.getCardsLeftColumn(3)) +"   " + 
            str(Board.getCardsLeftColumn(4)) +"   " + 
            str(Board.getCardsLeftColumn(5)) +"   " + 
            str(Board.getCardsLeftColumn(6)))
    print("-------------------------------")
    rowString = ""
    for y in range(cardAmount):
        for x in range(7):
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
    #print("[?]  " + "  " + lastElement(Board.drawPile) + "\t\t"
    print("["+ str(Board.cardsLeftDeckDrawPile) + " total]  " + "  " + lastElement(Board.drawPile) + "\t\t"
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
        return cardPrint(cardObj.cards[-1])
