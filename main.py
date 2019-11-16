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
        self.painter = QPainter(self)
        self.sss = []

    def draw_line(self):
        self.sss = []
        tt = random.randint(1, 5)
        for i in range(tt):
            a = random.randint(0, 200)
            b = random.randint(0, 200)
            b1 = random.randint(0, 200)
            self.sss.append([a, b, b1])
        b = random.randint(0, 255)
        c = random.randint(0, 255)
        d = random.randint(0, 255)
        self.selected_color = QColor(b, c, d)
        self.update()

    def paintEvent(self,event):
        self.painter.begin(self)
        if self.sss:
            self.painter.setBrush(QBrush(self.selected_color, Qt.SolidPattern))
            for i in range(len(self.sss)):
                self.painter.drawEllipse(self.sss[i][1], self.sss[i][2], self.sss[i][0], self.sss[i][0])
        self.painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
