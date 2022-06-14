from Model.Board import Board
from Model.SuitType import SuitType as type
from Model.Card import Card
from Model.Column import Column
from View.KabaleView import display
from AI.AI import stateful_board[-1]


def menu(board):
    finished = "Y"
    while(finished == "Y"):
        
        option = input("Please enter one of the following commands:\ncc: change card\ncf: correct foundation count\ncd: change deck\nhc: change hidden column counts\nHere: ")

        if option == "cc":
            changeCard(board)

        elif option == "cf":
            correctFoundationCount()

        elif option == "cd":
            changeDeck()

        elif option == "hc":
            changeHiddenColumnCount()

        board.mergeStatefulBoard(stateful_board[-1])

        display(board)

        finished = input("Do you want to continue Y/N: ") 




def changeDeck():
    deckChange = input("Enter integer to change deck count?: ")

    if deckChange[0] == "-" :
        toInt = int(deckChange[1:])
        stateful_board[-1].changeCardsLeftDeckDrawPile(-toInt) 
    else: 
        toInt = int(deckChange)
        stateful_board[-1].changeCardsLeftDeckDrawPile(toInt)

    
    

def changeHiddenColumnCount():
    column = int(input("Which column do you want to change?: "))
    changeHiddenColumnNmb = input("Enter integer to change column count: ")

    if changeHiddenColumnNmb[0] == "-" :
        toInt = int(changeHiddenColumnNmb[1:])
        stateful_board[-1].changeCardsLeftColumns(column,-toInt)
    else: 
        toInt = int(changeHiddenColumnNmb)
        stateful_board[-1].changeCardsLeftColumns(column,toInt)


def changeCard(board):
    position = input("Please position of the card you want to change (column, row \"xy\"): ")
    newCardString = input("Please enter which card you want to change it to: ")
    newSuit = newCardString[0]
    
    
    newRank = int(newCardString[1:])


    x = int(position[0])
    y = int(position[1])

    if(newSuit == "H"):
        newCard = Card(newRank, type.H)
            
    elif (newSuit == "C"):
        newCard = Card(newRank, type.C)

    elif (newSuit == "S"):
        newCard = Card(newRank, type.S)

    elif (newSuit == "D"):
        newCard = Card(newRank, type.D)

    column = board.columns[x-1]
    column.cards[y-1] = newCard

def correctFoundationCount():

    newFoundation = input("Please enter the foundation you want to correct:")
    newFoundationInt = int(newFoundation)
    choice = input("Y for pop N for push:")
    newSuit= ""
    newRank = -1
       

    if(choice == "Y"):
        stateful_board[-1].foundations[newFoundationInt-1].cards.pop()
    elif(choice == "N"):
        
        newCardString = input("Please enter the card you want to change it to:")
        newSuit = newCardString[0]

        newRank = newCardString[1:]

        if(newSuit == "H"):
            newCard = Card(newRank, type.H)
                
        elif (newSuit == "C"):
            newCard = Card(newRank, type.C)

        elif (newSuit == "S"):
            newCard = Card(newRank, type.S)

        elif (newSuit == "D"):
            newCard = Card(newRank, type.D)
        
        
        stateful_board[-1].foundations[newFoundationInt-1].cards.append(newCard)


            


    

