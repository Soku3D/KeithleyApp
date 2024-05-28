import sys
import time
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

class TimerExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.startTime = time.perf_counter()  # 시작 시간을 기록
        self.lastTime = self.startTime
        self.elapsedTime = 0
        
    def initUI(self):
        self.layout = QVBoxLayout()
        self.label = QLabel("Elapsed Time: 0.0 s", self)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        
        self.timer = QTimer(self)
        self.timer.setTimerType(Qt.PreciseTimer)
        self.timer.timeout.connect(self.checkTime)
        self.timer.start(10)  # 짧은 간격으로 타이머 이벤트 발생
        
        self.setWindowTitle('QTimer Example')
        self.show()
        
    def checkTime(self):
        currentTime = time.perf_counter()
        elapsedSinceLastCheck = currentTime - self.lastTime
        if elapsedSinceLastCheck >= 1.0:
            self.elapsedTime += elapsedSinceLastCheck
            self.label.setText(f"Elapsed Time: {self.elapsedTime:.3f} s")
            self.lastTime = currentTime

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TimerExample()
    sys.exit(app.exec_())
