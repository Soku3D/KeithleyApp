import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt6.QtGui import QColor, QFont
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTableWidget Styling Example')
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.table_widget = QTableWidget(5, 3, self)
        self.layout.addWidget(self.table_widget)

        # 테이블 스타일 설정
        self.table_widget.setStyleSheet("""
            QTableWidget {
                background-color: #f0f0f0;
                gridline-color: #d0d0d0;
                font-size: 14px;
            }
            QTableWidget::item {
                padding: 10px;
            }
        """)

        # 셀 스타일 설정
        for row in range(5):
            for col in range(3):
                item = QTableWidgetItem(f"Item {row+1},{col+1}")
                if row % 2 == 0:
                    item.setBackground(QColor("#c0c0c0"))
                item.setFont(QFont("Arial", 12, QFont.Weight.Bold))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.table_widget.setItem(row, col, item)

        # 헤더 스타일 설정
        self.table_widget.horizontalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: #404040;
                color: #ffffff;
                font-weight: bold;
                font-size: 16px;
                border: 1px solid #6c6c6c;
                padding: 5px;
            }
        """)
        self.table_widget.verticalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: #404040;
                color: #ffffff;
                font-weight: bold;
                font-size: 16px;
                border: 1px solid #6c6c6c;
                padding: 5px;
            }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
