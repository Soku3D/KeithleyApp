import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
import pyqtgraph as pg

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('IV Curve Measurement')

        self.layout = QVBoxLayout()

        self.label = QLabel('IV Curve')
        self.layout.addWidget(self.label)

        self.graph_widget = pg.PlotWidget()
        self.layout.addWidget(self.graph_widget)

        self.setLayout(self.layout)

        self.plot_iv_curve()

    def plot_iv_curve(self):
        voltages = [0., 1., 2., 3., 4., 5., 6., 7., 8., 9.]
        currents = [1.48303e-11, 2.441952e-11, 2.593309e-11, 1.331663e-11, 1.886785e-11, 
                    1.331674e-11, 2.391481e-11, 1.382156e-11, 1.83637e-11, 2.189599e-11]

        self.graph_widget.plot(voltages, currents, pen=pg.mkPen(color='b', width=2))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
