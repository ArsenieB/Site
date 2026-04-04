import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                             QPushButton, QTextEdit, QLabel, QColorDialog)
from PyQt6.QtCore import Qt

class MultiToolApp(QWidget):
    def __init__(self):
        super().__init__()

        # Configurarea ferestrei principale
        self.setWindowTitle("PyQt6 Multi-Tool")
        self.setGeometry(100, 100, 400, 300)

        # Layout principal vertical
        self.layout = QVBoxLayout()

        # Etichetă de instrucțiuni
        self.label = QLabel("Introdu textul mai jos:")
        self.layout.addWidget(self.label)

        # Zona de introducere text
        self.text_area = QTextEdit()
        self.layout.addWidget(self.text_area)

        # Buton pentru Majuscule
        self.btn_upper = QPushButton("Transformă în MAJUSCULE")
        self.btn_upper.clicked.connect(self.make_uppercase)
        self.layout.addWidget(self.btn_upper)

        # Buton pentru numărarea cuvintelor
        self.btn_count = QPushButton("Numără cuvintele")
        self.btn_count.clicked.connect(self.count_words)
        self.layout.addWidget(self.btn_count)

        # Buton pentru schimbarea culorii de fundal
        self.btn_color = QPushButton("Schimbă culoarea ferestrei")
        self.btn_color.clicked.connect(self.change_background_color)
        self.layout.addWidget(self.btn_color)

        # Setăm layout-ul ferestrei
        self.setLayout(self.layout)

    # Funcționalitate 1: Modificare Text
    def make_uppercase(self):
        current_text = self.text_area.toPlainText()
        self.text_area.setPlainText(current_text.upper())

    # Funcționalitate 2: Analiză Text
    def count_words(self):
        text = self.text_area.toPlainText()
        words = text.split()
        count = len(words)
        self.label.setText(f"Număr de cuvinte: {count}")

    # Funcționalitate 3: Interacțiune cu Sistemul (Dialog Culori)
    def change_background_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.setStyleSheet(f"background-color: {color.name()};")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MultiToolApp()
    window.show()
    sys.exit(app.exec())