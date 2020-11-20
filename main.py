import sys

from random import randint

from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


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
        qp.setPen(QColor('yellow'))
        qp.setBrush(QColor('yellow'))
        diameter = randint(1, 240)
        qp.drawEllipse(QPoint(250, 200), diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
