from tkinter import *
import tkinter.ttk
import random
import sys
import time


class Timer(Frame):
    @staticmethod
    def format_time(elap):
        hours = int(elap / 3600)
        minutes = int(elap / 60 - hours * 60.0)
        seconds = int(elap - hours * 3600.0 - minutes * 60.0)
        hseconds = int((elap - hours * 3600.0 - minutes * 60.0 - seconds) * 10)
        return '%02d:%02d:%02d:%1d' % (hours, minutes, seconds, hseconds)
class CustomButton(Frame):
    def left_click(self,event):
        self.revealNumber([],False,0)
    def right_click(self,event):
        self.revealNumber([],True,0)
    def gameLoss(self):
        (button,row,column) = self.gameGrid.gameGrid[self.id]
        gameState = self.engine.gameGrid[self.id]
        if gameState[1] == True:
            if gameState[4] == False and gameState[3] == False:
                button.label.configure(image = self.photoDic[13])
        else:
            if self.flagged == 0:
                if gameState[1] == False:
                    button.label.configure(image = self.photoDic[12])
        self.pressed = 1
    def revealNumber(self,currentRecurseStack : list,flag :bool,debug):
        (button,row,column) = self.gameGrid.gameGrid[self.id]
        if(self.pressed == 0):
            if (flag):
                if(self.flagged == 0):
                    button.label.configure(image = self.photoDic[9])
                    self.gameGrid.gameGrid[self.id] = (button,row,column)
                    engData = self.engine.gameGrid[self.id]
                    self.engine.gameGrid[self.id] = (engData[0],engData[1],engData[2],False,False)
                    self.flagged =1
                elif(self.flagged == 1):
                    button.label.configure(image = self.photoDic[11])
                    self.gameGrid.gameGrid[self.id] = (button,row,column)
                    engData = self.engine.gameGrid[self.id]
                    self.engine.gameGrid[self.id] = (engData[0],engData[1],engData[2],True,False)
                    self.flagged = 0
            elif self.engine.gameGrid[self.id][1] == True and self.flagged == 1:
                button.label.configure(image = self.photoDic[10])
                self.gameGrid.gameGrid[self.id] = (button,row,column)
                engData = self.engine.gameGrid[self.id]
                self.engine.gameGrid[self.id] = (engData[0],engData[1],engData[2],engData[3],True)
                self.pressed = 1
            elif self.flagged == 1:
            
                button.label.configure(image = self.photoDic[self.engine.gameGrid[self.id][2]])
                engData = self.engine.gameGrid[self.id]
                self.engine.gameGrid[self.id] = (engData[0],engData[1],engData[2],engData[3],True)
                self.pressed = 1
            #calculate pressing the rest of the buttons
                if self.engine.gameGrid[self.id][2] == 0:
                    for currRow in range(3):
                        calRow = (row -1) + currRow
                        for currCol in range(3):
                            calCol = (column-1) + currCol
                            if not (calRow < 0 or calRow >= self.engine.rowLen):
                                if not( calCol < 0 or calCol >= self.engine.colLen):
                                    currentRecurseStack.append(self.id)
                                    
                                    if not (self.gameGrid.gameGrid[calRow* self.engine.rowLen + calCol][0].id in currentRecurseStack):
                                        self.gameGrid.gameGrid[calRow* self.engine.rowLen + calCol][0].revealNumber(currentRecurseStack,flag,debug+1)
                self.gameGrid.gameGrid[self.id] = (button,row,column)
                engData = self.engine.gameGrid[self.id]
                self.engine.gameGrid[self.id] = (engData[0],engData[1],engData[2],engData[3],True)
            gameState = self.engine.checkGameState()
            self.gameGrid.gameOver(gameState)
    def __init__(self,root,number,engine,photoDic,gameGrid,timer):
        super().__init__(master = root,width=32,height=32)
        self.timer = timer
        self.photoDic = photoDic
        self.id = number
        self.engine = engine
        self.label = Label(self,image = self.photoDic[9])
        self.label.grid()
        self.label.bind("<Button-1>",self.left_click)
        self.label.bind("<Button-2>",self.right_click)
        self.label.bind("<Button-3>",self.right_click)
        self.flagged = 1
        self.gameGrid = gameGrid
        self.pressed = 0

