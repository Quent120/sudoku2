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