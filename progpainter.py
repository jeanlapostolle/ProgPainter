from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt, QTimer
import sys, random

global qp, mpos

qp = QPainter()

class Win(QWidget):

    def __init__(self, title="New Window"):
        super().__init__()
        self.title = title
        self.initUI()
        self.setMouseTracking(True)
        # qp.begin(self)
        self._init()
        # qp.end()


    def initUI(self):
        self.setGeometry(300,300, 300, 190)
        self.setWindowTitle(self.title)
        self.show()


    def paintEvent(self, e):
        qp.begin(self)
        self._draw()
        qp.end()


    def mousePosition(self):
        mpos = self.cursor().pos()
        fpos = self.pos()
        return mpos.x()-fpos.x(), mpos.y()-fpos.y()

    def mousePressEvent(self, e):
        qp.begin(self)
        self._press()
        qp.end()


    def mouseMoveEvent(self, e):
        pass


    # def updt(self):
    #     self.update()


def point(x):
    qp.drawPoint(x[0], x[1])

def line(start, stop):
    qp.drawLine(start[0], start[1], stop[0], stop[1])

def circle(center, radius=5):
    qp.drawEllipse(center[0]-radius//2, center[1]-radius//2, radius, radius)

def rectangle(center, width=5, height=5):
    qp.drawRect(center[0]-width//2, center[1]-height//2, width, height)

def mapping(element, source, destination):
    a, b = source
    c, d = destination
    if a == b:
        print(" error source is not ok in mapping")
        return 0
    return c + (element-a)*(d-c)/(b-a)


colorD = {'red' : Qt.red, 'blue' : Qt.blue, 'green' : Qt.green, 'yellow' : Qt.yellow, 'cyan' : Qt.cyan, 'magenta' : Qt.magenta, 'white' : Qt.white, 'black': Qt.black}
def pencolor(color):
    qp.setPen(colorD[color])




# def grid():






    # def drawPoints(self, qp):
    #
    #     qp.setPen(Qt.red)
    #     size = self.size()
    #
    #     for i in range(1000):
    #         x = random.randint(1, size.width()-1)
    #         y = random.randint(1, size.height()-1)
    #         qp.drawPoint(x, y)



app = QApplication(sys.argv)

# sys.exit(app.exec_())