class GameGrid(Frame):
    def gameOver(self,state):
        if state == 0:
            return
        if state == 1:
            #winning
            for idx in self.gameGrid:
                button = self.gameGrid[idx]
            return
        if state == 2:
            #losing
            for idx in self.gameGrid:
                (button,row,column) = self.gameGrid[idx]
                button.gameLoss()
            return
        return
    def __init__(self,root,dims,timer):
        super().__init__(master = root)
        
        self.rowconfigure(0,weight=1)
        self.columnconfigure((0,1),weight=1)
        self.timer = timer

        
        
        self.photoDic = {}
        self.photoDic[0] = PhotoImage(file="Sprites/empty.png",width=32,height=32)
        self.photoDic[1] = PhotoImage(file="Sprites/grid1.png",width=32,height=32)
        self.photoDic[2] = PhotoImage(file="Sprites/grid2.png",width=32,height=32)
        self.photoDic[3] = PhotoImage(file="Sprites/grid3.png",width=32,height=32)
        self.photoDic[4] = PhotoImage(file="Sprites/grid4.png",width=32,height=32)
        self.photoDic[5] = PhotoImage(file="Sprites/grid5.png",width=32,height=32)
        self.photoDic[6] = PhotoImage(file="Sprites/grid6.png",width=32,height=32)
        self.photoDic[7] = PhotoImage(file="Sprites/grid7.png",width=32,height=32)
        self.photoDic[8] = PhotoImage(file="Sprites/grid8.png",width=32,height=32)
        self.photoDic[9] = PhotoImage(file="Sprites/Grid.png",width=32,height=32)
        self.photoDic[10] = PhotoImage(file="Sprites/mineClicked.png",width=32,height=32)
        self.photoDic[11] = PhotoImage(file="Sprites/flag.png",width=32,height=32)
        self.photoDic[12] = PhotoImage(file="Sprites/mineFalse.png",width=32,height=32)
        self.photoDic[13] = PhotoImage(file="Sprites/mine.png",width=32,height=32)
        self.gameGrid = {}
        self.engine = gameEngine(timer)
        self.engine.spawnNewGame(dims)
        self.spawnGrid(dims,self.photoDic[10])

    def spawnGrid(self,dims,photo):
        counter = 0
        global flag
        for i in range(dims[0]):
            for j in range(dims[1]):
                button = CustomButton(self,counter,self.engine,self.photoDic,self,self.timer)
                button.grid(row=i,column=j)
                self.gameGrid[counter] = (button,i,j)
                counter+=1

    
                
        
class gameEngine():
    def __init__(self,timer):
        self.timer = timer
        return
    def spawnNewGame(self,args):
        self.rowLen = args[0]
        self.colLen = args[1]
        self.numBombs = args[2]
        self.gameGrid = {}
        counter = 0
        for i in range(self.rowLen):
            for j in range(self.colLen):
                self.gameGrid[counter] = (counter,False,0,False,False)
                counter+=1
        for bomb in range(self.numBombs):
            flag = False
            while not flag:
                i = random.randint(0,self.rowLen-1)
                j = random.randint(0,self.colLen-1)
                currLoc = self.gameGrid[i*self.rowLen + j]
                if currLoc[1] == False:
                    flag = True
                    currLoc = (currLoc[0],True,-1,False,False)
                    self.gameGrid[i*self.rowLen + j] = currLoc
                    # Do calculations for surrounding spaces
                    
                    for row in range(3):
                        currRow = i-1 + row
                        for col in range(3):
                            currCol = j-1 + col
                            if not( currRow < 0 or currRow >= self.rowLen):
                                if not (currCol<0 or currCol >= self.colLen):
                                    if not (row == 1 and col ==1):
                                        currLoc = self.gameGrid[currRow * self.rowLen + currCol]
                                        if currLoc[1] != True:
                                            currLoc = (currLoc[0],currLoc[1],currLoc[2]+1,False,False)
                                            self.gameGrid[currRow * self.rowLen + currCol] = currLoc
    def checkGameState(self):
        clickedCounter = 0
        flagCounter = 0
        for bombNum in self.gameGrid:
            bomb = self.gameGrid[bombNum]
            if(bomb[1] == True and bomb[4] == True):
                return 2
            if(bomb[4] == True):
                clickedCounter += 1
            if bomb[3] == True:
                flagCounter += 1
        if clickedCounter == self.rowLen * self.colLen - self.numBombs and flagCounter == self.numBombs:
            return 1
        return 0
sys.setrecursionlimit(10000)
gridSize = (5,5)
root = tkinter.Tk()
flag = False
flagPhoto = PhotoImage(file="Sprites/flag.png",width=32,height=32)
newGame = Button(root,text="New Game",command=lambda : startNewGame()).grid(row = 0,column=0)
timer = Timer(root)
timer.grid(row=0,column=1)
gridG = GameGrid(root,(5,5,5),timer).grid(row=1,column=0,columnspan=2)

def startNewGame():
    global gridG
    gridG = GameGrid(root,(5,5,5),timer).grid(row=1,column=0,columnspan=2)

root.mainloop()
