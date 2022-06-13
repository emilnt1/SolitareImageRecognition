from asyncio.windows_events import NULL
from Model.Board import Board
from Model.SuitType import SuitType as type
from Model.Card import Card
from Model.Column import Column
import Ui


class Debugger():
    board = Ui
    
    
    def menu(self, board, statefulBoard):
        while(finished == NULL):
            option = input("Please enter one of the following commands:\ncc:  change card\ncf: correct foundation count\ndc: change deck count")

            if option == "cc":
                self.changeCard(board)

            elif option == "cf":
                self.correctFoundationCount(statefulBoard)

        



    def changeCard(board):
        position = input("Please position of the card you want to change (column, row \"xy\":")
        newCardString = input("Please enter which card you want to change it to:")
        newSuit = newCardString.index(0)
        if(newCardString.index(2) != NULL):
            newRank = newCardString.index(1,2)
        else: 
            newRank = newCardString.index(1)


        x = position.index(0)
        y = position.index(1)
        if(newSuit == "H"):
            newCard = Card(newRank, type.H)
                
        elif (newSuit == "C"):
            newCard = Card(newRank, type.C)

        elif (newSuit == "S"):
            newCard = Card(newRank, type.S)

        elif (newSuit == "D"):
            newCard = Card(newRank, type.D)

        column = board.columns[x-1]
        card = newCard

    def correctFoundationCount(statefulBoard):
        newFoundation = input("Please enter the foundation you want to correct:")
        choice = input("Y for pop N for push:")
        if(choice == "N"):
            newCardString = input("Please enter the card you want to change it to:")


        newSuit = newCardString.index(0)
        foundationNumber = newFoundation.index(0)
        
        if(newSuit == "H"):
            newCard = Card(newRank, type.H)
                
        elif (newSuit == "C"):
            newCard = Card(newRank, type.C)

        elif (newSuit == "S"):
            newCard = Card(newRank, type.S)

        elif (newSuit == "D"):
            newCard = Card(newRank, type.D)
        
        if(newCardString.index(2) != NULL):
            newRank = newCardString.index(1,2)
        else: 
            newRank = newCardString.index(1)
        if
            statefulBoard.foundations[newFoundation-1].cards.pop()




    
               


        
 
