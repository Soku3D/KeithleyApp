import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QPainter, QColor, QPolygon, QTransform
from PyQt6.QtCore import Qt, QPoint

class TriangleButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(100, 100)
        self.clicked.connect(self.on_clicked)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # 삼각형의 좌표 설정
        points = [QPoint(10, self.height() // 2),
                  QPoint(self.width() - 10, 10),
                  QPoint(self.width() - 10, self.height() - 10)]

        # 삼각형을 오른쪽으로 90도 회전시키기 위해 변환 행렬 생성
        transform = QTransform().rotate(90)

        # 삼각형 좌표를 변환 행렬을 사용하여 회전
        transformed_points = [transform.map(point) for point in points]
        triangle = QPolygon(transformed_points)

        # 삼각형 그리기
        painter.setBrush(QColor(255, 0, 0))  # 버튼의 배경색
        painter.drawPolygon(triangle)

    def on_clicked(self):
        print("Triangle Button Clicked")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Triangle Button Example")
        self.setGeometry(100, 100, 300, 200)

        self.triangle_button = TriangleButton(self)
        self.triangle_button.move(100, 50)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
