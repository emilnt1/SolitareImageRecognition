from cgitb import text
from CardSelectionWindow import Instructions
from tokenize import String
import PySimpleGUI as sg
import cv2 as cv
import numpy as np

card1 = "Queen of Spades"
columnFrom = 4
columnTo = 2
foundation = "Foundation for Spades"



moveCard = "Move " + card1 + " from coulmn " + str(columnFrom) + " to column " + str(columnTo)
noOption = "No options. Draw card from pile"
drawnCard = "Put drawn card \"" + card1 +"\" in column" + str(columnTo)
moveFoundation = "Move " + card1 + " from " + str(columnFrom) + " to " + foundation

def nextInstruction(moveType):
        if (moveType == Instructions.MOVE):
            return moveCard

        elif (moveType == Instructions.NO_OPTION):
            return noOption

        elif (moveType == Instructions.DRAW_CARD):
            return drawnCard

        elif (moveType == Instructions.FOUNDATION):
            return moveFoundation

        else:
            print("Wrong move type in the input, This should not be happening.")

def main():
    sg.theme("LightGreen")

    # Define the window layout
    layout = [
        [sg.Image(filename="", key="-IMAGE-")],
        [sg.Text("Instructuons:", justification="center", font="Roboto 15 bold",pad=((0,0),(10,0)))],
        [sg.Text("This is a dummy text", justification="center", font="Roboto 15", key="_INSTRUCTION_", pad=((0,0),(10,20)))],
        [sg.Button('NEXT STEP', pad=((0,0),(10,20)), image_filename=("BlueButton.png"),font="Raleway 15 bold", auto_size_button=True,  button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)]
        
    ]


    # Create the window and show it without the plot
    window = sg.Window("7-kabale assistant", layout,element_justification="center", location=(400, 100))
    
    globalmovetype = Instructions.MOVE

    cap = cv.VideoCapture(0)

    width=cap.get(3)
    height=cap.get(4)

    start_cord_x = round(width * 1/7)
    start_cord_y = round(height * 1/7)
    color = (255, 0, 0) # blue BGR   
    stroke = 2
    w = round(width * 1/7)
    h = round(height * .8)
    end_cord_x = start_cord_x + w
    end_cord_y = start_cord_y + h


    print('width, height: ', width, height) # this is to test the camara output hight and width. Will be removed later
   
    def rescale_frame(frame, percent=75):
        width = int(frame.shape[1] * percent/ 100)
        height = int(frame.shape[0] * percent/ 100)
        dim = (width, height)
        return cv.resize(frame, dim, interpolation =cv.INTER_AREA)

    while True:
        event, values = window.read(timeout=20)  
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "NEXT STEP":
            print("you clicked the button")
            instruction = nextInstruction(globalmovetype)
            print(instruction)
            print(globalmovetype.value)
            window["_INSTRUCTION_"].update(instruction)
            if (globalmovetype.value < 3 ):
                globalmovetype = Instructions(globalmovetype.value + 1)
        ret, frame = cap.read()
        cv.rectangle(frame, (start_cord_x, start_cord_y), (end_cord_x, end_cord_y), color, stroke)
        frame75 = rescale_frame(frame, percent=75)      

        
        imgbytes = cv.imencode(".png", frame75)[1].tobytes()
        window["-IMAGE-"].update(data=imgbytes)

        
      

    window.close()

    

main()