# DemoButton.py
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#단일 상속
class DemoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        btn1 = QPushButton("닫기", self)
        #좌측 상단(x축, y축)
        btn1.move(20, 20)
        #버튼.시그널명.connect(슬롯메서드)
        btn1.clicked.connect(QCoreApplication.instance().quit)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoWindow()
    demoWindow.show()
    app.exec_() 