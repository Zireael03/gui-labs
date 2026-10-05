from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        
        self.label = QLabel("ПЕЧАТЬ")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("""
            font-size: 38px;
            font-family: 'Impact', sans-serif;
            color: #FF4500;
            background-color: #1a0000;
            font-weight: bold;
            letter-spacing: 2px;
        """)
        
        self.button = QPushButton("Увидеть короля проклятий")
        self.button.clicked.connect(self.change_to_image)
        
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        
        central_widget.setLayout(layout)
        
        self.setWindowTitle("Фансервис магической битвы")
        self.setGeometry(100, 100, 400, 300)
    
    def change_to_image(self):
        pixmap = QPixmap("sukuna.png")  
        
        if pixmap.isNull():
            print("Короля запечатали(((")
            pixmap = QPixmap(200, 150)
            pixmap.fill()
        
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        
        self.button.setText("Бегите, глупцы!")
        self.button.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())