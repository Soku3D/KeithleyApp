# Form implementation generated from reading ui file 'AppUI_2_0.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(300, 60, 961, 611))
        self.tabWidget.setObjectName("tabWidget")
        self.settingTab = QtWidgets.QWidget()
        self.settingTab.setObjectName("settingTab")
        self.widget = QtWidgets.QWidget(parent=self.settingTab)
        self.widget.setGeometry(QtCore.QRect(40, 60, 441, 211))
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
        self.comboBox_3 = QtWidgets.QComboBox(parent=self.formLayoutWidget_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.modeFormLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboBox_3)
        self.comboBox_4 = QtWidgets.QComboBox(parent=self.formLayoutWidget_2)
        self.comboBox_4.setObjectName("comboBox_4")
        self.modeFormLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboBox_4)
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
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(parent=self.formLayoutWidget_2)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.modeFormLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.doubleSpinBox)
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
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(250, 60, 171, 124))
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
        self.spinBox_2 = QtWidgets.QSpinBox(parent=self.formLayoutWidget_3)
        self.spinBox_2.setEnabled(True)
        self.spinBox_2.setObjectName("spinBox_2")
        self.startVformLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.spinBox_2)
        self.spinBox_3 = QtWidgets.QSpinBox(parent=self.formLayoutWidget_3)
        self.spinBox_3.setObjectName("spinBox_3")
        self.startVformLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.spinBox_3)
        self.spinBox_4 = QtWidgets.QSpinBox(parent=self.formLayoutWidget_3)
        self.spinBox_4.setObjectName("spinBox_4")
        self.startVformLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.spinBox_4)
        self.label_12 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.startVformLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_12)
        self.label_13 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.startVformLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_13)
        self.widget_2 = QtWidgets.QWidget(parent=self.settingTab)
        self.widget_2.setGeometry(QtCore.QRect(40, 270, 441, 231))
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
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(90, 60, 101, 106))
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
        self.checkBox_2 = QtWidgets.QCheckBox(parent=self.formLayoutWidget_5)
        self.checkBox_2.setText("")
        self.checkBox_2.setTristate(False)
        self.checkBox_2.setObjectName("checkBox_2")
        self.startVformLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(parent=self.formLayoutWidget_5)
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.startVformLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.checkBox_3)
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
        self.comboBox_5 = QtWidgets.QComboBox(parent=self.formLayoutWidget_4)
        self.comboBox_5.setObjectName("comboBox_5")
        self.startVformLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboBox_5)
        self.label_22 = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.startVformLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_22)
        self.label_23 = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        self.label_23.setObjectName("label_23")
        self.startVformLayout_3.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_23)
        self.comboBox_6 = QtWidgets.QComboBox(parent=self.formLayoutWidget_4)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.startVformLayout_3.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboBox_6)
        self.widget_3 = QtWidgets.QWidget(parent=self.settingTab)
        self.widget_3.setGeometry(QtCore.QRect(489, 59, 441, 271))
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
        self.label_27.setGeometry(QtCore.QRect(30, 70, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_28.setGeometry(QtCore.QRect(30, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_29.setGeometry(QtCore.QRect(30, 150, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_30.setGeometry(QtCore.QRect(30, 130, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_31.setGeometry(QtCore.QRect(30, 200, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.pointsSpinBox = QtWidgets.QSpinBox(parent=self.widget_3)
        self.pointsSpinBox.setGeometry(QtCore.QRect(140, 80, 101, 31))
        self.pointsSpinBox.setObjectName("pointsSpinBox")
        self.delaySpinBox = QtWidgets.QSpinBox(parent=self.widget_3)
        self.delaySpinBox.setGeometry(QtCore.QRect(140, 140, 101, 31))
        self.delaySpinBox.setObjectName("delaySpinBox")
        self.reapeatSpinBox = QtWidgets.QSpinBox(parent=self.widget_3)
        self.reapeatSpinBox.setGeometry(QtCore.QRect(140, 200, 101, 31))
        self.reapeatSpinBox.setObjectName("reapeatSpinBox")
        self.label_32 = QtWidgets.QLabel(parent=self.settingTab)
        self.label_32.setGeometry(QtCore.QRect(20, 10, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        self.label_32.setFont(font)
        self.label_32.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_32.setObjectName("label_32")
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
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 281, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 490, 95, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 490, 73, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.line_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(190, 490, 95, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 509, 281, 91))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 20, 0, 20)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.comboBox = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboBox)
        self.label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboBox_2)
        self.addButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(110, 610, 75, 31))
        self.addButton.setObjectName("addButton")
        self.RunButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.RunButton.setGeometry(QtCore.QRect(10, 10, 51, 41))
        self.RunButton.setText("")
        self.RunButton.setObjectName("RunButton")
        self.saveButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(70, 10, 51, 41))
        self.saveButton.setText("")
        self.saveButton.setObjectName("saveButton")
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KeithleyApp"))
        self.label_4.setText(_translate("MainWindow", "Mode"))
        self.label_5.setText(_translate("MainWindow", "Range"))
        self.label_6.setText(_translate("MainWindow", "Limit (A)"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Bias"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Sweep"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Step"))
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
        self.comboBox_6.setItemText(0, _translate("MainWindow", "ON"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "OFF"))
        self.label_26.setText(_translate("MainWindow", "Common Settings"))
        self.label_27.setText(_translate("MainWindow", "Source/Sweep"))
        self.label_28.setText(_translate("MainWindow", "Points"))
        self.label_29.setText(_translate("MainWindow", "Measure Delay"))
        self.label_30.setText(_translate("MainWindow", "Source to"))
        self.label_31.setText(_translate("MainWindow", "Reapeat"))
        self.label_32.setText(_translate("MainWindow", "Model : -"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingTab), _translate("MainWindow", "Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tableTab), _translate("MainWindow", "Table"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.graphTab), _translate("MainWindow", "Graph"))
        self.label.setText(_translate("MainWindow", "Instruments"))
        self.label_2.setText(_translate("MainWindow", "Model"))
        self.comboBox.setItemText(0, _translate("MainWindow", "2420"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2635b"))
        self.label_3.setText(_translate("MainWindow", "Address"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "6"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "7"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "8"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "9"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "10"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "11"))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "12"))
        self.comboBox_2.setItemText(12, _translate("MainWindow", "13"))
        self.comboBox_2.setItemText(13, _translate("MainWindow", "14"))
        self.comboBox_2.setItemText(14, _translate("MainWindow", "15"))
        self.comboBox_2.setItemText(15, _translate("MainWindow", "16"))
        self.comboBox_2.setItemText(16, _translate("MainWindow", "17"))
        self.comboBox_2.setItemText(17, _translate("MainWindow", "18"))
        self.comboBox_2.setItemText(18, _translate("MainWindow", "19"))
        self.comboBox_2.setItemText(19, _translate("MainWindow", "20"))
        self.comboBox_2.setItemText(20, _translate("MainWindow", "21"))
        self.comboBox_2.setItemText(21, _translate("MainWindow", "22"))
        self.comboBox_2.setItemText(22, _translate("MainWindow", "23"))
        self.comboBox_2.setItemText(23, _translate("MainWindow", "24"))
        self.comboBox_2.setItemText(24, _translate("MainWindow", "25"))
        self.comboBox_2.setItemText(25, _translate("MainWindow", "26"))
        self.comboBox_2.setItemText(26, _translate("MainWindow", "27"))
        self.comboBox_2.setItemText(27, _translate("MainWindow", "28"))
        self.comboBox_2.setItemText(28, _translate("MainWindow", "29"))
        self.comboBox_2.setItemText(29, _translate("MainWindow", "30"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.menuSave.setTitle(_translate("MainWindow", "File"))
        self.actionSave_Data.setText(_translate("MainWindow", "Save Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())