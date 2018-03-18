from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint

#global variable
ActivePlayer=1
#lists
p1=[] #what player 1 selected.
p2=[] #what player 2 selected.

root=Tk()
root.title('Tic Tac Toe player 1')

style=ttk.Style()
style.theme_use('classic')

bu1=ttk.Button(root,text=' ')
bu1.grid(row=0,column=0,ipadx=20,ipady=20)
bu1.config(command=lambda :buttonClick(1))

bu2=ttk.Button(root,text=' ')
bu2.grid(row=0,column=1,ipadx=20,ipady=20)
bu2.config(command=lambda :buttonClick(2))

bu3=ttk.Button(root,text=' ')
bu3.grid(row=0,column=2,ipadx=20,ipady=20)
bu3.config(command=lambda :buttonClick(3))

bu4=ttk.Button(root,text=' ')
bu4.grid(row=1,column=0,ipadx=20,ipady=20)
bu4.config(command=lambda :buttonClick(4))

bu5=ttk.Button(root,text=' ')
bu5.grid(row=1,column=1,ipadx=20,ipady=20)
bu5.config(command=lambda :buttonClick(5))

bu6=ttk.Button(root,text=' ')
bu6.grid(row=1,column=2,ipadx=20,ipady=20)
bu6.config(command=lambda :buttonClick(6))

bu7=ttk.Button(root,text=' ')
bu7.grid(row=2,column=0,ipadx=20,ipady=20)
bu7.config(command=lambda :buttonClick(7))

bu8=ttk.Button(root,text=' ')
bu8.grid(row=2,column=1,ipadx=20,ipady=20)
bu8.config(command=lambda :buttonClick(8))

bu9=ttk.Button(root,text=' ')
bu9.grid(row=2,column=2,ipadx=20,ipady=20)
bu9.config(command=lambda :buttonClick(9))

def buttonClick(id):
    global ActivePlayer,p1,p2
    if(ActivePlayer==1):
        setLayout(id,"X")
        p1.append(id)
        root.title('Tic Tac Toe player 2')
        ActivePlayer=2
        print("p1={}".format(p1))
        autoPlay()
    elif(ActivePlayer==2):
        setLayout(id, "0")
        p2.append(id)
        root.title('Tic Tac Toe player 1')
        ActivePlayer = 1
        print("p2={}".format(p2))
    checkWinner()

def checkWinner():
    winner=-1 #no one
    # if((1 in p1) and (2 in p1) and (3 in p1)):
    #     winner=1
    # if ((1 in p2) and (2 in p2) and (3 in p2)):
    #     winner = 2
    # if ((4 in p1) and (5 in p1) and (6 in p1)):
    #     winner = 1
    # if ((4 in p2) and (5 in p2) and (6 in p2)):
    #     winner = 2
    # if ((7 in p1) and (8 in p1) and (9 in p1)):
    #     winner = 1
    # if ((7 in p2) and (8 in p2) and (9 in p2)):
    #     winner = 2
    # if ((1 in p1) and (4 in p1) and (7 in p1)):
    #     winner = 1
    # if ((1 in p2) and (4 in p2) and (7 in p2)):
    #     winner = 2
    # if ((2 in p1) and (5 in p1) and (8 in p1)):
    #     winner = 1
    # if ((2 in p2) and (5 in p2) and (8 in p2)):
    #     winner = 2
    # if ((3 in p1) and (6 in p1) and (9 in p1)):
    #     winner = 1
    # if ((3 in p2) and (6 in p2) and (9 in p2)):
    #     winner = 2
    if ((1 in p1) and (5 in p1) and (9 in p1)):
        winner = 1
    if ((1 in p2) and (5 in p2) and (9 in p2)):
        winner = 2
    if ((3 in p1) and (5 in p1) and (7 in p1)):
        winner = 1
    if ((3 in p2) and (5 in p2) and (7 in p2)):
        winner = 2
    for i in range(1,8,3):
        #range(start,stop,step)
        if((i in p1) and (i+1 in p1) and (i+2 in p1)):
            winner=1
        if ((i in p2) and (i + 1 in p2) and (i + 2 in p2)):
            winner = 2
    for i in range(1,4):
        if((i in p1) and (i+3 in p1) and (i+6 in p1)):
            winner=1
        if ((i in p2) and (i + 3 in p2) and (i + 6 in p2)):
            winner = 2
    if(winner==1):
        messagebox.showinfo(title='congrats!',message='You Won!')
        exit()
    elif(winner == 2):
        messagebox.showinfo(title='Retry!', message='You Lost!')
        exit()

