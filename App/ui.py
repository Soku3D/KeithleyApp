#TODO 세팅 로드
from PyQt6 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import pyvisa
import time
import sys
import os
import pandas as pd
import numpy as np
import math

pg.setConfigOptions(antialias=True)

class CommonSettings:
    sweepPoint = 0
    sourceDelay = 1
    Repeate = 1
    startTime = 0
    currTime = 0
    bIsDualSweep = False

    def __init__(self):
        super().__init__()

    def update(self, p, d, r):
        self.sweepPoint = p
        self.sourceDelay = d
        self.Repeate = r

    def updateDualSweep(self, IsDualSweep):
        self.bIsDualSweep = IsDualSweep
        

class IVThread(QtCore.QThread):
    # DrainVolt , DrainCurr, DrainLogCurr, GateVolt, GateCurr, GateLogCurr, Time
    data = QtCore.pyqtSignal(list,list, list, list, list,list,float)
    commonSetting = None
    devices = {}

    drainVolts =[]
    drainCurrents =[]
    drainLogScaleCurrents =[]
    gateVolts =[]
    gateCurrents =[]
    gateLogScaleCurrents = []
    def updateSettings(self, settings):
        self.commonSetting = settings

    # index-> 0 : 2420 | 1 : 2635b
    def setDevice(self, device, idx):
        if idx==0: # 2420
            self.devices["gate"] = device
        elif idx==1: # 2635b
            self.devices["drain"] = device



    def startSweep(self, biasStepList, sweepList):
        outputOn_ = False
        for bias in biasStepList:
                bias = round(bias ,3)
                self.devices["drain"].sourcingVoltage(bias)
                for sweepVolt in sweepList:
                    sweepVolt = round(sweepVolt, 3)
                    self.devices["gate"].sourcingVoltage(sweepVolt)
                    if outputOn_==False:
                        self.devices["drain"].setOutputOn()
                        self.devices["gate"].setOutputOn()
                        outputOn_ = True
                    gateData = self.devices["gate"].getData()
                    drainData= self.devices["drain"].getData()
                    print(drainData)
                    print(gateData)
                    drainVolt = drainData[0]
                    drainCurrent = drainData[1]
                    gateVolt = gateData[0]
                    gateCurrent = gateData[1]

                    drainLogCurr = math.log10(abs(drainCurrent))
                    gateLogCurr = math.log10(abs(gateCurrent))

                    self.drainVolts.append(drainVolt)
                    self.drainCurrents.append(drainCurrent)
                    self.drainLogScaleCurrents.append(drainLogCurr)
                    self.gateVolts.append(gateVolt)
                    self.gateCurrents.append(gateCurrent)
                    self.gateLogScaleCurrents.append(gateLogCurr)

                    time.sleep(self.commonSetting.sourceDelay)

                    self.currTime = time.perf_counter()
                    elapesedTime = self.currTime- self.startTime
                    # DrainVolt , DrainCurr, DrainLogCurr, GateVolt, GateCurr, GateLogCurr, Time
                    self.data.emit(self.drainVolts, self.drainCurrents, self.drainLogScaleCurrents,
                                    self.gateVolts, self.gateCurrents, self.gateLogScaleCurrents,
                                    elapesedTime)
                    
            
        
    def run(self): 
        try:
            self.startTime = time.perf_counter()
            biasStepList = []
            sweepList = []

            if self.devices["gate"].stepVolt != 0:
                sweepList = np.arange( self.devices["gate"].startVolt,
                                        self.devices["gate"].stopVolt+ self.devices["gate"].stepVolt,
                                        self.devices["gate"].stepVolt)
            else:
                sweepList.append(self.devices["gate"].startVolt)
                
            if self.devices["drain"].stepVolt != 0:
                biasStepList = np.arange( self.devices["drain"].startVolt,
                                        self.devices["drain"].stopVolt,
                                        self.devices["drain"].stepVolt)
            else:
                biasStepList.append(self.devices["drain"].startVolt)

            self.devices["drain"].setFunction()
            self.devices["drain"].setVoltRange()
            self.devices["drain"].setCurrRange()

            self.devices["gate"].setFunction()
            self.devices["gate"].setVoltRange()
            self.devices["gate"].setCurrRange()

            self.devices["gate"].setCurrentLimit()
            self.devices["drain"].setCurrentLimit()

            print(f"biasStep:{biasStepList}\n")
            print(f"sweep:{sweepList}")
            

            print(self.commonSetting.bIsDualSweep)
            
            self.startSweep(biasStepList, sweepList)
            
            if self.commonSetting.bIsDualSweep == True:
                    print("start Inv")
                    invBiasList = biasStepList[::-1]
        
                    invSweepList = sweepList[::-1]
                    invSweepList = invSweepList[1::]
                    print("inv : ", invBiasList)
                    print("inv : ", invSweepList)

                    self.startSweep(invBiasList, invSweepList)

            self.devices["drain"].setOutputOff()
            self.devices["gate"].setOutputOff()

        except Exception as e:
            print(f"{e}")

    def threadReady(self):
        if self.devices.get("drain") !=None and  self.devices.get("gate") != None:
            return True
        else:
            return False
        
