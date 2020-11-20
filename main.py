import sys

from random import randint

from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic

OBBLOBLES = 10


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.draw.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_obbloble(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_obbloble(self, qp):
        qp.setPen(QColor('black'))
        qp.setBrush(QColor('yellow'))
        for i in range(OBBLOBLES):
            diameter = randint(1, 100)
            qp.drawEllipse(QPoint(randint(0, 500), randint(0, 350)), diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
