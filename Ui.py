from cgitb import text
from wsgiref.handlers import format_date_time
from CardSelectionWindow import Instructions
from tokenize import String
import PySimpleGUI as sg
import cv2 as cv
import numpy as np
import math
from datetime import datetime
from CardRecognition.yolov5.detect import run 
from CardRecognition.ConvertPredictToBoard import convertPredictToBoard
from  View.KabaleView import display 

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

def drawColumn(CVframe, columnNumber, imgWidth, imgHeight):
    start_cord_x = round(imgWidth * (1/7 * columnNumber))
    start_cord_y = round(imgHeight * 0.25)
    color = (255, 0, 0) # blue BGR   
    stroke = 2
    if (columnNumber == 0):
        w = round(imgWidth * 1/7)
    else:
        w = round(imgWidth * (1/7 * columnNumber))
    h = round(imgHeight * .745)
    end_cord_x = start_cord_x + w
    end_cord_y = start_cord_y + h
    
    return cv.rectangle(CVframe, (round(start_cord_x), start_cord_y), (round(end_cord_x), end_cord_y), color, stroke)

def drawFoundationAndDeck(CVframe, columnNumber, imgWidth, imgHeight):
    start_cord_x = round(imgWidth * (1/7 * columnNumber))
    start_cord_y = 0
    color = (255, 0, 0) # blue BGR   
    stroke = 2
    if (columnNumber == 0):
        w = round(imgWidth * 1/7)
    else:
        w = round(imgWidth * (1/7 * columnNumber))
    h = round(imgHeight * .23)
    end_cord_x = start_cord_x + w
    end_cord_y = start_cord_y + h
    
    return cv.rectangle(CVframe, (round(start_cord_x), start_cord_y), (round(end_cord_x), end_cord_y), color, stroke)
    
# theshold the video frame to get the card
def getCard(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5,5), 0)
    ret, thresh = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    # kernal = np.ones((17,17), np.uint8)
    # thresh = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernal)
    # thresh = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernal)
    

    cv.imshow("thresh", thresh)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv.contourArea, reverse=True)
    cnt = contours[0]
    rect = cv.minAreaRect(cnt)
    box = cv.boxPoints(rect)
    
    box2 = box
    i = 0
    upperLeft, lowerRight = 0, 0
    for corners in box:
        totalXY = box[i][0] + box[i][1]
        if (totalXY < box[upperLeft][0] + box[upperLeft][1]):
            upperLeft = i
        if (totalXY > box[lowerRight][0] + box[lowerRight][1]):
            lowerRight = i
        i += 1        
    
    i = 0
    for corners in box:
        if (i == upperLeft):
            width = math.sqrt(pow(box[1][0]-box[upperLeft][0],2)+pow(box[1][1]-box[upperLeft][1],2))
        height = math.sqrt(pow(box[2][0]-box[upperLeft][0],2)+pow(box[2][1]-box[upperLeft][1],2))
    
    width = math.sqrt(pow(box[1][0]-box[0][0],2)+pow(box[1][1]-box[0][1],2))
    height = math.sqrt(pow(box[2][0]-box[0][0],2)+pow(box[2][1]-box[0][1],2))
    scale = height / width


    print (width, height)
    box = np.int0(box)
    cv.drawContours(frame, [box], -1, (0, 255, 0), 2)
    
    
    #x, y, w, h = cv.boundingRect(cnt)
    #cv.drawContours(frame, contours, -1, (0, 255, 0), 3)
    #cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv.imshow("rectangle", frame)
    cv.waitKey(1)





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

    # cap = cv.VideoCapture(1)
    cap = cv.VideoCapture(2)

    width=cap.get(3)
    height=cap.get(4)

    # start_cord_x = round(width * 1/7)
    # start_cord_y = round(height * 1/7)
    # color = (255, 0, 0) # blue BGR   
    # stroke = 2
    # w = round(width * 1/7)
    # h = round(height * .8)
    # end_cord_x = start_cord_x + w
    # end_cord_y = start_cord_y + h


    print('width, height: ', width, height) # this is to test the camara output hight and width. Will be removed later
   
    def rescale_frame(frame, percent=75):
        width = int(frame.shape[1] * percent/ 100)
        height = int(frame.shape[0] * percent/ 100)
        dim = (width, height)
        return cv.resize(frame, dim, interpolation =cv.INTER_AREA)

    def fixed_frame(frame):
        width = 1440
        height = 810
        dim = (width, height)
        return cv.resize(frame, dim, interpolation =cv.INTER_AREA)

    while True:
        event, values = window.read(timeout=20)  
        
        ret, frame = cap.read()
        #frame = cv.rotate(frame, cv.ROTATE_90_CLOCKWISE)
        #frame = cv.rotate(frame, cv.ROTATE_90_CLOCKWISE)
        
        frame_to_save = cv.resize(frame, (640,640),interpolation=cv.INTER_AREA)

        for i in range(7):
            frame = drawColumn(frame, i, width, height)
            if(i==2):
                continue
            frame = drawFoundationAndDeck(frame, i, width, height)
        
        #cv.rectangle(frame, (start_cord_x, start_cord_y), (end_cord_x, end_cord_y), color, stroke)
        #cv.rectangle(frame, (round(start_cord_x+w+20), start_cord_y), (round(end_cord_x+w+20), end_cord_y), color, stroke)
        frame75 = rescale_frame(frame, percent=75) 
        frameFixed = fixed_frame(frame)     
        
        imgbytes = cv.imencode(".png", frame)[1].tobytes()



        window["-IMAGE-"].update(data=imgbytes)



        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "NEXT STEP":
            
            currImgName = 'img/'+ str(datetime.now()).replace(" ", "_") + '.png'
            cv.imwrite(currImgName, frame_to_save)

            det, names = run(weights='CardRecognition/yolov5/best_run10_cards_with_number.pt', source=currImgName, conf_thres=0.4)
            currBoard = convertPredictToBoard(det, names)
            display(currBoard)

            print("you clicked the button")
            instruction = nextInstruction(globalmovetype)
            print(instruction)
            print(globalmovetype.value)
            window["_INSTRUCTION_"].update(instruction)

            # Made for testing the instructions message types
            if (globalmovetype.value < 3 ):
                globalmovetype = Instructions(globalmovetype.value + 1)
            elif (globalmovetype.value == 3):
                    globalmovetype = Instructions.MOVE
                
        
      

    window.close()

    

main()