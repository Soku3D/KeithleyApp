# Form implementation generated from reading ui file '.\AppUI_1.1.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QTimer, Qt, QThread, pyqtSignal
from PyQt6.QtGui import QPalette, QIcon, QPixmap, QPainter, QColor
from ctypes.wintypes import HANDLE, HICON
from ctypes import windll
from functools import partial

import os
import sys
import numpy as np
import time 
import pyqtgraph as pg
import pyvisa

painter = QPainter()
painter.setBrush(QColor(135, 206, 235)) 

class KeithleyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #self.setWindowTitle("Keithley")

        exe_path = sys.argv[0]
        exe_dir = os.path.dirname(exe_path)
        icon_path_16x16 = os.path.join(exe_dir, 'Resources/16x16.ico')
        icon_path_256 = os.path.join(exe_dir, 'Resources/256.ico')

        self.setWindowIcon(QIcon(icon_path_16x16))       
        self.setTaskbarIcon(icon_path_256)
        # self.setStyleSheet("""
        #     QWidget {
        #         border-radius: 15px;
        #     }
        # """)

    def setTaskbarIcon(self, icon_path):
        try:
            
            hwnd = self.winId()# 윈도우 핸들 가져오기

            pixmap = QPixmap(icon_path)
            windll.shell32.SHAppBarMessage(0x00C6, 0x00000002, HANDLE(hwnd), HICON(pixmap.toWinHICON()))

        except Exception as e:
            print(f"Failed to set taskbar icon: {e}")


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        
        
        self.device2420 = None
        self.device2635b = None

        self.currDrainVolt = 0
        self.currGateVolt = 0

        self.currTime = 0
        self.startTIme = 0
        
        self.gateStep = 0
        self.drainStep = 0

        self.Vd = []
        self.Vg = []
        self.drainCurrents = []
        self.times = []

        self.timer = QTimer()
        self.timer.setTimerType(Qt.TimerType.PreciseTimer)
        self.timer.timeout.connect(self.updateData)

    def setupUi(self, MainWindow):
       
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.KS_Label = QtWidgets.QLabel(parent=self.centralwidget)
        self.KS_Label.setGeometry(QtCore.QRect(40, 30, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.KS_Label.setFont(font)
        self.KS_Label.setObjectName("KS_Label")
        self.KS_TabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.KS_TabWidget.setGeometry(QtCore.QRect(40, 70, 201, 181))
        self.KS_TabWidget.setObjectName("KS_TabWidget")
        self.keithley2635b = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.keithley2635b.setFont(font)
        self.keithley2635b.setObjectName("keithley2635b")
        self.label = QtWidgets.QLabel(parent=self.keithley2635b)
        self.label.setGeometry(QtCore.QRect(50, 20, 61, 41))
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(parent=self.keithley2635b)
        self.spinBox.setGeometry(QtCore.QRect(110, 30, 70, 22))
        self.spinBox.setProperty("value", 26)
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(parent=self.keithley2635b)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 101, 21))
        self.label_2.setObjectName("label_2")
        self.CurrentLimit_2635b = QtWidgets.QDoubleSpinBox(parent=self.keithley2635b)
        self.CurrentLimit_2635b.setGeometry(QtCore.QRect(110, 60, 71, 22))
        self.CurrentLimit_2635b.setProperty("value", 0.1)
        self.CurrentLimit_2635b.setObjectName("CurrentLimit_2635b")
        self.IsConnected_2635b = QtWidgets.QLabel(parent=self.keithley2635b)
        self.IsConnected_2635b.setGeometry(QtCore.QRect(0, 130, 190, 16))
        self.IsConnected_2635b.setText("")
        self.IsConnected_2635b.setObjectName("IsConnected_2635b")
        self.connectBt_2635b = QtWidgets.QPushButton(parent=self.keithley2635b)
        self.connectBt_2635b.setGeometry(QtCore.QRect(60, 100, 75, 24))
        self.connectBt_2635b.setObjectName("connectBt_2635b")
        self.KS_TabWidget.addTab(self.keithley2635b, "")
        self.Keithley2420 = QtWidgets.QWidget()
        self.Keithley2420.setObjectName("Keithley2420")
        self.CurrentLimit_2420 = QtWidgets.QDoubleSpinBox(parent=self.Keithley2420)
        self.CurrentLimit_2420.setGeometry(QtCore.QRect(110, 60, 71, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.CurrentLimit_2420.setFont(font)
        self.CurrentLimit_2420.setProperty("value", 0.1)
        self.CurrentLimit_2420.setObjectName("CurrentLimit_2420")
        self.label_3 = QtWidgets.QLabel(parent=self.Keithley2420)
        self.label_3.setGeometry(QtCore.QRect(50, 20, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Address_2420 = QtWidgets.QSpinBox(parent=self.Keithley2420)
        self.Address_2420.setGeometry(QtCore.QRect(110, 30, 70, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Address_2420.setFont(font)
        self.Address_2420.setProperty("value", 24)
        self.Address_2420.setObjectName("Address_2420")
        self.label_4 = QtWidgets.QLabel(parent=self.Keithley2420)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.connectBt_2420 = QtWidgets.QPushButton(parent=self.Keithley2420)
        self.connectBt_2420.setGeometry(QtCore.QRect(60, 100, 75, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.connectBt_2420.setFont(font)
        self.connectBt_2420.setObjectName("connectBt_2420")
        self.IsConnected_2420 = QtWidgets.QLabel(parent=self.Keithley2420)
        self.IsConnected_2420.setGeometry(QtCore.QRect(0, 130, 190, 16))
        self.IsConnected_2420.setText("")
        self.IsConnected_2420.setObjectName("IsConnected_2420")
        self.KS_TabWidget.addTab(self.Keithley2420, "")
        self.KS_Label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.KS_Label_2.setGeometry(QtCore.QRect(50, 290, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.KS_Label_2.setFont(font)
        self.KS_Label_2.setObjectName("KS_Label_2")
        self.RS_TabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        #self.RS_TabWidget.setStyleSheet("background-color: lightblue;")
        
        self.RS_TabWidget.setGeometry(QtCore.QRect(40, 330, 201, 161))
        self.RS_TabWidget.setObjectName("RS_TabWidget")
        self.RS_keithley2635b = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.RS_keithley2635b.setFont(font)
        self.RS_keithley2635b.setObjectName("RS_keithley2635b")
        self.RS_2635b_VStart = QtWidgets.QSpinBox(parent=self.RS_keithley2635b)
        self.RS_2635b_VStart.setGeometry(QtCore.QRect(110, 30, 80, 22))
        self.RS_2635b_VStart.setMinimum(-100)
        self.RS_2635b_VStart.setMaximum(100)
        self.RS_2635b_VStart.setProperty("value", 1)
        self.RS_2635b_VStart.setObjectName("RS_2635b_VStart")
        self.label_6 = QtWidgets.QLabel(parent=self.RS_keithley2635b)
        self.label_6.setGeometry(QtCore.QRect(20, 60, 71, 21))
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(parent=self.RS_keithley2635b)
        self.label_9.setGeometry(QtCore.QRect(20, 90, 71, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.RS_keithley2635b)
        self.label_10.setGeometry(QtCore.QRect(20, 30, 71, 21))
        self.label_10.setObjectName("label_10")
        self.RS_2635b_VStop = QtWidgets.QSpinBox(parent=self.RS_keithley2635b)
        self.RS_2635b_VStop.setGeometry(QtCore.QRect(110, 60, 80, 22))
        self.RS_2635b_VStop.setMinimum(-100)
        self.RS_2635b_VStop.setProperty("value", 1)
        self.RS_2635b_VStop.setObjectName("RS_2635b_VStop")
        self.RS_2635b_VStep = QtWidgets.QSpinBox(parent=self.RS_keithley2635b)
        self.RS_2635b_VStep.setGeometry(QtCore.QRect(110, 90, 80, 22))
        self.RS_2635b_VStep.setMinimum(-100)
        self.RS_2635b_VStep.setProperty("value", 0)
        self.RS_2635b_VStep.setObjectName("RS_2635b_VStep")
        self.RS_TabWidget.addTab(self.RS_keithley2635b, "")
        self.Keithley2420_2 = QtWidgets.QWidget()
        self.Keithley2420_2.setObjectName("Keithley2420_2")
        self.RS_2420_VStart = QtWidgets.QSpinBox(parent=self.Keithley2420_2)
        self.RS_2420_VStart.setGeometry(QtCore.QRect(110, 30, 80, 22))
        self.RS_2420_VStart.setMinimum(-100)
        self.RS_2420_VStart.setProperty("value", -60)
        self.RS_2420_VStart.setObjectName("RS_2420_VStart")
        self.label_7 = QtWidgets.QLabel(parent=self.Keithley2420_2)
        self.label_7.setGeometry(QtCore.QRect(20, 60, 71, 21))
        self.label_7.setObjectName("label_7")
        self.label_11 = QtWidgets.QLabel(parent=self.Keithley2420_2)
        self.label_11.setGeometry(QtCore.QRect(20, 90, 71, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.Keithley2420_2)
        self.label_12.setGeometry(QtCore.QRect(20, 30, 71, 21))
        self.label_12.setObjectName("label_12")
        self.RS_2420_VStop = QtWidgets.QSpinBox(parent=self.Keithley2420_2)
        self.RS_2420_VStop.setGeometry(QtCore.QRect(110, 60, 80, 22))
        self.RS_2420_VStop.setMinimum(-100)
        self.RS_2420_VStop.setProperty("value", 60)
        self.RS_2420_VStop.setObjectName("RS_2420_VStop")
        self.RS_2420_VStep = QtWidgets.QSpinBox(parent=self.Keithley2420_2)
        self.RS_2420_VStep.setGeometry(QtCore.QRect(110, 90, 80, 22))
        self.RS_2420_VStep.setMinimum(-100)
        self.RS_2420_VStep.setProperty("value", 1)
        self.RS_2420_VStep.setObjectName("RS_2420_VStep")
        self.RS_TabWidget.addTab(self.Keithley2420_2, "")
        self.RunButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.RunButton.setGeometry(QtCore.QRect(50, 500, 81, 24))
        self.RunButton.setObjectName("RunButton")
        self.AbortButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.AbortButton.setGeometry(QtCore.QRect(144, 500, 81, 24))
        self.AbortButton.setObjectName("AbortButton")
        self.line_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(253, 20, 20, 641))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(40, 280, 201, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(40, 310, 201, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(40, 50, 201, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(40, 20, 201, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(280, 10, 981, 651))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.gridLayoutWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.DataGraph = QtWidgets.QWidget()
        self.DataGraph.setObjectName("DataGraph")

        
        self.gridLayoutWidget_2 = QtWidgets.QWidget(parent=self.DataGraph)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 971, 621))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_graph = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_graph.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_graph.setObjectName("gridLayout_graph")

        self.graphData = pg.PlotWidget()
        self.graphData.setBackground('w')
        self.graphData.setLabel('left', 'Currents (A)')
        self.graphData.setLabel('bottom', 'Gate Voltage (V)')
        self.graphData.showGrid(x=True, y=True, alpha = 0.1)
        self.graphData.getAxis('left').setPen(pg.mkPen(color='k', width=1.5))
        self.graphData.getAxis('bottom').setPen(pg.mkPen(color='k', width=1.5))
        
        self.curve = self.graphData.plot(self.times, self.Vd, pen=pg.mkPen(color=(255, 0, 0), width=2))
        self.scatter = pg.ScatterPlotItem(size=10, brush=pg.mkBrush(255, 0, 0), pen=pg.mkPen(None))
        self.graphData.addItem(self.scatter)

        self.gridLayout_graph.addWidget(self.graphData)
        
        self.tabWidget.addTab(self.DataGraph, "")
        self.DtataTable = QtWidgets.QWidget()
        self.DtataTable.setObjectName("DtataTable")
        self.DataTableWidget = QtWidgets.QTableWidget(parent=self.DtataTable)
        self.DataTableWidget.setGeometry(QtCore.QRect(-5, 1, 981, 621))
        self.DataTableWidget.setObjectName("DataTableWidget")
        self.DataTableWidget.setColumnCount(0)
        self.DataTableWidget.setRowCount(0)
        self.tabWidget.addTab(self.DtataTable, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.KS_TabWidget.setCurrentIndex(0)
        self.RS_TabWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.RunButton.clicked.connect(self.runStart)
        self.connectBt_2420.clicked.connect(lambda : self.keithleyConnect("2420", 24))
        self.connectBt_2635b.clicked.connect(partial(self.keithleyConnect, "2635b", 26))
        self.AbortButton.clicked.connect(self.abort)

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KeithleyApp"))
        self.KS_Label.setText(_translate("MainWindow", "Keithley Settings"))
        self.label.setText(_translate("MainWindow", "Address :"))
        self.label_2.setText(_translate("MainWindow", "Current Limit (A) :"))
        self.connectBt_2635b.setText(_translate("MainWindow", "Connect"))
        self.KS_TabWidget.setTabText(self.KS_TabWidget.indexOf(self.keithley2635b), _translate("MainWindow", "Keithley2635b"))
        self.label_3.setText(_translate("MainWindow", "Address :"))
        self.label_4.setText(_translate("MainWindow", "Current Limit (A) :"))
        self.connectBt_2420.setText(_translate("MainWindow", "Connect"))
        self.KS_TabWidget.setTabText(self.KS_TabWidget.indexOf(self.Keithley2420), _translate("MainWindow", "Keithley2420"))
        self.KS_Label_2.setText(_translate("MainWindow", "Run Settings"))
        self.label_6.setText(_translate("MainWindow", "Vg stop (V):"))
        self.label_9.setText(_translate("MainWindow", "Vg step (V):"))
        self.label_10.setText(_translate("MainWindow", "Vg start (V):"))
        self.RS_TabWidget.setTabText(self.RS_TabWidget.indexOf(self.RS_keithley2635b), _translate("MainWindow", "Keithley2635b"))
        self.label_7.setText(_translate("MainWindow", "Vd stop (V):"))
        self.label_11.setText(_translate("MainWindow", "Vd step (V):"))
        self.label_12.setText(_translate("MainWindow", "Vd start (V):"))
        self.RS_TabWidget.setTabText(self.RS_TabWidget.indexOf(self.Keithley2420_2), _translate("MainWindow", "Keithley2420"))
        self.RunButton.setText(_translate("MainWindow", "Run"))
        self.AbortButton.setText(_translate("MainWindow", "Abort"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DataGraph), _translate("MainWindow", "Graph"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DtataTable), _translate("MainWindow", "Table"))
    
    def keithleyConnect(self,deviceName, address):
     
        rm = pyvisa.ResourceManager()
                
        if deviceName == "2635b":

            try:
                self.device2635b = rm.open_resource(f'GPIB::{address}::INSTR')
                self.IsConnected_2635b.setStyleSheet('color: green;')
                self.IsConnected_2635b.setText(f"Connected to {address}")
                time.sleep(1)
                self.IsConnected_2635b.setText("")
                self.device2420.write('smua.source.func = smua.OUTPUT_DCV')# 전압 source mode
                self.device2420.write('smua.measure.func = smua.FUNC_DCI') # 전류 measure mode
                self.device2635b.write(f'smua.source.limiti = {self.CurrentLimit_2635b.value()}') # 전류 한계 설정
       
            except Exception as e:
                self.IsConnected_2635b.setText(f"Failed to connect: {e}")
                self.IsConnected_2635b.setStyleSheet('color: red;')
                self.device2635b = None


        elif deviceName == "2420":

            try:
                self.device2420 = rm.open_resource(f'GPIB::{address}::INSTR')
                self.IsConnected_2420.setStyleSheet('color: green;')
                self.IsConnected_2420.setText(f"Connected to {address}")         
                print(self.device2420.query('*IDN?'))
                
                self.device2420.write(':SOUR:FUNC VOLT')# 전압 source mode
                self.device2420.write(':SENS:FUNC "CURR"') # 전류 measure mode
                self.device2420.write(f':SENS:CURR:PROT {self.CurrentLimit_2420.value()}') # 전류한계 설정


            except Exception as e:
                self.IsConnected_2420.setText(f"Failed to connect: {e}")
                self.IsConnected_2420.setStyleSheet('color: red;')
                self.device2420 = None

    def runStart(self):
        
        self.currDrainVolt = self.RS_2420_VStart.value()
        self.currGateVolt = self.RS_2635b_VStart.value()
        self.gateStep = self.RS_2635b_VStep.value()
        self.drainStep = self.RS_2420_VStep.value()
        try:
            self.Vd.append(self.currDrainVolt)
            self.Vg.append(self.currGateVolt)
            self.times.append(0.0)

            self.device2635b.write('smua.source.output = smua.OUTPUT_ON')
            self.device2420.write(':OUTP ON')

            # 전압설정
            self.device2635b.write(f'suma.source.levelv = {self.currGateVolt}')    
            self.device2420.write(f':SOUR:VOLT {self.curreDrainVolt}')

            self.startTime = time.perf_counter()
            self.timer.start(1000)

        except Exception as e:
            print(f"{e}")

    def abort(self):
        self.timer.stop()

    def updateData(self):
        self.currTime = time.perf_counter() - self.startTime
        print(self.currTime)
        self.currGateVolt += self.gateStep
        self.currDrainVolt += self.drainStep
        self.Vd.append(self.currGateVolt)
        self.times.append(self.currTime)
        
        self.curve.setData(self.times, self.Vd)
        self.scatter.setData(self.times, self.Vd)
        try:
            
            self.drainCurrents.append(self.device2420.query(':MEAS:CURR?')) # 1초동안 인가한 VOlTAGE 의한 Drain Currents 측정

            # GateVoltage & Drain Voltage 인가

            print()

        except Exception as e:
                
            print(f"{e}")
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow =  KeithleyMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
