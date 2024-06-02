import pyqtgraph as pg


class Graph(pg.PlotWidget):
    def __init__(self):
        super().__init__(self)
        self.graphData = pg.PlotWidget()
        self.setBackground('w')
        self.setLabel('left', 'Currents (A)')
        self.setLabel('bottom', 'Gate Voltage (V)')
        self.showGrid(x=True, y=True, alpha = 0.1)
        self.getAxis('left').setPen(pg.mkPen(color='k', width=1.5))
        self.getAxis('bottom').setPen(pg.mkPen(color='k', width=1.5))
        self.curve = self.plot([], [], pen=pg.mkPen(color=(255, 0, 0), width=2)) 
        self.scatter = pg.ScatterPlotItem(size=10, brush=pg.mkBrush(255, 0, 0), pen=pg.mkPen(None))
        self.addItem(self.scatter)