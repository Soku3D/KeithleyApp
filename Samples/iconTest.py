import os
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        # 현재 스크립트 파일의 디렉토리 경로 가져오기
        script_dir = os.path.dirname(sys.executable)

        # 이미지 파일 경로 설정
        #image_path = os.path.join(script_dir, "Run.png")
        application_path = ""
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
            EXE_APPLICATION = True
        elif __file__:
            application_path = os.path.dirname(__file__)
            EXE_APPLICATION = False

        image_path = os.path.join(application_path, "Run.png")
       
        # 버튼 생성 및 이미지 배경 설정
        # for i in range(len(image_path)):
        #     if image_path[i] == 'U':
        #         image_path[i] = "a"
      
        #print(image_path)
        for c in image_path:
            if c == "\\":
                print(c)
        path = image_path.replace("\\", "/")
        print(path)
        button = QPushButton()
        QString  = 'C:/Users/son/KeithleyApp/Samples/Run.png'
        button.setStyleSheet(f"border-image : url({path});")

        layout.addWidget(button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.setWindowTitle("Image Button Example")
    widget.show()
    sys.exit(app.exec())
