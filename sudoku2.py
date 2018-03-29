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


afficher_sol(s, 8)

fenetre.mainloop()