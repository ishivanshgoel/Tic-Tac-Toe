## main driver programme
import tkinter as tk
from tkinter import ttk
from widgets import Widgets,get_player_name

window=tk.Tk()
window.title("TikTak-Toe")
window.geometry("500x500")


player=tk.StringVar()
player_name=tk.Label(textvariable=player,fg="red")
player_name.pack()
if(player.get()==''):
    player.set("Player1")

main_frame=tk.Frame(master=window,bg='cyan',height=250, width=250)
main_frame.pack()

### buttons
for i in range(3):
    for j in range(3):
        btn1=Widgets()
        btn1.new_grid_button(main_frame,f"{i},{j}",10,5,'blue',i,j)

## player name
get_player_name(player.get())

window.mainloop()