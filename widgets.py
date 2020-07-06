## widgets for game
import tkinter as tk
from tkinter import ttk
from logic import Logic

player1=Logic("Player1")
player2=Logic("Player2")
player='Player1'
game_result=None

def get_player_name(main_frame):
    global player,game_result
    player_name=tk.StringVar()
    if game_result is not None:
        global player1,player2
        player_name.set(game_result)
        game_result=None
        player1=Logic("Player1")
        player2=Logic("Player2")
    else:
        player_name.set(f"{player}'s Turn")
    print(player_name.get())
    tk.Label(main_frame,textvariable=player_name,bg='#d93253',font=("helvetica 12",12)).grid(row=7,column=1)

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
        self.frame=frame       
        ## when button is clicked
        def clicked(i,j):
            global game_result
            ## debugging
            # print(i,j)
            # print(self.btn)
            if(self.click_count==0):
                if(player=="Player1"):
                    player1.nums[f"{i}{j}"]="x"
                    print(player1.check())
                    game_result=player1.check()
                    get_player_name(self.frame)
                    self.click_count+=1
                elif(player=="Player2"):
                    player2.nums[f"{i}{j}"]="o"
                    print(player2.check())
                    game_result=player2.check()
                    get_player_name(self.frame)
                    self.click_count+=1
                self.used_by_player=player
                self.configure_button()
            else:
                print(f"Already Used by {self.used_by_player}")
        self.btn=tk.Button(frame,text=text,font="helvetica 12",width=width,height=height,bg=bg_color,command= lambda : clicked(row,column))
        self.btn.grid(row=row, column=column)