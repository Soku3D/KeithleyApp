import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
import pyqtgraph as pg

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt6 QtGraph Two Y-Axes Example")
        self.setGeometry(100, 100, 800, 600)

        self.plot_widget = pg.PlotWidget()
        self.setCentralWidget(self.plot_widget)

        self.update_plot()

    def update_plot(self):
        # 샘플 데이터 생성
        x = list(range(10))
        y1 = [random.randint(0, 10) for _ in range(10)]
        y2 = [random.randint(20, 40) for _ in range(10)]

        # 첫 번째 y축 데이터 그리기
        pen1 = pg.mkPen(color='r', width=2, style=pg.QtCore.Qt.PenStyle.SolidLine)
        symbol1 = 'o'
        curve1 = self.plot_widget.plot(x, y1, pen=pen1, symbol=symbol1, symbolBrush=('r'), name='Y1 Data')

        # 두 번째 y축 생성 및 데이터 그리기
        self.plot_widget.getPlotItem().showAxis('right')
        self.plot_widget.getPlotItem().scene().addItem(self.plot_widget.getPlotItem().getViewBox())
        self.plot_widget.getPlotItem().getAxis('right').linkToView(self.plot_widget.getPlotItem().getViewBox())
        self.plot_widget.getPlotItem().getViewBox().setXLink(self.plot_widget.getPlotItem().vb)

        # 두 번째 Y축 데이터 그리기
        p2 = pg.ViewBox()
        self.plot_widget.getPlotItem().getAxis('right').linkToView(p2)
        pen2 = pg.mkPen(color='b', width=2, style=pg.QtCore.Qt.PenStyle.DashLine)
        symbol2 = 't'
        curve2 = pg.PlotDataItem(x, y2, pen=pen2, symbol=symbol2, symbolBrush=('b'), name='Y2 Data')
        p2.addItem(curve2)
        self.plot_widget.getPlotItem().scene().addItem(p2)
        p2.setGeometry(self.plot_widget.getPlotItem().getViewBox().sceneBoundingRect())
        p2.linkedViewChanged(self.plot_widget.getPlotItem().getViewBox(), p2.XAxis)

        # 제목 추가
        self.plot_widget.setTitle('Two Y-Axes Example')

        # 범례 추가 및 항목 정의
        legend = self.plot_widget.addLegend()
        legend.addItem(curve1, 'Y1 Data: red circles')
        legend.addItem(curve2, 'Y2 Data: blue triangles')

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