class SMUDevice(object):
    device = None
    deviceName = ""

    # 0:LinearSweep | 1:Bias | 2:Step
    mode = 0 
    modeIdx = 0 
    voltRangeIdx = 0
    currentRangeIdx = 0
    
    voltRange = "200e-3"
    currentsRange = "100e-3"
    currentLimit = 0.1
    
    currAutoRange = True
    voltAutoRange = True

    startVolt = 0
    stopVolt = 0
    stepVolt = 0

    biasStart = 0
    biasStop = 0
    biasStop = 0

    def __init__(self, deviceName, d):
        super().__init__()
        self.deviceName  = deviceName
        self.device = d
    def setIdx(self, mode, volt, curr):
        self.modeIdx = mode
        self.voltRangeIdx = volt
        self.currentRangeIdx = curr
    def setSweepValues(self, startV, stopV, stepV):
        self.startVolt = startV
        self.stopVolt = stopV
        self.stepVolt = stepV

    def setCurrentLimitValue(self, limit):
        self.currentLimit = limit
        print(self.currentLimit)

    def setRange(self, currRange, voltRange):
        if currRange=="Auto":
            self.currAutoRange = True
        else :
            self.currentsRange = currRange
            self.currAutoRange = False

        if voltRange=="Auto":
            self.voltAutoRange = True
        else :
            self.voltRange = voltRange
            self.voltAutoRange = False

    def setCurrentLimit(self):

        if self.deviceName == "2420":
            print(f"2420 Set currLimit: {self.currentLimit}")
            self.device.write(f":SENS:CURR:PROT {self.currentLimit}")
        if self.deviceName == "2635b":
            print(f"2635b Set currLimit: {self.currentLimit}")
            self.device.write(f"smua.source.limiti = {self.currentLimit}")

    def setVoltRange(self):
        if self.deviceName == "2420":
            if self.voltAutoRange:
                print("2420 AutoRange")
                self.device.write(":SOUR:VOLT:RANG:AUTO ON")
            else:
                self.device.write(f":SOUR:VOLT:RANG {self.voltRange}")
        if self.deviceName == "2635b":
            if self.voltAutoRange:
                print("2635b AutoRange")
                self.device.write("smua.source.autorangev = smua.AUTORANGE_ON")
            else:
                self.device.write(f"smua.source.rangev = {self.voltRange}")

    def setCurrRange(self):
        if self.deviceName == "2420":
            if self.currAutoRange:
                self.device.write(":SENS:CURR:RANG:AUTO ON")
                print("device 2420 autoRange")
            else:
                self.device.write(f":SENS:CURR:RANG {self.currentsRange}")
                print("device 2420 autoRange")

        if self.deviceName == "2635b":
            if self.voltAutoRange:
                self.device.write("smua.measure.autorangei = smua.AUTORANGE_ON")
            else:
                self.device.write(f"smua.measure.rangei = {self.currentsRange}")

    def sourcingVoltage(self, v):
        try:
            if self.deviceName == "2420":
                #print("sourcingVoltage 2420")
                self.device.write(f":SOUR:VOLT:LEV {v}")
                #print(v)

            elif self.deviceName == "2635b":
                #print("sourcingVoltage 2635b")
                self.device.write(f"smua.source.levelv = {v}")
                #print(v)

        except pyvisa.errors.VisaIOError as e:
            print(e)

    def setFunction(self):
        self.device.write('*RST') 
        if self.deviceName == "2420":
            self.device.write(":SENS:FUNC 'CURR:DC'")  # 전류 측정 모드 설정
            self.device.write(':SOUR:FUNC VOLT')  # 전압 소스 모드 설정
            #self.device.write(':FORM:ELEM CURR') 전압만 측정
        elif self.deviceName == "2635b":
            self.device.write('*CLS')
            self.device.write("smua.source.func = smua.OUTPUT_DCVOLTS")

    def setOutputOn(self):
        try:
            if self.deviceName == "2420":
                self.device.write(":OUTP ON")
            elif self.deviceName == "2635b":
                self.device.write("smua.source.output = smua.OUTPUT_ON")
        except pyvisa.errors.VisaIOError as e:
            print(e)

    def setOutputOff(self):
        if self.deviceName == "2420":
            self.device.write(":OUTP OFF")
        elif self.deviceName == "2635b":
            self.device.write("smua.source.output = smua.OUTPUT_OFF")

    def getCurrent(self):
        current = 0
        if self.deviceName == "2420":
            current = float(self.device.query(':READ?'))
        elif self.deviceName == "2635b":
            self.device.write('print(smua.measure.i())')
            current =  self.device.read()
            current = float(current[:-1])
        return current
    
    def getVolt(self):
        current = 0
        if self.deviceName == "2420":
            current = float(self.device.query(':READ?'))
        elif self.deviceName == "2635b":
            self.device.write('print(smua.measure.v())')
            current =  self.device.read()
            current = float(current[:-1])
        return current
    
    def getData(self):
        data = []
        if self.deviceName == "2420":
            str_ = self.device.query(':READ?')
            print("2420 : ", str_)
            data_ = str_.split(',')
            data = data_[:2]
            data = [float(num) for num in data]
            print("2402 data: " ,data)
        elif self.deviceName == "2635b":
            current = self.device.query("print(smua.measure.i())")
            current = float(current[:-1])
            print("2635b curr " , current)
            volt = self.device.query('print(smua.measure.v())')
            volt = float(volt[:-1])
            
            data.append(volt)
            data.append(current)
        return data

