import sys
import time
import pyvisa
import numpy as np
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import QThread, pyqtSignal
import pyqtgraph as pg

# PyVisa 측정을 수행할 QThread 클래스
class MeasurementThread(QThread):
    data_acquired = pyqtSignal(list, list)  # (voltages, currents)
    
    def run(self):
        rm = pyvisa.ResourceManager()
        keithley = rm.open_resource('GPIB0::24::INSTR')

        # 장치 ID 확인 (선택사항)
        print(keithley.query('*IDN?'))

        # 초기 설정
        keithley.write('*RST')  # 장치 리셋
        keithley.write(':SENS:FUNC "CURR"')  # 전류 측정 모드 설정
        keithley.write(':SOUR:FUNC VOLT')  # 전압 소스 모드 설정
        keithley.write(':FORM:ELEM CURR')  # 전류만 읽기
        keithley.write(':SENS:CURR:PROT 0.1')
        voltages = []
        currents = []
        for voltage in np.linspace(0, 10, 11):
            keithley.write(f":SOUR:VOLT {voltage}")
            keithley.write("OUTP ON")
            time.sleep(1)  # 1초 대기
            current =float(keithley.query(":READ?"))          
            voltages.append(voltage)
            currents.append(current)

            self.data_acquired.emit(voltages, currents)
            keithley.write("OUTP OFF")
            
        

# 메인 윈도우 클래스
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Voltage-Current Measurement")
        
        self.graph_widget = pg.PlotWidget()
        self.plot = self.graph_widget.plot([], [], pen=None, symbol='o')
        
        self.button = QPushButton("Run")
        self.button.clicked.connect(self.start_measurement)
        
        layout = QVBoxLayout()
        layout.addWidget(self.graph_widget)
        layout.addWidget(self.button)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        self.thread = MeasurementThread()
        self.thread.data_acquired.connect(self.update_graph)
    
    def start_measurement(self):
        self.plot.setData([], [])  # 그래프 초기화
        self.thread.start()
    
    def update_graph(self, voltages, currents):
        print(voltages)
        print(currents)
        self.plot.setData(voltages, currents)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
