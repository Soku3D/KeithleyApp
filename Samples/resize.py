#resize Winodw 
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 레이아웃 설정
        vbox = QVBoxLayout()
        
        # QLabel 생성
        self.label = QLabel('This is a label', self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # QPushButton 생성
        self.button = QPushButton('This is a button', self)
        
        # QLabel과 QPushButton을 레이아웃에 추가
        vbox.addWidget(self.label)
        vbox.addWidget(self.button)
        
        # 레이아웃을 메인 위젯에 설정
        self.setLayout(vbox)
        
        self.setWindowTitle('Resizable Widgets Example')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def resizeEvent(self, event):
        # 윈도우가 리사이즈 될 때 호출되는 이벤트
        size = event.size()
        self.label.setText(f"Window size: {size.width()} x {size.height()}")
        super().resizeEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
