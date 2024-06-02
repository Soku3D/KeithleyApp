# qThread 로 class를 갖는 Thread 

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import QThread, pyqtSignal, QTimer
import time
class device():
    def __init__(self, voltRange):
        super().__init__()
        self.volt = voltRange


class Worker(QThread):
    countChanged = pyqtSignal(int)

    def __init__(self, device1):
        super().__init__()
        self.device = device1

    def run(self):
        s = self.device.volt
        for v in range (s):
            self.countChanged.emit(v)
            time.sleep(1)


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.worker = Worker(device(10))
        self.worker.countChanged.connect(self.on_count_changed)


    def initUI(self):
        self.layout = QVBoxLayout()
        self.label = QLabel("Count: 0", self)
        self.button = QPushButton("Start Counting", self)
        self.button.clicked.connect(self.start_counting)
        
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        
        self.setLayout(self.layout)
        
        self.setWindowTitle('QThread Example')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def start_counting(self):
        if not self.worker.isRunning():
            self.worker.start()

    def on_count_changed(self, count):
        self.label.setText(f"Count: {count}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
