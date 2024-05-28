import sys
import random
import time
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QFont
import pyqtgraph as pg

class CurrentMonitor(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

        # 데이터 저장을 위한 딕셔너리
        self.data = {}

        # 그래프 초기화
        self.plotWidget = pg.PlotWidget()
        self.plotWidget.setBackground('w')  # 그래프 배경을 흰색으로 설정
        self.plotWidget.setTitle("Gate Voltage vs Current", color='k', size='20pt')  # 타이틀을 검은색으로 설정
        self.plotWidget.setLabel('left', 'Current (A)', color='k', size='14pt')  # y축 레이블을 검은색으로 설정
        self.plotWidget.setLabel('bottom', 'Gate Voltage (V)', color='k', size='14pt')  # x축 레이블을 검은색으로 설정
        self.plotWidget.showGrid(x=True, y=True, alpha=0.3)  # 그리드 라인을 약간 투명하게 설정
        self.plotWidget.getAxis('left').setPen(pg.mkPen(color='k', width=1.5))  # y축 라인을 검은색으로 설정
        self.plotWidget.getAxis('bottom').setPen(pg.mkPen(color='k', width=1.5))  # x축 라인을 검은색으로 설정

        # 레이아웃에 그래프 추가
        self.layout().addWidget(self.plotWidget)

        # QTimer 설정
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data)

        self.current_gate_voltage = 0  # 초기 게이트 전압
        self.gate_voltages = [1, 2, 3, 4, 5]  # 예시 게이트 전압 리스트
        self.update_interval = 1000  # 1초마다 데이터 업데이트

    def initUI(self):
        self.setWindowTitle('Current Monitor')
        self.setGeometry(100, 100, 800, 600)
        layout = QVBoxLayout()

        header = QLabel('Gate Voltage vs Current Monitoring')
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
        self.timer.start(self.update_interval)

    def update_data(self):
        # 임의의 전류 값 생성 (여기에서는 랜덤 값 사용)
        current = self.get_current()

        if self.current_gate_voltage not in self.data:
            self.data[self.current_gate_voltage] = {'voltages': [], 'currents': []}

        self.data[self.current_gate_voltage]['voltages'].append(self.current_gate_voltage)
        self.data[self.current_gate_voltage]['currents'].append(current)

        # 그래프 업데이트
        self.plotWidget.clear()
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
        for i, (voltage, data) in enumerate(self.data.items()):
            color = colors[i % len(colors)]
            self.plotWidget.plot(data['voltages'], data['currents'], pen=pg.mkPen(color=color, width=2), name=str(voltage) + " V")
            scatter = pg.ScatterPlotItem(size=10, brush=pg.mkBrush(color[0], color[1], color[2]), pen=pg.mkPen(None))
            scatter.setData(data['voltages'], data['currents'])
            self.plotWidget.addItem(scatter)

        # 다음 게이트 전압으로 변경
        self.current_gate_voltage = self.gate_voltages[(self.gate_voltages.index(self.current_gate_voltage) + 1) % len(self.gate_voltages)]

    def get_current(self):
        # 전류 측정 시뮬레이션 (여기에서는 랜덤 값 사용)
        return random.uniform(0.1, 1.0)

def main():
    app = QApplication(sys.argv)
    window = CurrentMonitor()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
