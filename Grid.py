from tkinter import *
import tkinter.ttk
class GameGrid(tkinter.Frame):
    gameGrid = {}
    def revealNumber(self,idx):
        (button,row,column) = self.gameGrid[idx]
        button.configure(image = PhotoImage(file="Sprites/empty.png",width=16,height=16))
        button.state = "disabled"
    def __init__(self,root,dims):
        super().__init__(master = root)
        counter = 0
        for i in range(dims[0]):
            for j in range(dims[1]):
                button = Button(self,image = PhotoImage(file="Sprites/grid.png",width=16,height=16),command=lambda c=counter: self.revealNumber(c))
                button.grid(row=i,column=j)
                self.gameGrid[counter] = (button,i,j)
            counter+=1
    def get(self):
        return self.entry.get()