from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import cl1
import cl2

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(30, 30, 30, 30)
        
        self.kg_input = QLineEdit()
        self.kg_input.setPlaceholderText("Килограммы")
        self.kg_input.textChanged.connect(self.on_kg_changed)
        
        self.grams_input = QLineEdit()
        self.grams_input.setPlaceholderText("Грамм")
        self.grams_input.textChanged.connect(self.on_grams_changed)
        
        self.pounds_input = QLineEdit()
        self.pounds_input.setPlaceholderText("Фунты")
        self.pounds_input.textChanged.connect(self.on_pounds_changed)
        
        kg_label = QLabel("Килограммы:")
        grams_label = QLabel("Грамм:")
        pounds_label = QLabel("Фунты:")
        
        layout.addWidget(kg_label)
        layout.addWidget(self.kg_input)
        layout.addWidget(grams_label)
        layout.addWidget(self.grams_input)
        layout.addWidget(pounds_label)
        layout.addWidget(self.pounds_input)
        
        central_widget.setLayout(layout)
        
        self.setWindowTitle("Конвертер веса")
        self.setFixedSize(350, 350)
        
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)
        
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2c3e50;
            }
            QWidget {
                background-color: #34495e;
            }
            QLabel {
                color: #ecf0f1;
                font-size: 18px;
                font-weight: bold;
                padding: 5px 0;
            }
            QLineEdit {
                background-color: #ffffff;
                border: 2px solid #95a5a6;
                border-radius: 5px;
                padding: 12px;
                font-size: 20px;
                color: #2c3e50;
                min-height: 25px;
            }
            QLineEdit:focus {
                border: 2px solid #3498db;
            }
        """)
        
        self.updating = False
        
        cl1.signals.from_kg.connect(self.update_from_kg)
        cl1.signals.from_grams.connect(self.update_from_grams)
        cl2.signals.from_pounds.connect(self.update_from_pounds)
    
    def on_kg_changed(self, text):
        if self.updating:
            return
        if not text:
            cl1.convert_from_kg(None)
            return
        try:
            text = text.replace(',', '.')
            value = float(text)
            cl1.convert_from_kg(value)
        except ValueError:
            pass
    
    def on_grams_changed(self, text):
        if self.updating:
            return
        if not text:
            cl1.convert_from_grams(None)
            return
        try:
            text = text.replace(',', '.')
            value = float(text)
            cl1.convert_from_grams(value)
        except ValueError:
            pass
    
    def on_pounds_changed(self, text):
        if self.updating:
            return
        if not text:
            cl2.convert_from_pounds(None)
            return
        try:
            text = text.replace(',', '.')
            value = float(text)
            cl2.convert_from_pounds(value)
        except ValueError:
            pass
    
    def update_from_kg(self, kg, grams, pounds):
        self.updating = True
        if kg is None:
            self.grams_input.clear()
            self.pounds_input.clear()
        else:
            self.grams_input.setText(str(round(grams, 2)))
            self.pounds_input.setText(str(round(pounds, 2)))
        self.updating = False
    
    def update_from_grams(self, kg, grams, pounds):
        self.updating = True
        if kg is None:
            self.kg_input.clear()
            self.pounds_input.clear()
        else:
            self.kg_input.setText(str(round(kg, 4)))
            self.pounds_input.setText(str(round(pounds, 4)))
        self.updating = False
    
    def update_from_pounds(self, kg, grams, pounds):
        self.updating = True
        if kg is None:
            self.kg_input.clear()
            self.grams_input.clear()
        else:
            self.kg_input.setText(str(round(kg, 4)))
            self.grams_input.setText(str(round(grams, 2)))
        self.updating = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())