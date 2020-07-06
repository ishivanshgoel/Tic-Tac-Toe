## widgets for game
import tkinter as tk
from tkinter import ttk
from logic import Logic

player1=Logic("Player1")
player2=Logic("Player2")
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
            self.btn.configure(bg='#9636c9', text='X')
            player="Player2"
        elif(player=="Player2"):
            self.btn.config(bg='#5ed194', text='O')
            player="Player1"

    def new_grid_button(self,frame,text,width,height,bg_color,row,column):
        global player1,player2
        self.click_count=0
        ## when button is clicked
        def clicked(i,j):
            ## debugging
            print(i,j)
            print(self.btn)
            if(self.click_count==0):
                print(f"Click count {self.click_count}")
                if(player=="Player1"):
                    player1.nums[f"{i}{j}"]="x"
                    print(player1.check())
                    self.click_count+=1
                    
                elif(player=="Player2"):
                    player2.nums[f"{i}{j}"]="o"
                    print(player2.check())
                    self.click_count+=1
                self.used_by_player=player
                self.configure_button()
            else:
                print(f"Already Used by {self.used_by_player}")
            

        self.btn=tk.Button(frame,text=text,width=width,height=height,bg=bg_color,command= lambda : clicked(row,column))
        self.btn.grid(row=row, column=column)