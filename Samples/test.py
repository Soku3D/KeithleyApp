import sys
import random
import time
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QFont
import pyqtgraph as pg

class TemperatureMonitor(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

        # 데이터 저장을 위한 리스트
        self.times = []
        self.temperatures = []

        # 그래프 초기화
        self.plotWidget = pg.PlotWidget()
        self.plotWidget.setBackground('w')  # 그래프 배경을 흰색으로 설정
        self.plotWidget.setTitle("Time vs Temperature", color='k', size='20pt')  # 타이틀을 검은색으로 설정
        self.plotWidget.setLabel('left', 'Temperature (°C)', color='k', size='14pt')  # y축 레이블을 검은색으로 설정
        self.plotWidget.setLabel('bottom', 'Time (s)', color='k', size='14pt')  # x축 레이블을 검은색으로 설정
        self.plotWidget.showGrid(x=True, y=True, alpha=0.3)  # 그리드 라인을 약간 투명하게 설정
        self.plotWidget.getAxis('left').setPen(pg.mkPen(color='k', width=1.5))  # y축 라인을 검은색으로 설정
        self.plotWidget.getAxis('bottom').setPen(pg.mkPen(color='k', width=1.5))  # x축 라인을 검은색으로 설정

        # 선 그래프 설정
        self.curve = self.plotWidget.plot(self.times, self.temperatures, pen=pg.mkPen(color=(255, 0, 0), width=2))  # 데이터 라인을 빨간색으로 설정

        # 점 그래프 설정
        self.scatter = pg.ScatterPlotItem(size=10, brush=pg.mkBrush(255, 0, 0), pen=pg.mkPen(None))
        self.plotWidget.addItem(self.scatter)

        # 레이아웃에 그래프 추가
        self.layout().addWidget(self.plotWidget)

        # QTimer 설정
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data)

    def initUI(self):
        self.setWindowTitle('Temperature Monitor')
        self.setGeometry(100, 100, 800, 600)
        layout = QVBoxLayout()

        header = QLabel('Real-Time Temperature Monitoring')
        header.setFont(QFont('Arial', 24))
        header.setStyleSheet('color: #2E8B57; margin-bottom: 20px;')
        layout.addWidget(header, alignment=Qt.AlignmentFlag.AlignCenter)

        self.startButton = QPushButton('Start Monitoring', self)
        self.startButton.setFont(QFont('Arial', 16))
        self.startButton.setStyleSheet('''
            QPushButton {
                background-color: #4CAF50; 
                color: white; 
                padding: 15px 32px; 
                text-align: center; 
                font-size: 16px; 
                margin: 4px 2px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        ''')
        self.startButton.clicked.connect(self.start_monitoring)
        layout.addWidget(self.startButton, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def start_monitoring(self):
        self.start_time = time.time()
        self.timer.start(1000)  # 1초마다 timeout 시그널 발생

    def update_data(self):
        current_time = time.time() - self.start_time
        current_temperature = self.get_temperature()

        self.times.append(current_time)
        self.temperatures.append(current_temperature)

        # 그래프 업데이트
        self.curve.setData(self.times, self.temperatures)
        self.scatter.setData(self.times, self.temperatures)

    def get_temperature(self):
        # 온도 측정 시뮬레이션 (여기에서는 랜덤 값 사용)
        return random.uniform(20.0, 30.0)

def main():
    app = QApplication(sys.argv)
    window = TemperatureMonitor()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
