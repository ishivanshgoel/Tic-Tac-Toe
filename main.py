## main driver programme
import tkinter as tk
from tkinter import ttk
from tkinter import font
from widgets import Widgets,get_player_name

window=tk.Tk()

def startPage():
    main_frame=tk.Frame(master=window,bg='#d93253',height=250, width=250)
    main_frame.grid(row=3,column=0)
    ### buttons
    for i in range(3):
        for j in range(3):
            btn1=Widgets()
            btn1.new_grid_button(main_frame,f"{i},{j}",10,5,'#d93253',i,j)
    get_player_name(main_frame)

### front page of app
window.title("Tik-Tac-Toe")
window.geometry("600x600")
window.configure(bg='#d93253')
window.resizable(0,0)
first_page=tk.Frame(master=window,bg='#d93253')
first_page.grid(row=0,column=0,pady=10,padx=125)

top_icon=tk.PhotoImage(file='icons/tictactoe.png')
tk.Label(master=first_page,image=top_icon).grid(row=0,column=1)

label=tk.Label(master=first_page,text="Click button below to start the Game!!",bg='#d93253',font="helvetica 12")
label.grid(row=1,column=1)

btn=tk.Button(first_page,text='Start Game',bg='#d93253',font=("helvetica 12",14,'bold'),command=startPage)
btn.grid(row=2,column=1)

window.mainloop()