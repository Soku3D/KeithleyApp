import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QMessageBox
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Screen Capture Example')
        self.setGeometry(100, 100, 300, 200)

        self.capture_button = QPushButton('Capture Screen', self)
        self.capture_button.setGeometry(50, 50, 200, 50)
        self.capture_button.clicked.connect(self.capture_screen)

    def capture_screen(self):
        # 현재 윈도우의 내용을 캡처
        screenshot = self.grab()
        
        #options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, 
                                                   "Save Screenshot", 
                                                   "", 
                                                   "PNG Files (*.png);;All Files (*)"
                                                   )
        if file_name:
            screenshot.save(file_name, "png")
            QMessageBox.information(self, "Success", f"Screenshot saved as: {file_name}")
        else:
            QMessageBox.warning(self, "Canceled", "Screenshot save canceled.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
