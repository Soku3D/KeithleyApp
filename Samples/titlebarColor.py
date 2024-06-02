import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
import win32api


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 윈도우 핸들 가져오기
        hwnd = self.winId()

        # 타이틀바 색상 변경
        win32api.SetWindowLong(hwnd, win32api.GWL_EXSTYLE, win32api.GetWindowLong(hwnd, win32api.GWL_EXSTYLE) | win32api.WS_EX_LAYERED)
        win32api.SetLayeredWindowAttributes(hwnd, win32api.RGB(255, 0, 0), 255, win32api.LWA_COLORKEY)

        self.setWindowTitle("Red Title Bar Example")

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        label = QLabel("This is the central widget.")
        layout.addWidget(label)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
