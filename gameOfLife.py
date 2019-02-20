from progpainter import *
from random import randint
from copy import deepcopy


def init(self): # N'est executé qu'une seule fois au départ
    self.q = 5 # exemple d'initiation de variable
    self.grid = [[randint(0,11)//10 for x in range(50)] for y in range(50)] # grille templi aléatoirement
    self.tmpgrid = [[0 for x in range(50)] for y in range(50)] # grille temporaire vide
    self.resize(500, 500) # taille de la fenetre

def draw(self): # Fonction repeter 30 fois par seconde

    pencolor("blue") # Couleur du pinceau

    for i in range(1,len(self.grid)-1): # Parcours de la grille
        for j in range(1,len(self.grid[0])-1):
            if self.grid[i][j] == 1: rectangle((i *10, j*10)) # Affichage

            neighbour_alive = count_alive(self.grid, i ,j) # Compte les voisins vivant
            if neighbour_alive == 3: # Condition du jeu de la vie
                self.tmpgrid[i][j] = 1
            elif self.grid[i][j]==1 and neighbour_alive == 2:
                self.tmpgrid[i][j] = self.grid[i][j]
            else:
                self.tmpgrid[i][j] = 0

    self.grid = deepcopy(self.tmpgrid) # Copy Profonde


def count_alive(grid, x, y):
    return grid[x-1][y-1] + grid[x-1][y] + grid[x-1][y+1] + grid[x+1][y-1] +\
    grid[x+1][y] + grid[x+1][y+1] + grid[x][y-1] + grid[x][y+1]


if __name__ == '__main__': # Ne pas ou peu toucher
    Win._draw = draw  # Associe la fonction a repeter
    Win._init = init # Associe la fonction executé une seule fois au départ
    w = Win("Game of Life - ProgPainter Example") # Création de la fenetre
    timer = QTimer()
    timer.timeout.connect(w.update)
    fps = 30 # Frame per seconds
    timer.start(1000/fps)
    app.exec_()
