import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor
from random import randint as gen


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 500)
        self.setWindowTitle('Рисовалка кругов')
        self.pushButton = QPushButton('рисовать', self)
        self.pushButton.resize(90, 60)
        self.pushButton.move(105, 25)
        self.pushButton.clicked.connect(self.bol)
        self.flag = False
        self.show()

    def bol(self):
        self.flag = True
        if self.flag:
            self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        if self.flag:
            x, y, len_ = gen(0, self.width() - 1), gen(0, self.height() - 1), gen(0, self.width() // 2)
            qp.setBrush(QColor(gen(0, 255), gen(0, 255), gen(0, 255)))
            qp.drawEllipse(x, y, len_, len_)
            self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())