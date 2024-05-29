from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPalette, QColor
import sys

app = QApplication(sys.argv)

window = QWidget()
palette = QPalette()
palette.setColor(QPalette.ColorRole.Window, QColor(135, 206, 235))  # RGB 값 설정
window.setPalette(palette)
window.setAutoFillBackground(True)
window.show()

sys.exit(app.exec())
