# Form implementation generated from reading ui file 'AppUI_2_0.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import pyvisa

class SMUDevice(object):
    device = None
    mode = "Bias"
    voltRange = 0
    currRange = 0
    currLimit = 0.1
    
    startV = 0
    stopV = 0
    stepV = 0

    # def __init__(self, d):
    #     super().__init__()
    #     self.rm = pyvisa.ResourceManager()
    #     self.device = d
    def __init__(self):
        super().__init__()
        self.rm = pyvisa.ResourceManager()
        #self.device = d
    


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
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(300, 60, 961, 611))
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
        self.checkBox = QtWidgets.QCheckBox(parent=self.formLayoutWidget_2)
        self.checkBox.setObjectName("checkBox")
        self.modeFormLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.checkBox)
        self.limitCurrentDSB = QtWidgets.QDoubleSpinBox(parent=self.formLayoutWidget_2)
        self.limitCurrentDSB.setStyleSheet("background-color: white;")
        self.limitCurrentDSB.setObjectName("limitCurrentDSB")
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
        self.startVformLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.stepvSpinBox)
        self.stopvSpinBox = QtWidgets.QSpinBox(parent=self.formLayoutWidget_3)
        self.stopvSpinBox.setStyleSheet("background-color: white;")
        self.stopvSpinBox.setObjectName("stopvSpinBox")
        self.startVformLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.stopvSpinBox)
        self.StartvSpinBox = QtWidgets.QSpinBox(parent=self.formLayoutWidget_3)
        self.StartvSpinBox.setStyleSheet("background-color: white;")
        self.StartvSpinBox.setObjectName("StartvSpinBox")
        self.startVformLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.StartvSpinBox)
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
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.tableTab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 951, 641))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.tableGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.tableGridLayout.setContentsMargins(0, 0, 0, 0)
        self.tableGridLayout.setObjectName("tableGridLayout")
        self.tabWidget.addTab(self.tableTab, "")
        self.graphTab = QtWidgets.QWidget()
        self.graphTab.setObjectName("graphTab")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(parent=self.graphTab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 951, 641))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.graphGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.graphGridLayout.setContentsMargins(0, 0, 0, 0)
        self.graphGridLayout.setObjectName("graphGridLayout")
        self.tabWidget.addTab(self.graphTab, "")
        self.RunButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.RunButton.setGeometry(QtCore.QRect(10, 10, 51, 41))
        self.RunButton.setText("")
        self.RunButton.setObjectName("RunButton")
        self.saveButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(70, 10, 51, 41))
        self.saveButton.setText("")
        self.saveButton.setObjectName("saveButton")
        self.widget_4 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(10, 60, 281, 611))
        self.widget_4.setStyleSheet("background-color: #DBE7FF;")
        self.widget_4.setObjectName("widget_4")
        self.addButton = QtWidgets.QPushButton(parent=self.widget_4)
        self.addButton.setGeometry(QtCore.QRect(100, 550, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.addButton.setFont(font)
        self.addButton.setStyleSheet("background-color: blue;color : white;")
        self.addButton.setObjectName("addButton")
        self.line = QtWidgets.QFrame(parent=self.widget_4)
        self.line.setGeometry(QtCore.QRect(0, 410, 95, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(parent=self.widget_4)
        self.line_2.setGeometry(QtCore.QRect(180, 410, 95, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.label = QtWidgets.QLabel(parent=self.widget_4)
        self.label.setGeometry(QtCore.QRect(100, 410, 73, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.widget_4)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 429, 261, 106))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 20, 0, 20)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
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
        for addr in range(30):
            self.addressComboBox.addItem(f"{addr}")

        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.addressComboBox)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(parent=self.widget_4)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 261, 141))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.smu1Layout = QtWidgets.QVBoxLayout(self.gridLayoutWidget_3)
        self.smu1Layout.setContentsMargins(0, 0, 0, 0)
        self.smu1Layout.setObjectName("smu1Layout")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(parent=self.widget_4)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 160, 261, 141))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.smu2Layout = QtWidgets.QVBoxLayout(self.gridLayoutWidget_4)
        self.smu2Layout.setContentsMargins(0, 0, 0, 0)
        self.smu2Layout.setObjectName("smu2Layout")
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
        self.smuLabel1.setSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        self.smuLabel2 = QtWidgets.QLabel('SMU')
        self.smuLabel2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.smuLabel2.setSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        self.smu2635bButton.setSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
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
        self.smu2420Button.clicked.connect(lambda : self.InitSettings(self.device2420, 0))
        self.smu2635bButton.clicked.connect(lambda : self.InitSettings(self.device2635b, 1))
        self.StartvSpinBox.valueChanged.connect(lambda : self.valueChanged("StartV",self.currSetDevice))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KeithleyApp"))
        self.label_4.setText(_translate("MainWindow", "Mode"))
        self.label_5.setText(_translate("MainWindow", "Range"))
        self.label_6.setText(_translate("MainWindow", "Limit (A)"))
        self.modeComboBox.setItemText(0, _translate("MainWindow", "Bias"))
        self.modeComboBox.setItemText(1, _translate("MainWindow", "Sweep"))
        self.modeComboBox.setItemText(2, _translate("MainWindow", "Step"))
        self.checkBox.setText(_translate("MainWindow", "Dual Sweep"))
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
        if idx == 0:
            # 위젯 설정
            self.smu1Layout.addWidget(self.smuLabel1, 1)
            
            self.smu1Layout.addWidget(self.smu2420Button,4)
            self.addr2420 = addr
            try:
                # device 연결
                device = self.rm.open_resource(f'GPIB::{self.addr2420}::INSTR')
                self.smu2420Button.setText("2420 - {self.addr2420}\nConncted") 
                #self.device2420 = SMUDevice(device)  #TODO : device로 변경  
                self.device2420 = SMUDevice()    
                
            except Exception as e:
                self.smu2420Button.setText(f"2420 - {self.addr2420}\nFailed to connect")
                self.device2420 = SMUDevice() #TODO : NONE 으로 변경

        elif idx == 1:
            self.addr2635b
            self.smu2Layout.addWidget(self.smuLabel2, 1)
            self.smu2Layout.addWidget(self.smu2635bButton,4)
            self.addr2635b = addr

            try:
                # device 연결
                device = self.rm.open_resource(f'GPIB::{self.addr2420}::INSTR')
                self.smu2635bButton.setText("2635b - {self.addr2635b}\nConncted")     
                #self.device2635b = SMUDevice(device) 
            except Exception as e:
                self.smu2635bButton.setText(f"2635b - {self.addr2635b}\nFailed to connect")
                self.device2635b = SMUDevice() #TODO : NONE 으로 변경
            
    def InitSettings(self, device, idx):
        self.StartvSpinBox.setValue(device.startV)
        self.currSetDevice = idx
        if idx==0:
            self.ModelLabel.setText("Model : 2420")
        elif idx==1:
            self.ModelLabel.setText("Model : 2635b")
        
    # settings 값이 변경되면 device 값을 변경시킨다
    def valueChanged(self, valueName, deviceIdx):
        if deviceIdx == 0:
            if valueName == "StartV":
                test = 1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
