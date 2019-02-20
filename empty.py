from progpainter import *

def init(self): # N'est executé qu'une seule fois au départ
    pass

def draw(self): # Fonction repeter 30 fois par seconde
    pass



if __name__ == '__main__': # Ne pas ou peu toucher
    Win._draw = draw  # Associe la fonction a repeter
    Win._init = init # Associe la fonction executé une seule fois au départ
    w = Win("Empty file  - ProgPainter Example") # Création de la fenetre
    timer = QTimer()
    timer.timeout.connect(w.update)
    fps = 30 # Frame per seconds
    timer.start(1000/fps)
    app.exec_()
