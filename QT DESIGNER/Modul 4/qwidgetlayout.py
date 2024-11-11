from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        btn1 = QPushButton("Btn1")
        btn2 = QPushButton("Btn2")
        btn3 = QPushButton("Btn3")
        btn4 = QPushButton("Btn4")
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        self.setLayout(layout)

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()
