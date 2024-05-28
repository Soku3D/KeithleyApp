import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon, QPixmap
from ctypes import windll
from ctypes.wintypes import HANDLE, HICON

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My PyQt6 App")

        # 윈도우 크기 조절
        self.setGeometry(100, 100, 600, 400)

        # 실행 파일의 절대 경로 구하기
        exe_path = sys.argv[0]
        exe_dir = os.path.dirname(exe_path)

        # 아이콘 파일의 경로 설정
        icon_path = os.path.join(exe_dir, 'Resources/test3.ico')

        # 창 아이콘 설정
        self.setWindowIcon(QIcon(icon_path))

        # 작업 표시줄 아이콘 설정
        self.set_taskbar_icon(icon_path)

    def set_taskbar_icon(self, icon_path):
        try:
            # 윈도우 핸들 가져오기
            hwnd = self.winId()
            
            # 아이콘 파일을 QPixmap으로 로드
            pixmap = QPixmap(icon_path)

            # 작업 표시줄 아이콘 설정
            windll.shell32.SHAppBarMessage(0x00C6, 0x00000002, HANDLE(hwnd), HICON(pixmap.toWinHICON()))

        except Exception as e:
            print(f"Failed to set taskbar icon: {e}")

def main():
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
