import sys
import pyvisa
import numpy as np
import time
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import QThread, pyqtSignal, QTimer
import pyqtgraph as pg
from scipy import stats
startv = 0
stopv = 10
stepv = 1
steps= 11
startvprime = float(startv)
stopvprime = float(stopv)
stepvprime = float(stepv)
xvalues = np.arange(startvprime,stopvprime,stepvprime)


class IVThread(QThread):
    data_ready = pyqtSignal()

    def run(self):
        
        startvprime = float(startv)
        stopvprime = float(stopv)
        stepvprime = float(stepv)
        steps = (stopvprime - startvprime) / stepvprime 
        rm = pyvisa.ResourceManager()
        Keithley = rm.open_resource('GPIB::24::INSTR')
        # Turn off concurrent functions and set sensor to current with fixed voltage
        Keithley.write(":SENS:FUNC:CONC OFF")
        Keithley.write(":SOUR:FUNC VOLT")
        Keithley.write(":SENS:FUNC 'CURR:DC' ")

        # Voltage starting, ending, and spacing values based on input
        Keithley.write(f":SOUR:VOLT:STAR {startv}")
        Keithley.write(f":SOUR:VOLT:STOP {stopv}")
        Keithley.write(f":SOUR:VOLT:STEP {stepv}")
        Keithley.write(":SOUR:SWE:RANG AUTO")

        # Set compliance current (in A), sweep direction, and data acquisition
        Keithley.write(":SENS:CURR:PROT 0.1")
        Keithley.write(":SOUR:SWE:SPAC LIN")
        Keithley.write(":SOUR:SWE:POIN ", str(int(steps)))
        Keithley.write(":SOUR:SWE:DIR UP")
        Keithley.write(":TRIG:COUN ", str(int(steps)))
        Keithley.write(":FORM:ELEM CURR")

        # Set sweep mode and turn output on
        Keithley.write(":SOUR:VOLT:MODE SWE")
        Keithley.write(":OUTP ON")


        result = Keithley.query(":READ?")
        self.voltages = xvalues
        self.currents = Keithley.query_ascii_values(":FETC?")
        print(self.voltages)
        print(self.currents)
        self.data_ready.emit()
        Keithley.write(":OUTP OFF")
        Keithley.write(":SOUR:VOLT 0")
        Keithley.close()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('IV Curve Measurement')

        self.layout = QVBoxLayout()

        self.label = QLabel('Press "Run" to start IV measurement')
        self.layout.addWidget(self.label)

        self.run_button = QPushButton('Run')
        self.run_button.clicked.connect(self.start_measurement)
        self.layout.addWidget(self.run_button)

        self.graph_widget = pg.PlotWidget()
        self.graph_widget.setBackground('w')
        self.layout.addWidget(self.graph_widget)

        self.setLayout(self.layout)

        self.iv_thread = IVThread()
        self.iv_thread.data_ready.connect(self.update_plot)

        self.voltages = []
        self.currents = []



    def start_measurement(self):
        self.run_button.setEnabled(False)
        self.label.setText('Measurement in progress...')
        self.voltages = []
        self.currents = []
        self.iv_thread.start()

    def update_plot(self):
        self.graph_widget.plot(self.voltages, self.currents)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())