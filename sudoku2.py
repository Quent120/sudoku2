from tkinter import *
from copy import*
from math import sqrt
import time

#E : sol : liste contenant la grille de SUDOKU troué
#S : affiche dans un canvas de la grille en cours de remplissage
def resolution_sudoku(sol):
    p = 0
    N = int(sqrt(len(sol)+1)) - 1
    global est_arrive
    est_arrive = False
    global sol2
    placer(p,N,sol)
    
fenetre=Tk()  
cadre=Frame(fenetre,borderwidth=4)

texte1=Label(fenetre,text="Sudoku",fg="blue",font=ecriture)
texte1.pack(side="top")

canevas=Canvas(fenetre,height=500,width=500,bg="white")  #création
canevas.pack()  


fenetre.mainloop()