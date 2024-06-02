from test import TemperatureMonitor
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QMainWindow, QApplication
import sys
import pyqtgraph as pg

class testWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

        # 데이터 저장을 위한 리스트
        self.times = []
        self.temperatures = []

        # 그래프 초기화
        self.plotWidget = pg.PlotWidget()
        self.layout().addWidget(self.plotWidget)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()


class MainUI(object):

    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        MainWindow.setCentralWidget(TemperatureMonitor())
        



if __name__ == "__main__":
    finalApp = QApplication(sys.argv)
    window = MainWindow()
    ui = MainUI()
    ui.setupUi(window)
    window.show()
    sys.exit(finalApp.exec())


