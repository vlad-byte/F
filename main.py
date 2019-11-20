import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import Qt
from PyQt5 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.draw_line)
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
        self.update()

    def paintEvent(self, event):
        self.painter.begin(self)
        if self.sss:
            self.painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
            for i in range(len(self.sss)):
                self.painter.drawEllipse(self.sss[i][1], self.sss[i][2], self.sss[i][0], self.sss[i][0])
        self.painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())