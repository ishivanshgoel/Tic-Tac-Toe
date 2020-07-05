import tkinter as tk
from tkinter import ttk
from logic import Logic

log=Logic("Player")
player=''

def get_player_name(player_name):
    global player
    player=player_name
    print(player_name)

class Widgets:
    def __init__(self):
        pass
 
    def configure_button(self):
        global player
        if(player=="Player1"):
            self.btn.configure(bg='red', text='X')
            player="Player2"
        elif(player=="Player2"):
            self.btn.config(bg='yellow', text='O')
            player="Player1"

    def new_grid_button(self,frame,text,width,height,bg_color,row,column):
        global log

        ## when button is clicked
        def clicked(i,j):
            print(i,j)
            print(self.btn)
            log.nums[f"{i}{j}"]="x"
            print(log.nums[f"{i}{j}"])
            self.configure_button()
            

        self.btn=tk.Button(frame,text=text,width=width,height=height,bg=bg_color,command= lambda : clicked(row,column))
        self.btn.grid(row=row, column=column)