import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QHBoxLayout, QFileDialog, QMenuBar
import pandas as pd
from PyQt6.QtGui import QAction, QIcon
class TemperatureApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Temperature Logger")
        self.setGeometry(100, 100, 600, 400)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout()
        
        # Input fields for time and temperature
        self.input_layout = QHBoxLayout()
        
        self.time_label = QLabel("Time:")
        self.time_input = QLineEdit()
        self.input_layout.addWidget(self.time_label)
        self.input_layout.addWidget(self.time_input)
        
        self.temp_label = QLabel("Temperature:")
        self.temp_input = QLineEdit()
        self.input_layout.addWidget(self.temp_label)
        self.input_layout.addWidget(self.temp_input)
        
        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.add_data)
        self.input_layout.addWidget(self.add_button)
        
        self.layout.addLayout(self.input_layout)
        
        # Table to display data
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Time", "Temperature"])
        self.layout.addWidget(self.table)
        
        self.central_widget.setLayout(self.layout)
        
        # Menu bar
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)
        
        self.file_menu = self.menu_bar.addMenu("File")
        
        self.save_action = QAction("Save to Excel", self)
        self.save_action.triggered.connect(self.save_to_excel)
        self.file_menu.addAction(self.save_action)
        
    def add_data(self):
        time = self.time_input.text()
        temperature = self.temp_input.text()
        
        if time and temperature:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            
            self.table.setItem(row_position, 0, QTableWidgetItem(time))
            self.table.setItem(row_position, 1, QTableWidgetItem(temperature))
            
            self.time_input.clear()
            self.temp_input.clear()
            
    def save_to_excel(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Excel Files (*.xlsx);;All Files (*)")
        
        if path:
            data = []
            for row in range(self.table.rowCount()):
                row_data = []
                for column in range(self.table.columnCount()):
                    item = self.table.item(row, column)
                    row_data.append(item.text() if item else "")
                data.append(row_data)
                
            df = pd.DataFrame(data, columns=["Time", "Temperature"])
            df.to_excel(path, index=False)

app = QApplication(sys.argv)
window = TemperatureApp()
window.show()
sys.exit(app.exec())
