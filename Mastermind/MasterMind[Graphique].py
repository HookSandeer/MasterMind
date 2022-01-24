##### Programme writen by Antonin Michon ;
### MasterMind Tkinter v2.1

from tkinter import*
from random import randint, choices

# Fuction :
def homepage():
    # Windows create : 
    window = Tk()
    #Windows Config :
    window.title("MasterMind -- Le Jeu")
    window.geometry("1280x720")
    window.minsize(720, 480)
    window.config(background='#000000')
    # Frame :
    all = Frame(window, bg='#000000')
    right = Frame(all, bg='#000000')
    left = Frame(all, bg='#000000')
    top = Frame(all, bg='#000000')
    bottom = Frame(all, bg='#000000')
    # Text :
    label_title = Label(window, text="MasterMind -- Le Jeu\nV2.1", font=("Arial", 25), bg='#000000', fg='#FFFFFF' )
    label_title.pack(side=TOP)
    level_choice = Label(right, text="Choix du Niveau : ", font=("Arial", 20), bg='#000000', fg='#FFFFFF')
    level_choice.grid(row=0, column=0)
    level_sep = Label(right, text="=================", font=("Arial", 10), bg='#000000', fg='#FFFFFF')
    level_sep.grid(row=2, column=0)
    # Level select :
    lev1 = Button(right, text="Facile", bg='#FFFFFF', fg='#000000', command=level1)
    lev1.grid(row=1, column=0)
    lev2 = Button(right, text="Difficile", bg='#FFFFFF', fg='#000000')
    lev2.grid(row=3, column=0)

    # Program Graphic:
    all.pack(expand=YES)
    right.pack(side=RIGHT)
    left.pack(side=LEFT)
    top.pack(side=TOP)
    bottom.pack(side=BOTTOM)

    # Menu :

    menu_bar = Menu(window)
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Quitter", command=window.quit)
    menu_bar.add_cascade(label="Option", menu=file_menu)


    # Screen :
    window.config(menu=menu_bar)
    window.mainloop()

def level1():
    # Windows create :
    win1 = Tk()
    # Windows config :
    win1.title("MasterMind -- Level1")
    win1.geometry("1280x720")
    win1.minsize(720, 480)
    win1.config(background='#5cb638')
    


    # Screen :
    win1.mainloop()


homepage()