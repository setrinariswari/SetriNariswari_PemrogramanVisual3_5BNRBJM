from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel, QHBoxLayout

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        btn1 = QPushButton("Btn1")
        btn2 = QPushButton("Btn2")
        btn3 = QPushButton("Btn3")
        btn4 = QPushButton("Btn4")
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()
