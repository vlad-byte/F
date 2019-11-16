import sys
import random
from PyQt5.QtWidgets import QMainWindow,QPushButton, QApplication
from PyQt5.QtCore import QSize, Qt, QLine, QPoint
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(300, 300))

        b = random.randint(0, 255)
        c = random.randint(0, 255)
        d = random.randint(0, 255)
        self.selected_color = QColor(b, c, d)
        pybutton = QPushButton('button', self)
        pybutton.clicked.connect(self.draw_line)
        pybutton.resize(100, 50)
        pybutton.move(100, 240)
        self.line = QLine()

    def draw_line(self):
        button = self.sender()
        self.line = QLine(QPoint(), button.pos())
        self.update()

    def paintEvent(self,event):
        if not self.line.isNull():
            painter = QPainter(self)
            painter.setPen(QPen(self.selected_color, 8, Qt.SolidLine))
            painter.setBrush(QBrush(self.selected_color, Qt.SolidPattern))
            a = random.randint(100, 200)
            painter.drawEllipse(40, 40, a, a)
            b = random.randint(0, 255)
            c = random.randint(0, 255)
            d = random.randint(0, 255)
            self.selected_color = QColor(b, c, d)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
