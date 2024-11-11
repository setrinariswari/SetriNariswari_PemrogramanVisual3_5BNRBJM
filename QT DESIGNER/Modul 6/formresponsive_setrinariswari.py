import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QCheckBox, QRadioButton, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Form Responsive")
        self.setGeometry(100, 100, 800, 600)

        # Warna latar belakang
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#FFDDDD"))
        self.setPalette(palette)

        # Widget utama
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # Layout utama
        main_layout = QHBoxLayout(main_widget)

        # Sidebar Kiri
        sidebar_layout = QVBoxLayout()
        main_layout.addLayout(sidebar_layout)

        # Input teks
        text_input = QLineEdit()
        text_input.setPlaceholderText("Type Here")
        sidebar_layout.addWidget(text_input)

        # Tombol di sidebar kiri
        button_layout = QVBoxLayout()
        for _ in range(4):
            button = QPushButton("PushButton")
            button.setStyleSheet("background-color: #7FFFD4;")
            button_layout.addWidget(button)
        sidebar_layout.addLayout(button_layout)

        # Checkbox
        checkbox_layout = QVBoxLayout()
        for _ in range(5):
            checkbox = QCheckBox("CheckBox")
            checkbox_layout.addWidget(checkbox)
        sidebar_layout.addLayout(checkbox_layout)

        # Radio Button
        radio_button_layout = QVBoxLayout()
        for _ in range(5):
            radio_button = QRadioButton("RadioButton")
            radio_button_layout.addWidget(radio_button)
        sidebar_layout.addLayout(radio_button_layout)

        # Area utama kanan
        main_area_layout = QVBoxLayout()
        main_layout.addLayout(main_area_layout)

        # Tombol di atas area utama
        top_button_layout = QHBoxLayout()
        for _ in range(4):
            button = QPushButton("PushButton")
            button.setStyleSheet("background-color: #FF7F7F;")
            top_button_layout.addWidget(button)
        main_area_layout.addLayout(top_button_layout)

        # Area utama
        main_area = QWidget()
        main_area.setStyleSheet("background-color: #FFDDDD; border: 1px solid #7FFFD4;")
        main_area_layout.addWidget(main_area)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
