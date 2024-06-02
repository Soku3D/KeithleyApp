import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QSizePolicy
from PyQt6.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        # 레이아웃 설정
        vbox = QVBoxLayout()
        
        # QLabel 생성
        label = QLabel('This is a label', self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # QPushButton 생성
        button = QPushButton('This is a button', self)
        
        # QLabel과 QPushButton의 크기 정책 설정
        label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        button.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        
        # QLabel과 QPushButton을 레이아웃에 추가
        vbox.addWidget(label, 1)  # 1/4 비율로 설정
        vbox.addWidget(button, 3) # 3/4 비율로 설정
        
        # 레이아웃을 메인 위젯에 설정
        self.setLayout(vbox)
        
        self.setWindowTitle('QVBoxLayout Example')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
