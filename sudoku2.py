from tkinter import *
from copy import*
from math import sqrt
import time

#E : sol : liste contenant la grille de SUDOKU troué
#S : affiche dans un canvas de la grille en cours de remplissage
def resolution_sudoku(sol):
    p = 0
    placer(p,sol)
    
def placer(p, sol):
    if(p==81):
        print(sol)
    else:
        if(sol[p] == 0):
            for i in range (1,10):
                sol[p] = i
                afficher_sol(sol,8)
                if(ajout_possible(p,sol)):
                    placer(p+1,sol)
                sol.pop()
        else:
            placer(p+1,sol)
           

def ajout_possible(p,sol):
    Ok = True

    
    
def ligne(p, sol):
    W=[]
    for i in range(81):
        if p//9 == i//9:
            W.append(i)
    for i in W:
        if sol[i] == sol[p] and p != i:
            return False
    return True

    
    
def colonne(p, sol):
     W=[]
     for i in range(0,81):
        if p%9 == i%9:
            W.append(i)
     for i in W:
        if sol[i] == sol[p] and p != i:
            return False
     return True

def region(p,sol):
    
    
    
#E :sol : liste du SUDOKU 
#   N : longueur d'une ligne
#S :affiche en sortie une fenetre represantant graphiquement le SUDOKU en fonction de sol
def afficher_sol(sol, N):
    time.sleep(0)
    canvas.delete(ALL) #efface tout pour remplir pour le sol suivant
    for i in range(N+1):
        canvas.create_line((450//(N+1))*i,0,(450//(N+1))*i, 450, fill = 'gray')
        canvas.create_line(0,(450//(N+1))*i, 450, (450//(N+1))*i, fill = 'gray')

    for i in range(int(sqrt(N+1))):
        canvas.create_line((450//int(sqrt(N+1)))*i,0,(450//int(sqrt(N+1)))*i, 450, fill = 'black')
        canvas.create_line(0,(450//int(sqrt(N+1)))*i, 450, (450//int(sqrt(N+1)))*i, fill = 'black')
    
    for i in range(N+1):
        for j in range(N+1):
            if(sol[i*(N+1)+j] != 0):
                canvas.create_text(25+50*j, 25+50*i, text=sol[i*(N+1)+j])
    
    fenetre.update()
    
s = [0, 8, 7, 0, 0, 0, 5, 2, 0, 
9, 1, 0, 5, 0, 2, 0, 4, 6,
2, 0, 0, 0, 0, 0, 0, 0, 7,
0, 9, 0, 0, 2, 0, 0, 1, 0,
0, 0, 0, 1, 0, 6, 0, 0, 0,
0, 4, 0, 0, 9, 0, 0, 8, 0,
6, 0, 0, 0, 0, 0, 0, 0, 3,
5, 7, 0, 3, 0, 1, 0, 6, 8,
0, 3, 8, 0, 0, 0, 9, 5, 0]


    
    
    
    
fenetre=Tk()  
cadre=Frame(fenetre,borderwidth=4)

canvas= Canvas(fenetre,height=450,width=450,bg="white")  #création
canvas.pack()  

resolution_sudoku(s)
afficher_sol(s, 8)

fenetre.mainloop()