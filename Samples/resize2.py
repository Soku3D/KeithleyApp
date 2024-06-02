import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QTabWidget
import pyqtgraph as pg

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Tab Widget with Resizable PyQtGraph')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        tab_widget = QTabWidget()
        main_layout.addWidget(tab_widget)

        # 첫 번째 탭
        tab1 = QWidget()
        tab1_layout = QVBoxLayout()
        tab1.setLayout(tab1_layout)

        plot_widget1 = pg.PlotWidget()
        tab1_layout.addWidget(plot_widget1)

        tab_widget.addTab(tab1, "Tab 1")

        # 두 번째 탭
        tab2 = QWidget()
        tab2_layout = QVBoxLayout()
        tab2.setLayout(tab2_layout)

        plot_widget2 = pg.PlotWidget()
        tab2_layout.addWidget(plot_widget2)

        tab_widget.addTab(tab2, "Tab 2")

        # 데이터 추가
        self.plot_data(plot_widget1)
        self.plot_data(plot_widget2)

    def plot_data(self, plot_widget):
        x = range(100)
        y = [i ** 0.5 for i in x]
        plot_widget.plot(x, y)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
