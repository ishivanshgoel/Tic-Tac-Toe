## main driver programme
import tkinter as tk
from tkinter import ttk
from tkinter import font
# import PIL.Image
# import PIL.ImageTk
from widgets import Widgets,get_player_name

window=tk.Tk()

def startPage():
    # window.title("TikTak-Toe")
    # window.geometry("500x500")
    main_frame=tk.Frame(master=window,bg='cyan',height=250, width=250)
    main_frame.grid(row=3,column=0)


    # player=tk.StringVar()
    # player_name=tk.Label(textvariable=player,fg="red")
    # player_name.grid(row=4,column=0)
    # if(player.get()==''):
    #     player.set("Player1")


    ### buttons
    for i in range(3):
        for j in range(3):
            btn1=Widgets()
            btn1.new_grid_button(main_frame,f"{i},{j}",10,5,'#d93253',i,j)

    ## player name
    get_player_name("Player1")

# violet color
#bf36c9

### front page of app
window.title("TikTak-Toe")
window.geometry("500x500")
window.configure(bg='#d93253')
window.resizable(0,0)
first_page=tk.Frame(master=window,bg='#d93253')
first_page.grid(row=0,column=0,pady=10,padx=55)



top_icon=tk.PhotoImage(file='icons/tictactoe.png')
tk.Label(master=first_page,image=top_icon).grid(row=0,column=1)

label=tk.Label(master=first_page,text="Tik-Tac_Toe",bg='#d93253',font="helvetica 12")
label.grid(row=1,column=1)

btn=tk.Button(first_page,text='Start Game',bg='#d93253',font="helvetica 12",command=startPage)
btn.grid(row=2,column=1)

window.mainloop()