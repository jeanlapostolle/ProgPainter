from progpainter import *

def init(self): # N'est executé qu'une seule fois au départ
    self.resize(500,500)

def draw(self): # Fonction repeter 30 fois par seconde
    pencolor("white") # Couleur du pinceau
    x, y = self.mousePosition()
    circle((x,y), 10)
    pencolor("black")
    circle((x,y), 13)
    pencolor("green")
    circle((x,y), 16)




if __name__ == '__main__': # Ne pas ou peu toucher
    Win._draw = draw  # Associe la fonction a repeter
    Win._init = init # Associe la fonction executé une seule fois au départ
    w = Win("Mouse Follow - ProgPainter Example") # Création de la fenetre
    timer = QTimer()
    timer.timeout.connect(w.update)
    fps = 30 # Frame per seconds
    timer.start(1000/fps)
    app.exec_()
