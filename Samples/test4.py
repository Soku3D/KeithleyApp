import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMainWindow
from PyQt6.QtCore import QSettings, Qt

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.loadSettings()
    
    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout()
        
        self.label = QLabel("Enter some text:")
        self.layout.addWidget(self.label)
        
        self.text_input = QLineEdit()
        self.layout.addWidget(self.text_input)
        
        self.save_button = QPushButton("Save Settings")
        self.save_button.clicked.connect(self.saveSettings)
        self.layout.addWidget(self.save_button)
        
        self.central_widget.setLayout(self.layout)
        
        self.setWindowTitle('Settings Example')
        self.setGeometry(300, 300, 300, 200)
        
        self.createMenuBar()
        
    def createMenuBar(self):
        menubar = self.menuBar()
        
        file_menu = menubar.addMenu('&File')
        
        save_action = QAction('&Save Settings', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.saveSettings)
        file_menu.addAction(save_action)
        
        exit_action = QAction('&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(qApp.quit)
        file_menu.addAction(exit_action)
    
    def loadSettings(self):
        settings = QSettings('MyCompany', 'MyApp')
        text = settings.value('text', '')
        self.text_input.setText(text)
    
    def saveSettings(self):
        settings = QSettings('MyCompany', 'MyApp')
        settings.setValue('text', self.text_input.text())
        print('Settings saved')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
