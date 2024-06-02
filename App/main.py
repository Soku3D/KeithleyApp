
from ui import Ui_MainWindow
from ui import SMUDevice
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QTimer, Qt, QThread, pyqtSignal
from PyQt6.QtGui import QPalette, QIcon, QPixmap, QPainter, QColor
from ctypes.wintypes import HANDLE, HICON
from ctypes import windll
from functools import partial

import os
import sys
import numpy as np
import time 
import pyqtgraph as pg
import pyvisa

class KeithleyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #self.setWindowTitle("Keithley")

        exe_path = sys.argv[0]
        exe_dir = os.path.dirname(exe_path)
        icon_path_16x16 = os.path.join(exe_dir, 'Resources/16x16.ico')
        icon_path_256 = os.path.join(exe_dir, 'Resources/256.ico')

        self.setWindowIcon(QIcon(icon_path_16x16))       
        self.setTaskbarIcon(icon_path_256)
        self.setStyleSheet("background-color : #F8F8F8;")

    def setTaskbarIcon(self, icon_path):
        try:
            
            hwnd = self.winId() # 윈도우 핸들 가져오기
            pixmap = QPixmap(icon_path)
            windll.shell32.SHAppBarMessage(0x00C6, 0x00000002, HANDLE(hwnd), HICON(pixmap.toWinHICON()))

        except Exception as e:

            print(f"Failed to set taskbar icon: {e}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow =  KeithleyMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