def setLayout(id,activeSymbol):
    if(id==1):
        bu1.config(text=activeSymbol)
        bu1.state(['disabled'])
    elif(id==2):
        bu2.config(text=activeSymbol)
        bu2.state(['disabled'])
    elif (id == 3):
        bu3.config(text=activeSymbol)
        bu3.state(['disabled'])
    elif (id == 4):
        bu4.config(text=activeSymbol)
        bu4.state(['disabled'])
    elif (id == 5):
        bu5.config(text=activeSymbol)
        bu5.state(['disabled'])
    elif (id == 6):
        bu6.config(text=activeSymbol)
        bu6.state(['disabled'])
    elif (id == 7):
        bu7.config(text=activeSymbol)
        bu7.state(['disabled'])
    elif (id == 8):
        bu8.config(text=activeSymbol)
        bu8.state(['disabled'])
    elif (id == 9):
        bu9.config(text=activeSymbol)
        bu9.state(['disabled'])

def autoPlay():
    global p1,p2
    emptyCells=[]
    for cell in range(9):
        if(not((cell+1 in p1)or(cell+1 in p2))):
            emptyCells.append(cell+1)
    if(len(emptyCells)==0):
        messagebox.showinfo(title='NO winner!',message="Play again!")
        exit()
    if(len(p1)==1):
       randomIndex=randint(0,len(emptyCells)-1)
       buttonClick(emptyCells[randomIndex])
    elif ((1 in p2) and (2 in p2) and (3 in emptyCells)):
        buttonClick(3)
    elif ((2 in p2) and (3 in p2) and (1 in emptyCells)):
        buttonClick(1)
    elif ((1 in p2) and (3 in p2) and (2 in emptyCells)):
        buttonClick(2)
    elif ((1 in p2) and (4 in p2) and (7 in emptyCells)):
        buttonClick(7)
    elif ((1 in p2) and (7 in p2) and (4 in emptyCells)):
        buttonClick(4)
    elif ((4 in p2) and (7 in p2) and (1 in emptyCells)):
        buttonClick(1)
    elif ((4 in p2) and (5 in p2) and (6 in emptyCells)):
        buttonClick(6)
    elif ((5 in p2) and (6 in p2) and (4 in emptyCells)):
        buttonClick(4)
    elif ((4 in p2) and (6 in p2) and (5 in emptyCells)):
        buttonClick(5)
    elif ((7 in p2) and (8 in p2) and (9 in emptyCells)):
        buttonClick(9)
    elif ((8 in p2) and (9 in p2) and (7 in emptyCells)):
        buttonClick(7)
    elif ((7 in p2) and (9 in p2) and (8 in emptyCells)):
        buttonClick(8)
    elif ((2 in p2) and (5 in p2) and (8 in emptyCells)):
        buttonClick(8)
    elif ((5 in p2) and (8 in p2) and (2 in emptyCells)):
        buttonClick(2)
    elif ((2 in p2) and (8 in p2) and (5 in emptyCells)):
        buttonClick(5)
    elif ((3 in p2) and (6 in p2) and (9 in emptyCells)):
        buttonClick(9)
    elif ((6 in p2) and (9 in p2) and (3 in emptyCells)):
        buttonClick(3)
    elif ((3 in p2) and (9 in p2) and (6 in emptyCells)):
        buttonClick(6)
    elif ((1 in p2) and (5 in p2) and (9 in emptyCells)):
        buttonClick(9)
    elif ((5 in p2) and (9 in p2) and (1 in emptyCells)):
        buttonClick(1)
    elif ((1 in p2) and (9 in p2) and (5 in emptyCells)):
        buttonClick(5)
    elif ((3 in p2) and (5 in p2) and (7 in emptyCells)):
        buttonClick(7)
    elif ((5 in p2) and (7 in p2) and (3 in emptyCells)):
        buttonClick(3)
    elif ((3 in p2) and (7 in p2) and (5 in emptyCells)):
        buttonClick(5)
    elif((1 in p1)and(2 in p1)and (3 in emptyCells)):
        buttonClick(3)
    elif ((2 in p1) and (3 in p1) and (1 in emptyCells)):
        buttonClick(1)
    elif((1 in p1)and(3 in p1)and (2 in emptyCells)):
        buttonClick(2)
    elif ((1 in p1) and (4 in p1) and (7 in emptyCells)):
        buttonClick(7)
    elif ((1 in p1) and (7 in p1) and (4 in emptyCells)):
        buttonClick(4)
    elif ((4 in p1) and (7 in p1) and (1 in emptyCells)):
        buttonClick(1)
    elif ((4 in p1) and (5 in p1) and (6 in emptyCells)):
        buttonClick(6)
    elif ((5 in p1) and (6 in p1) and (4 in emptyCells)):
        buttonClick(4)
    elif ((4 in p1) and (6 in p1) and (5 in emptyCells)):
        buttonClick(5)
    elif ((7 in p1) and (8 in p1) and (9 in emptyCells)):
        buttonClick(9)
    elif ((8 in p1) and (9 in p1) and (7 in emptyCells)):
        buttonClick(7)
    elif ((7 in p1) and (9 in p1) and (8 in emptyCells)):
        buttonClick(8)
    elif ((2 in p1) and (5 in p1) and (8 in emptyCells)):
        buttonClick(8)
    elif ((5 in p1) and (8 in p1) and (2 in emptyCells)):
        buttonClick(2)
    elif ((2 in p1) and (8 in p1) and (5 in emptyCells)):
        buttonClick(5)
    elif ((3 in p1) and (6 in p1) and (9 in emptyCells)):
        buttonClick(9)
    elif ((6 in p1) and (9 in p1) and (3 in emptyCells)):
        buttonClick(3)
    elif ((3 in p1) and (9 in p1) and (6 in emptyCells)):
        buttonClick(6)
    elif ((1 in p1) and (5 in p1) and (9 in emptyCells)):
        buttonClick(9)
    elif ((5 in p1) and (9 in p1) and (1 in emptyCells)):
        buttonClick(1)
    elif ((1 in p1) and (9 in p1) and (5 in emptyCells)):
        buttonClick(5)
    elif ((3 in p1) and (5 in p1) and (7 in emptyCells)):
        buttonClick(7)
    elif ((5 in p1) and (7 in p1) and (3 in emptyCells)):
        buttonClick(3)
    elif ((3 in p1) and (7 in p1) and (5 in emptyCells)):
        buttonClick(5)
    elif ((1 in p1) and (2 in p1) and (3 in emptyCells)):
        buttonClick(3)
    elif ((2 in p1) and (3 in p1) and (1 in emptyCells)):
        buttonClick(1)
    elif ((1 in p1) and (3 in p1) and (2 in emptyCells)):
        buttonClick(2)
    elif ((1 in p1) and (4 in p1) and (7 in emptyCells)):
        buttonClick(7)
    elif ((1 in p1) and (7 in p1) and (4 in emptyCells)):
        buttonClick(4)
    elif ((4 in p1) and (7 in p1) and (1 in emptyCells)):
        buttonClick(1)
    elif ((4 in p1) and (5 in p1) and (6 in emptyCells)):
        buttonClick(6)
    elif ((5 in p1) and (6 in p1) and (4 in emptyCells)):
        buttonClick(4)
    elif ((4 in p1) and (6 in p1) and (5 in emptyCells)):
        buttonClick(5)
    elif ((7 in p1) and (8 in p1) and (9 in emptyCells)):
        buttonClick(9)
    elif ((8 in p1) and (9 in p1) and (7 in emptyCells)):
        buttonClick(7)
    elif ((7 in p1) and (9 in p1) and (8 in emptyCells)):
        buttonClick(8)
    elif ((2 in p1) and (5 in p1) and (8 in emptyCells)):
        buttonClick(8)
    elif ((5 in p1) and (8 in p1) and (2 in emptyCells)):
        buttonClick(2)
    elif ((2 in p1) and (8 in p1) and (5 in emptyCells)):
        buttonClick(5)
    elif ((3 in p1) and (6 in p1) and (9 in emptyCells)):
        buttonClick(9)
    elif ((6 in p1) and (9 in p1) and (3 in emptyCells)):
        buttonClick(3)
    elif ((3 in p1) and (9 in p1) and (6 in emptyCells)):
        buttonClick(6)
    elif ((1 in p1) and (5 in p1) and (9 in emptyCells)):
        buttonClick(9)
    elif ((5 in p1) and (9 in p1) and (1 in emptyCells)):
        buttonClick(1)
    elif ((1 in p1) and (9 in p1) and (5 in emptyCells)):
        buttonClick(5)
    elif ((3 in p1) and (5 in p1) and (7 in emptyCells)):
        buttonClick(7)
    elif ((5 in p1) and (7 in p1) and (3 in emptyCells)):
        buttonClick(3)
    elif ((3 in p1) and (7 in p1) and (5 in emptyCells)):
        buttonClick(5)
    else:
        randomIndex = randint(0, len(emptyCells) - 1)
        buttonClick(emptyCells[randomIndex])



root.mainloop()