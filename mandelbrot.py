from progpainter import *

def init(self): # N'est executé qu'une seule fois au départ
    self.resize(500,500)

def press(self):
    pass

def draw(self): # Fonction repeter 30 fois par seconde
    for a in range(500):
        for b in range(500):
            x = mapping(a, (0, 499), (-2, 0.5))
            y = mapping(b, (0, 499), (-1, 1))

            if mandelbrot(complex(x,y),100) < 99:
                point((a,b))


def mandelbrot(c, max_iter):
    z = 0
    iter = 0
    while abs(z) < 2 and iter < max_iter:
        z = z ** 2 + c
        iter += 1
    return iter






if __name__ == '__main__': # Ne pas ou peu toucher
    Win._draw = draw  # Associe la fonction a repeter
    Win._init = init # Associe la fonction executé une seule fois au départ
    Win._press = press
    w = Win("Empty file  - ProgPainter Example") # Création de la fenetre
    timer = QTimer()
    timer.timeout.connect(w.update)
    fps = 0.001 # Frame per seconds
    timer.start(1000/fps)
    app.exec_()