class Ui_MainWindow(object):

    currSMUCount = 0
    addr2420 = 0
    addr2635b = 0
    rm = pyvisa.ResourceManager()
    currSetDevice = -1
    device2420 = None
    device2635b = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        
        #Thread 설정
        self.thread = IVThread()
        self.thread.data.connect(self.updateTabs)
        
        # Common Setting 생성
        self.commonSet = CommonSettings()
        self.thread.updateSettings(self.commonSet)

        # Resources 경로 설정
        exe_path = sys.argv[0]
        exe_dir = os.path.dirname(exe_path)
        self.resourcePath = os.path.join(exe_dir,"Resources")
        self.resourcePath = self.resourcePath.replace("\\","/")

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.centralwidget.setLayout(self.mainLayout)
        
        self.topLayout = QtWidgets.QHBoxLayout()
        self.bottomLayout = QtWidgets.QHBoxLayout()
        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addLayout(self.bottomLayout)

        #self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget = QtWidgets.QTabWidget()
        #self.tabWidget.setGeometry(QtCore.QRect(300, 60, 961, 611))
        self.tabWidget.setStyleSheet("background-color: white;")
        self.tabWidget.setObjectName("tabWidget")
        
        self.settingTab = QtWidgets.QWidget()
        self.settingTab.setObjectName("settingTab")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        
        self.widget = QtWidgets.QWidget(parent=self.settingTab)
        self.saveSettingsBt = QtWidgets.QPushButton(parent=self.settingTab)
        self.saveSettingsBt.setStyleSheet("background-color: white;")
        self.saveSettingsBt.setGeometry(QtCore.QRect(410, 510, 150, 40))
        self.saveSettingsBt.setFont(font)
        self.saveSettingsBt.setStyleSheet("background-color: blue;color : white;")
        self.saveSettingsBt.setObjectName("saveButton")
        self.saveSettingsBt.setText("Save Settings")

        self.widget.setGeometry(QtCore.QRect(40, 91, 441, 211))
        self.widget.setStyleSheet("background-color: #FFFDB5;")
        self.widget.setObjectName("widget")
        self.formLayoutWidget_2 = QtWidgets.QWidget(parent=self.widget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 60, 171, 121))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.modeFormLayout = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.modeFormLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.modeFormLayout.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.modeFormLayout.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignJustify|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.modeFormLayout.setContentsMargins(0, 0, 0, 0)
        self.modeFormLayout.setHorizontalSpacing(6)
        self.modeFormLayout.setVerticalSpacing(2)
        self.modeFormLayout.setObjectName("modeFormLayout")
        self.label_4 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.modeFormLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.modeFormLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.modeFormLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.modeComboBox = QtWidgets.QComboBox(parent=self.formLayoutWidget_2)
        self.modeComboBox.setStyleSheet("background-color: white;")
        self.modeComboBox.setObjectName("modeComboBox")
        self.modeComboBox.addItem("")
        self.modeComboBox.addItem("")
        self.modeComboBox.addItem("")
        self.modeFormLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.modeComboBox)
        self.sourceRangeComboBox = QtWidgets.QComboBox(parent=self.formLayoutWidget_2)
        self.sourceRangeComboBox.setStyleSheet("background-color: white;")
        self.sourceRangeComboBox.setObjectName("sourceRangeComboBox")
        self.modeFormLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.sourceRangeComboBox)
        self.label_7 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.modeFormLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.modeFormLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.dualSweepcheckBox = QtWidgets.QCheckBox(parent=self.formLayoutWidget_2)
        self.dualSweepcheckBox.setObjectName("checkBox")
        self.modeFormLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dualSweepcheckBox)
        self.limitCurrentDSB = QtWidgets.QDoubleSpinBox(parent=self.formLayoutWidget_2)
        self.limitCurrentDSB.setStyleSheet("background-color: white;")
        self.limitCurrentDSB.setObjectName("limitCurrentDSB")
        self.limitCurrentDSB.setDecimals(5)
        self.modeFormLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.limitCurrentDSB)
        self.label_14 = QtWidgets.QLabel(parent=self.widget)
        self.label_14.setEnabled(True)
        self.label_14.setGeometry(QtCore.QRect(200, 20, 41, 16))
        self.label_14.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.label_14.setObjectName("label_14")
        self.line_3 = QtWidgets.QFrame(parent=self.widget)
        self.line_3.setGeometry(QtCore.QRect(20, 20, 171, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(parent=self.widget)
        self.line_4.setGeometry(QtCore.QRect(250, 20, 171, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.formLayoutWidget_3 = QtWidgets.QWidget(parent=self.widget)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(250, 60, 171, 121))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.startVformLayout = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.startVformLayout.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.startVformLayout.setContentsMargins(0, 0, 0, 0)
        self.startVformLayout.setObjectName("startVformLayout")
        self.label_9 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.startVformLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
        self.label_10 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.startVformLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_10)
        self.label_11 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.startVformLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_11)
        self.stepvSpinBox = QtWidgets.QDoubleSpinBox(parent=self.formLayoutWidget_3)
        self.stepvSpinBox.setEnabled(True)
        self.stepvSpinBox.setStyleSheet("background-color: white;")
        self.stepvSpinBox.setObjectName("stepvSpinBox")
        self.stepvSpinBox.setEnabled(False)
        self.stepvSpinBox.setMinimum(-200)
        self.stepvSpinBox.setMaximum(200)
        self.stepvSpinBox.setDecimals(4)
        self.startVformLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.stepvSpinBox)
        self.stopvSpinBox = QtWidgets.QDoubleSpinBox(parent=self.formLayoutWidget_3)
        self.stopvSpinBox.setStyleSheet("background-color: white;")
        self.stopvSpinBox.setObjectName("stopvSpinBox")
        self.stopvSpinBox.setMinimum(-100)
        self.stopvSpinBox.setDecimals(4)
        self.startVformLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.stopvSpinBox)
        self.startvSpinBox = QtWidgets.QDoubleSpinBox(parent=self.formLayoutWidget_3)
        self.startvSpinBox.setStyleSheet("background-color: white;")
        self.startvSpinBox.setObjectName("StartvSpinBox")
        self.startvSpinBox.setMinimum(-100)
        self.startvSpinBox.setMaximum(100)
        self.startvSpinBox.setDecimals(4)
        self.startVformLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.startvSpinBox)
        self.label_12 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.startVformLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_12)
        self.label_13 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.startVformLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_13)
        self.widget_2 = QtWidgets.QWidget(parent=self.settingTab)
        self.widget_2.setGeometry(QtCore.QRect(40, 301, 441, 181))
        self.widget_2.setStyleSheet("background-color: #FFFDB5;")
        self.widget_2.setObjectName("widget_2")
        self.label_20 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_20.setEnabled(True)
        self.label_20.setGeometry(QtCore.QRect(190, 20, 61, 16))
        self.label_20.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.label_20.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.line_5 = QtWidgets.QFrame(parent=self.widget_2)
        self.line_5.setGeometry(QtCore.QRect(20, 20, 171, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(parent=self.widget_2)
        self.line_6.setGeometry(QtCore.QRect(250, 20, 171, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_6.setObjectName("line_6")
        self.formLayoutWidget_5 = QtWidgets.QWidget(parent=self.widget_2)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(90, 40, 101, 106))
        self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
        self.startVformLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_5)
        self.startVformLayout_2.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.startVformLayout_2.setContentsMargins(0, 0, 0, 0)
        self.startVformLayout_2.setObjectName("startVformLayout_2")
        self.label_15 = QtWidgets.QLabel(parent=self.formLayoutWidget_5)
        self.label_15.setObjectName("label_15")
        self.startVformLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_15)
        self.label_16 = QtWidgets.QLabel(parent=self.formLayoutWidget_5)
        self.label_16.setObjectName("label_16")
        self.startVformLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_16)
        self.measureVCB = QtWidgets.QCheckBox(parent=self.formLayoutWidget_5)
        self.measureVCB.setText("")
        self.measureVCB.setTristate(False)
        self.measureVCB.setObjectName("measureVCB")
        self.startVformLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.measureVCB)
        self.measureCurrentCB = QtWidgets.QCheckBox(parent=self.formLayoutWidget_5)
        self.measureCurrentCB.setText("")
        self.measureCurrentCB.setObjectName("measureCurrentCB")
        self.startVformLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.measureCurrentCB)
        self.label_17 = QtWidgets.QLabel(parent=self.formLayoutWidget_5)
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.startVformLayout_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_17)
        self.label_18 = QtWidgets.QLabel(parent=self.formLayoutWidget_5)
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.startVformLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_18)
        self.label_19 = QtWidgets.QLabel(parent=self.formLayoutWidget_5)
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.startVformLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_19)
        self.formLayoutWidget_4 = QtWidgets.QWidget(parent=self.widget_2)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(250, 60, 171, 91))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.startVformLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.startVformLayout_3.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.startVformLayout_3.setContentsMargins(0, 0, 0, 0)
        self.startVformLayout_3.setObjectName("startVformLayout_3")
        self.label_21 = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        self.label_21.setObjectName("label_21")
        self.startVformLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_21)
        self.measureRangeComboBox = QtWidgets.QComboBox(parent=self.formLayoutWidget_4)
        self.measureRangeComboBox.setStyleSheet("background-color: white;")
        self.measureRangeComboBox.setObjectName("measureRangeComboBox")
        self.startVformLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.measureRangeComboBox)
        self.label_22 = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.startVformLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_22)
        self.label_23 = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        self.label_23.setObjectName("label_23")
        self.startVformLayout_3.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_23)
        self.autoZeroComboBox = QtWidgets.QComboBox(parent=self.formLayoutWidget_4)
        self.autoZeroComboBox.setStyleSheet("background-color: white;")
        self.autoZeroComboBox.setObjectName("autoZeroComboBox")
        self.autoZeroComboBox.addItem("")
        self.autoZeroComboBox.addItem("")
        self.startVformLayout_3.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.autoZeroComboBox)
        self.widget_3 = QtWidgets.QWidget(parent=self.settingTab)
        self.widget_3.setGeometry(QtCore.QRect(489, 90, 441, 291))
        self.widget_3.setStyleSheet("background-color: #DBE7FF;")
        self.widget_3.setObjectName("widget_3")
        self.label_26 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_26.setGeometry(QtCore.QRect(10, 10, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_27.setGeometry(QtCore.QRect(30, 70, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_28.setGeometry(QtCore.QRect(30, 90, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_29.setGeometry(QtCore.QRect(30, 160, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_30.setGeometry(QtCore.QRect(30, 140, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_31.setGeometry(QtCore.QRect(30, 230, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.SSPpointsSpinBox = QtWidgets.QSpinBox(parent=self.widget_3)
        self.SSPpointsSpinBox.setGeometry(QtCore.QRect(140, 70, 101, 31))
        self.SSPpointsSpinBox.setStyleSheet("background-color: white;")
        self.SSPpointsSpinBox.setObjectName("SSPpointsSpinBox")
        self.SSPpointsSpinBox.setValue(1)
        self.SSPpointsSpinBox.setMinimum(1)
        self.SSPpointsSpinBox.setMaximum(200)
        self.delaySpinBox = QtWidgets.QSpinBox(parent=self.widget_3)
        self.delaySpinBox.setGeometry(QtCore.QRect(140, 150, 101, 31))
        self.delaySpinBox.setStyleSheet("background-color: white;")
        self.delaySpinBox.setObjectName("delaySpinBox")
        self.repeatSpinBox = QtWidgets.QSpinBox(parent=self.widget_3)
        self.repeatSpinBox.setGeometry(QtCore.QRect(140, 230, 101, 31))
        self.repeatSpinBox.setStyleSheet("background-color: white;")
        self.repeatSpinBox.setObjectName("repeatSpinBox")
        self.ModelLabel = QtWidgets.QLabel(parent=self.settingTab)
        self.ModelLabel.setGeometry(QtCore.QRect(20, 10, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        self.ModelLabel.setFont(font)
        self.ModelLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ModelLabel.setObjectName("ModelLabel")
        self.tabWidget.addTab(self.settingTab, "")
        self.tableTab = QtWidgets.QWidget()
        self.tableTab.setObjectName("tableTab")
        self.tableTabLayout = QtWidgets.QVBoxLayout()
        self.tableTab.setLayout(self.tableTabLayout)
        # self.gridLayoutWidget = QtWidgets.QWidget(parent=self.tableTab)
        # self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 951, 580))
        # self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        # self.tableGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        # self.tableGridLayout.setContentsMargins(0, 0, 0, 0)
        # self.tableGridLayout.setObjectName("tableGridLayout")

        # Table 추가
        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["Time (s)", "Drain Voltage (V)", "Drain Current (A)", "Drain Log Scale Current (A)",
                                               "Gate Voltage (V)", "Gate Current (A)","Gate Log Scale Current (A)"])
        
        self.table.setColumnWidth(0, 100)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 250)
        self.table.setColumnWidth(4, 150)
        self.table.setColumnWidth(5, 150)
        self.table.setColumnWidth(6, 250)
  
        self.table.setStyleSheet("""
            QTableWidget {
                background-color: #f0f0f0;
                gridline-color: #d0d0d0;
                font-size: 14px;
            }
            QTableWidget::item {
                padding: 10px;
            }
        """)
        self.table.horizontalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: #404040;
                color: #ffffff;
                font-weight: bold;
                font-size: 16px;
                border: 1px solid #6c6c6c;
                padding: 5px;
            }
        """)
        self.table.verticalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: #404040;
                color: #ffffff;
                font-weight: bold;
                font-size: 16px;
                 border: 1px solid #6c6c6c;
                padding: 5px;
            }
        """)

        self.tableTabLayout.addWidget(self.table)
        

        self.tabWidget.addTab(self.tableTab, "")
        self.graphTab = QtWidgets.QWidget()
        self.graphTab.setObjectName("graphTab")
        self.graphTabLayout = QtWidgets.QVBoxLayout()
        self.graphTab.setLayout(self.graphTabLayout)
            
        # Graph 추가
        pg.setConfigOptions(antialias=True)
        self.plotWidget = pg.PlotWidget()
        
        self.plotWidget.setBackground('w')  
        self.plotWidget.setLabel('left', 'Drain Current I<sub>d</sub> (A)', color='k', size='17pt')  
        self.plotWidget.setLabel('bottom', 'Gate Voltage V<sub>d</sub> (V)', color='k', size='17pt')  
        #self.plotWidget.setLabel('right', 'Gate Current I<sub>g</sub> (A)', color='k', size='17pt')  
        self.plotWidget.getAxis('left').setPen(pg.mkPen(color='k', width=1.5))  # y축 라인을 검은색으로 설정
        self.plotWidget.getAxis('bottom').setPen(pg.mkPen(color='k', width=1.5))  # x축 라인을 검은색으로 설정
        m_pen = QtGui.QPen(QtGui.QColor(255,0,0))
        m_pen.setCosmetic(True) 
        m_pen.setWidth(2) 
        m_pen.setStyle(QtCore.Qt.PenStyle.SolidLine)
        m_pen1 = QtGui.QPen(QtGui.QColor(0,255,0))
        m_pen1.setCosmetic(True) 
        m_pen1.setWidth(2) 
        m_pen1.setStyle(QtCore.Qt.PenStyle.SolidLine)
        self.curve = self.plotWidget.plot([], [], pen=m_pen, width=2,symbolBrush =(255, 0, 0), symbol='s')
        #self.curve2 = self.plotWidget.plot([], [], pen=m_pen1, width=2,symbolBrush =(0, 255, 0), symbol='o')
        self.graphTabLayout.addWidget(self.plotWidget)    
        
        self.tabWidget.addTab(self.graphTab, "")
        #self.RunButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.RunButton = QtWidgets.QPushButton()
        #self.RunButton.setGeometry(QtCore.QRect(3, 3, 60, 60))
        self.RunButton.setMinimumSize(60,60)
        self.RunButton.setText("")
        self.RunButton.setObjectName("RunButton")
        
        runPath = self.resourcePath + "/Run.png"        
        self.RunButton.setStyleSheet(f"border-image : url({runPath});")
        
        self.saveButton = QtWidgets.QPushButton()
        #self.saveButton.setGeometry(QtCore.QRect(70, 10, 45, 40))
        self.saveButton.setMinimumSize(45,40)
        self.saveButton.setText("")
        self.saveButton.setObjectName("saveButton")
        
        savePath = self.resourcePath + "/Save.png"
        self.saveButton.setStyleSheet(f"border-image : url({savePath});")

        #self.captureButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.captureButton = QtWidgets.QPushButton()
        #self.captureButton.setGeometry(QtCore.QRect(130, 5, 50, 50))
        self.captureButton.setMinimumSize(50,50)
        self.captureButton.setText("")
        self.captureButton.setObjectName("captureButton")
        
        capturePath = self.resourcePath + "/Capture.png"
        self.captureButton.setStyleSheet(f"border-image : url({capturePath});")

        #self.captureGraphButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.captureGraphButton = QtWidgets.QPushButton()
        #self.captureGraphButton.setGeometry(QtCore.QRect(195, 5, 50, 50))
        self.captureGraphButton.setMinimumSize(50,50)
        self.captureGraphButton.setText("")
        self.captureGraphButton.setObjectName("captureGraphButton")
        
        capturGraphePath = self.resourcePath + "/CaptureGraph.png"
        self.captureGraphButton.setStyleSheet(f"border-image : url({capturGraphePath});")

        self.topLayout.addWidget(self.RunButton)
        self.topLayout.addWidget(self.saveButton)
        self.topLayout.addWidget(self.captureButton)
        self.topLayout.addWidget(self.captureGraphButton)
        spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.topLayout.addItem(spacer)
        
        self.instrumentsWidget = QtWidgets.QWidget()
        self.instrumentsWidget.setGeometry(QtCore.QRect(10, 60, 281, 611))
        self.instrumentsWidget.setStyleSheet("background-color: #DBE7FF;")
        self.instrumentsWidget.setObjectName("instrumentsWidget")
        self.instrumentLayout = QtWidgets.QVBoxLayout()
        self.instrumentsWidget.setLayout(self.instrumentLayout)

        self.bottomLayout.addWidget(self.instrumentsWidget,1)
        self.bottomLayout.addWidget(self.tabWidget,4)
        
        self.addButton = QtWidgets.QPushButton()
        self.addButton.setMinimumSize(30, 31)

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.addButton.setFont(font)
        self.addButton.setStyleSheet("background-color: blue;color : white;")
        self.addButton.setObjectName("addButton")
        
        
        self.instrumentLineLayout = QtWidgets.QHBoxLayout()

        self.line = QtWidgets.QFrame()
        self.line.setGeometry(QtCore.QRect(0, 410, 95, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame()
        self.line_2.setGeometry(QtCore.QRect(180, 410, 95, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.label = QtWidgets.QLabel(parent=self.instrumentsWidget)
        self.label.setGeometry(QtCore.QRect(100, 410, 73, 16))

        self.instrumentLineLayout.addWidget(self.line)
        self.instrumentLineLayout.addWidget(self.label)
        self.instrumentLineLayout.addWidget(self.line_2)

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget()
        self.formLayoutWidget.setMinimumSize(261, 200)
        self.formLayoutWidget.setObjectName("formLayoutWidget")
 
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(0, 20, 0, 20)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.formLayoutWidget.setLayout(self.formLayout)
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.modelComboBox = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.modelComboBox.setStyleSheet("background-color: white;")
        self.modelComboBox.setObjectName("modelComboBox")
        self.modelComboBox.addItem("")
        self.modelComboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.modelComboBox)
        self.label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.addressComboBox = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.addressComboBox.setStyleSheet("background-color: white;")
        self.addressComboBox.setObjectName("addressComboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.addressComboBox)

        for addr in range(30):
            self.addressComboBox.addItem(f"{addr}")

        self.sourceRangeLists = ["Auto", "200 mV", "2 V", "20 V", "200 V"]
        self.measureRangeLists2420 = ["Auto", "1 µA", "10 µA","100 µA", 
                                       "1 mA","10 mA","100 mA",
                                       "1 A"]
        self.measureRangeLists2635b = ["Auto", "100 pA", 
                                       "1 nA", "10 nA", "100 nA",
                                       "1 µA", "10 µA","100 µA", 
                                       "1 mA","10 mA","100 mA",
                                       "1 A", "1.5 A"]

        self.sourceRangeListsValue = ["Auto", "200e-3", "2", "20", "200"]
        self.measureRangeLists2420Value = ["Auto", "1e-6", "10e-6","100e-6", 
                                       "1e-3","10e-3","100e-3",
                                       "1"]
        self.measureRangeLists2635bValue = ["Auto", "100e-12", 
                                       "1e-9", "10e-9", "100e-9",
                                       "1e-6", "10e-6","100e-6", 
                                       "1e-3","10e-3","100e-3",
                                       "1", "1.5"]
        
        self.gridLayoutWidget_3 = QtWidgets.QWidget()
        self.gridLayoutWidget_3.setMinimumSize(261, 100)
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        #self.gridLayoutWidget_3.setStyleSheet("background-color : red;")
        self.smu1Layout = QtWidgets.QVBoxLayout()
        self.smu1Layout.setContentsMargins(0, 0, 0, 0)
        self.smu1Layout.setObjectName("smu1Layout")
        
        self.gridLayoutWidget_3.setLayout(self.smu1Layout)

        self.gridLayoutWidget_4 = QtWidgets.QWidget()
        self.gridLayoutWidget_4.setMinimumSize(261, 100)
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.smu2Layout = QtWidgets.QVBoxLayout()
        self.smu2Layout.setContentsMargins(0, 0, 0, 0)
        self.smu2Layout.setObjectName("smu2Layout")
        self.gridLayoutWidget_4.setLayout(self.smu2Layout)

        self.instrumentLayout.addWidget(self.gridLayoutWidget_3)
        self.instrumentLayout.addWidget(self.gridLayoutWidget_4)
        spacer2 = QtWidgets.QSpacerItem(40, 100, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.instrumentLayout.addItem(spacer2)
        self.instrumentLayout.addLayout(self.instrumentLineLayout)
        self.instrumentLayout.addWidget(self.formLayoutWidget)
        self.instrumentLayout.addWidget(self.addButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        self.menubar.setObjectName("menubar")
        self.menuSave = QtWidgets.QMenu(parent=self.menubar)
        self.menuSave.setObjectName("menuSave")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_Data = QtGui.QAction(parent=MainWindow)
        self.actionSave_Data.setObjectName("actionSave_Data")
        self.menuSave.addAction(self.actionSave_Data)
        self.menubar.addAction(self.menuSave.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.smu2420Button = QtWidgets.QPushButton('2420')
        self.smu2635bButton = QtWidgets.QPushButton('2635b')
        self.smuLabel1 = QtWidgets.QLabel('SMU')
        self.smuLabel1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.smuLabel1.setSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Ignored)
        self.smuLabel2 = QtWidgets.QLabel('SMU')
        self.smuLabel2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.smuLabel2.setSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Ignored)
        self.smu2635bButton.setSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Ignored)
        self.smu2420Button.setSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.smu2635bButton.setStyleSheet("background-color: white;")
        self.smu2420Button.setStyleSheet("background-color: white;")
        self.smu2420Button.setStyleSheet("background-color: white;")
        self.smuLabel1.setStyleSheet("background-color: blue; color : white")
        self.smuLabel2.setStyleSheet("background-color: blue; color : white")
        self.smu2420Button.setFont(font)
        self.smu2635bButton.setFont(font)

        # 이벤트 연결
        self.addButton.clicked.connect(self.addButtonClicked)
        self.smu2420Button.clicked.connect(lambda : self.loadSettings(self.device2420, 0))
        self.smu2635bButton.clicked.connect(lambda : self.loadSettings(self.device2635b, 1))
        self.saveSettingsBt.clicked.connect(lambda : self.saveSettings(self.currSetDevice))
        self.RunButton.clicked.connect(self.runStart)
        self.modeComboBox.currentIndexChanged.connect(self.updateMode)
        self.saveButton.clicked.connect(lambda: self.saveToExcel(MainWindow))
        self.captureButton.clicked.connect(lambda: self.captureScreen(MainWindow))
        self.captureGraphButton.clicked.connect(lambda: self.captureGraph(MainWindow))
        self.startvSpinBox.valueChanged.connect(self.updateStep)
        self.stopvSpinBox.valueChanged.connect(self.updateStep)
        self.SSPpointsSpinBox.valueChanged.connect(self.updateStep)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KeithleyApp"))
        self.label_4.setText(_translate("MainWindow", "Mode"))
        self.label_5.setText(_translate("MainWindow", "Range"))
        self.label_6.setText(_translate("MainWindow", "Limit (A)"))
        self.modeComboBox.setItemText(0, _translate("MainWindow", "Linear Sweep"))
        self.modeComboBox.setItemText(1, _translate("MainWindow", "Bias"))
        self.modeComboBox.setItemText(2, _translate("MainWindow", "Step"))
        self.dualSweepcheckBox.setText(_translate("MainWindow", "Dual Sweep"))
        self.label_14.setText(_translate("MainWindow", "Source"))
        self.label_9.setText(_translate("MainWindow", "Start"))
        self.label_10.setText(_translate("MainWindow", "Stop"))
        self.label_11.setText(_translate("MainWindow", "Step"))
        self.label_20.setText(_translate("MainWindow", "Measure"))
        self.label_15.setText(_translate("MainWindow", "Voltage"))
        self.label_16.setText(_translate("MainWindow", "Current"))
        self.label_21.setText(_translate("MainWindow", "Range"))
        self.label_23.setText(_translate("MainWindow", "Auto Zero"))
        self.autoZeroComboBox.setItemText(0, _translate("MainWindow", "ON"))
        self.autoZeroComboBox.setItemText(1, _translate("MainWindow", "OFF"))
        self.label_26.setText(_translate("MainWindow", "Common Settings"))
        self.label_27.setText(_translate("MainWindow", "Source/Sweep"))
        self.label_28.setText(_translate("MainWindow", "Points"))
        self.label_29.setText(_translate("MainWindow", "Measure Delay"))
        self.label_30.setText(_translate("MainWindow", "Source to"))
        self.label_31.setText(_translate("MainWindow", "Repeat"))
        self.ModelLabel.setText(_translate("MainWindow", "Model : -"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingTab), _translate("MainWindow", "Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tableTab), _translate("MainWindow", "Table"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.graphTab), _translate("MainWindow", "Graph"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.label.setText(_translate("MainWindow", "Instruments"))
        self.label_2.setText(_translate("MainWindow", "Model"))
        self.modelComboBox.setItemText(0, _translate("MainWindow", "2420"))
        self.modelComboBox.setItemText(1, _translate("MainWindow", "2635b"))
        self.label_3.setText(_translate("MainWindow", "Address"))
        self.menuSave.setTitle(_translate("MainWindow", "File"))
        self.actionSave_Data.setText(_translate("MainWindow", "Save Data"))

    def addButtonClicked(self):
        idx = self.modelComboBox.currentIndex()
        addr = self.addressComboBox.currentText()

        if idx == 0: # device 2420
            # 위젯 설정
            self.smu1Layout.addWidget(self.smuLabel1 ,1 )
            self.smu1Layout.addWidget(self.smu2420Button, 3)
            self.addr2420 = addr
            try:
                # device 연결
                deviceStr = f"2420 - {self.addr2420}\nConncted"
                device = self.rm.open_resource(f'GPIB0::{self.addr2420}::INSTR')
                self.smu2420Button.setText(deviceStr) 
                self.device2420 = SMUDevice("2420", device)
                self.thread.setDevice(self.device2420, 0) 
                print("Device 2420 Connected") 
                
            except pyvisa.errors.VisaIOError as e:
                print(e)
                deviceStr = f"2420 - {self.addr2420}\nFailed to Connect"
                self.smu2420Button.setText(deviceStr)
                self.device2420 = None

        elif idx == 1:  # device 2635b
            self.addr2635b
            self.smu2Layout.addWidget(self.smuLabel2, 1)
            self.smu2Layout.addWidget(self.smu2635bButton, 3)
            self.addr2635b = addr

            try:
                # device 연결
                deviceStr = f"2635b - {self.addr2635b}\nConncted"
                device = self.rm.open_resource(f'GPIB1::{self.addr2635b}::INSTR')
                self.smu2635bButton.setText(deviceStr)     
                self.device2635b = SMUDevice("2635b", device)
                self.thread.setDevice(self.device2635b, 1) 

            except Exception as e:
                deviceStr = f"2635b - {self.addr2635b}\nFailed to connect"
                self.smu2635bButton.setText(deviceStr)
                self.device2635b = None
            
    def saveSettings(self, idx):
        self.commonSet.update(self.SSPpointsSpinBox.value(),
                            self.delaySpinBox.value(),
                            self.repeatSpinBox.value())
        self.commonSet.updateDualSweep(self.dualSweepcheckBox.isChecked())

        voltRangeIdx = self.sourceRangeComboBox.currentIndex()
        currRangeIdx = self.measureRangeComboBox.currentIndex()
        modeIdx = self.modeComboBox.currentIndex()
        if idx==0:
            self.device2420.setSweepValues(
                self.startvSpinBox.value(),
                self.stopvSpinBox.value(),
                self.stepvSpinBox.value())
            self.device2420.setRange(self.measureRangeLists2420Value[currRangeIdx], self.sourceRangeListsValue[voltRangeIdx])
            self.device2420.setCurrentLimitValue(self.limitCurrentDSB.value())
            self.device2420.setIdx(modeIdx, voltRangeIdx, currRangeIdx)
        elif idx==1:
            self.device2635b.setSweepValues(
                self.startvSpinBox.value(),
                self.stopvSpinBox.value(),
                self.stepvSpinBox.value())
            self.device2635b.setRange(self.measureRangeLists2635bValue[currRangeIdx], self.sourceRangeListsValue[voltRangeIdx])
            self.device2635b.setCurrentLimitValue(self.limitCurrentDSB.value())
            self.device2635b.setIdx(modeIdx, voltRangeIdx, currRangeIdx)

    def SetCommonSettings(self, settings):

        self.SSPpointsSpinBox.setValue(settings.sweepPoint)
        self.delaySpinBox.setValue(settings. sourceDelay)
        self.repeatSpinBox.setValue(settings.Repeate)

    # device 값을 load 한다
    def loadSettings(self, device, idx):
        self.SetCommonSettings(self.commonSet)
        self.currSetDevice = idx
        self.startvSpinBox.setValue(device.startVolt)
        self.stopvSpinBox.setValue(device.stopVolt)
        self.stepvSpinBox.setValue(device.stepVolt)
        self.limitCurrentDSB.setValue(float(device.currentLimit))
        self.modeComboBox.setCurrentIndex(int(device.modeIdx))
        if idx == 0:  # 2420

            self.ModelLabel.setText("Model : 2420")
            self.sourceRangeComboBox.clear()
            self.sourceRangeComboBox.addItems(self.sourceRangeLists)
            self.measureRangeComboBox.clear()
            self.measureRangeComboBox.addItems(self.measureRangeLists2420)

        elif idx==1: # 2635b

            self.sourceRangeComboBox.clear()
            self.sourceRangeComboBox.addItems(self.sourceRangeLists)
            self.measureRangeComboBox.clear()
            self.measureRangeComboBox.addItems(self.measureRangeLists2635b)
            self.ModelLabel.setText("Model : 2635b")

        self.measureRangeComboBox.setCurrentIndex(int(device.currentRangeIdx))
        self.sourceRangeComboBox.setCurrentIndex(int(device.voltRangeIdx))

    def runStart(self):
        if self.thread.threadReady() :
            self.thread.start()

    # DrainVolt , DrainCurr, DrainLogCurr, GateVolt, GateCurr, GateLogCurr, Time
    def updateTabs(self,  drainVolts , drainCurrs, drainLogCurrs, gateVolts, gateCurrs, gateLogCurrs, time):
        #print(time)
        #print(volts)
        #print(currs)
        self.curve.setData(gateVolts, drainLogCurrs)
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        
        self.table.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(time)))
        self.table.setItem(row_position, 1,  QtWidgets.QTableWidgetItem(str(drainVolts[row_position])))
        self.table.setItem(row_position, 2,  QtWidgets.QTableWidgetItem(str(drainCurrs[row_position])))
        self.table.setItem(row_position, 3,  QtWidgets.QTableWidgetItem(str(drainLogCurrs[row_position])))
        self.table.setItem(row_position, 4,  QtWidgets.QTableWidgetItem(str(gateVolts[row_position])))
        self.table.setItem(row_position, 5,  QtWidgets.QTableWidgetItem(str(gateCurrs[row_position])))
        self.table.setItem(row_position, 6,  QtWidgets.QTableWidgetItem(str(gateLogCurrs[row_position])))

    def updateMode(self):
        mode = self.modeComboBox.currentIndex()
        self.startvSpinBox.setValue(0)
        self.stopvSpinBox.setValue(0)
        if mode == 0 :
            self.startvSpinBox.setEnabled(True)
            self.stopvSpinBox.setEnabled(True)
        #Bias mode
        if mode == 1 :
            self.startvSpinBox.setEnabled(True)
            self.stopvSpinBox.setEnabled(False)
        if mode == 2 :
            self.startvSpinBox.setEnabled(True)
            self.stopvSpinBox.setEnabled(True)

    #self.table 내에 있는 데이터를 저장
    def saveToExcel(self, window):
        path, _ = QtWidgets.QFileDialog.getSaveFileName(window, "Save File", "", "Excel Files (*.xlsx);;All Files (*)")
        
        if path:
            data = []
            for row in range(self.table.rowCount()):
                row_data = []
                for column in range(self.table.columnCount()):
                    item = self.table.item(row, column)
                    row_data.append(item.text() if item else "")
                data.append(row_data)
            # DrainVolt , DrainCurr, DrainLogCurr, GateVolt, GateCurr, GateLogCurr, Time
            df = pd.DataFrame(data, columns=["Time (s)", "Drain Voltage (V)", "Drain Current (A)", "Drain Log Scale Current (A)",
                                               "Gate Voltage (V)", "Gate Current (A)","Gate Log Scale Current (A)"])
            df.to_excel(path, index=False)

    # 현재 윈도우의 내용을 캡처
    def captureScreen(self, winodow):
        
        screenshot = winodow.grab()
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(self, 
                                                   "Save Screenshot", 
                                                   "", 
                                                   "PNG Files (*.png);;All Files (*)")
        if file_name:
            screenshot.save(file_name, "png")

    
    # 현재 윈도우의 내용을 캡처
    def captureScreen(self, window):
        
        screenshot = window.grab()
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(window, 
                                                   "Save Screenshot", 
                                                   "", 
                                                   "PNG Files (*.png);;All Files (*)")
        if file_name:
            screenshot.save(file_name, "png")

    # 현재 그래프 내용을 캡처
    def captureGraph(self, window):
        
        screenshot = self.plotWidget.grab()
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(window, 
                                                   "Save Screenshot", 
                                                   "", 
                                                   "PNG Files (*.png);;All Files (*)")
        if file_name:
            screenshot.save(file_name, "png")

    def updateStep(self):
        start = self.startvSpinBox.value()
        stop = self.stopvSpinBox.value()
        sweep = self.SSPpointsSpinBox.value()
        if self.modeComboBox.currentIndex() != 1:
            step = 0

            if sweep != 1:
                step = (stop-start) / (sweep-1.0)
            else:
                step = stop - start
            self.stepvSpinBox.setValue(step)





from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow

from PyQt6.QtGui import QIcon, QPixmap
from ctypes.wintypes import HANDLE, HICON
from ctypes import windll

import os
import sys

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
        self.setStyleSheet("background-color : #F8F8F8;")

    def setTaskbarIcon(self, icon_path):
        try:
            
            hwnd = self.winId() # 윈도우 핸들 가져오기
            pixmap = QPixmap(icon_path)
            windll.shell32.SHAppBarMessage(0x00C6, 0x00000002, HANDLE(hwnd), HICON(pixmap.toWinHICON()))

        except Exception as e:

            print(f"Failed to set taskbar icon: {e}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow =  KeithleyMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
