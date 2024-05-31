import sys
import pyvisa
import numpy as np
import pyqtgraph as pg
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QTimer

class IVPlotter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.voltages = np.arange(0, 5.1, 0.1)  # 초기화 위치 수정
        self.currents = []
        self.index = 0

        self.initUI()
        self.initKeithley()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(100)  # 100 ms interval

    def initUI(self):
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        self.graphWidget.setTitle("Real-time IV Curve")
        self.graphWidget.setLabel('left', 'Current (A)')
        self.graphWidget.setLabel('bottom', 'Voltage (V)')
        self.data_line = self.graphWidget.plot([], [], pen=pg.mkPen('r', width=2))

    def initKeithley(self):
        rm = pyvisa.ResourceManager()
        self.keithley = rm.open_resource('GPIB0::24::INSTR')  # GPIB 주소를 적절히 변경하세요
        try:
            self.keithley.write('*RST')
            self.keithley.write(':SOUR:FUNC VOLT')
            self.keithley.write(':SOUR:VOLT:STAR 0')
            self.keithley.write(':SOUR:VOLT:STOP 5')
            self.keithley.write(':SOUR:VOLT:STEP 0.1')
            self.keithley.write(':SOUR:VOLT:MODE SWE')
            self.keithley.write(':SENS:FUNC "CURR"')
            self.keithley.write(':SENS:CURR:PROT 0.1')
            self.keithley.write(f':TRIG:COUN {len(self.voltages)}')
            self.keithley.write(':OUTP ON')  # Sweep 시작
        except Exception error:


    def update_plot(self):
        if self.index < len(self.voltages):
            data = self.keithley.query(':TRAC:DATA? 1,1')  # 최신 측정값 불러오기
            current = float(data.split(',')[1])
            self.currents.append(current)
            self.data_line.setData(self.voltages[:self.index + 1], self.currents)
            self.index += 1
        else:
            self.timer.stop()
            self.keithley.write(':OUTP OFF')
            self.keithley.close()

def main():
    app = QApplication(sys.argv)
    plotter = IVPlotter()
    plotter.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
