import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        uic.loadUi('QT DESIGNER/MODUL 4/Latihanqtdesigner.ui', self)

        # Ambil referensi ke widget input dan tombol
        self.input_nim = self.findChild(QLineEdit, 'lineEdit')  # Ganti dengan objectName untuk input NIM
        self.input_nama = self.findChild(QLineEdit, 'lineEdit_2')  # Ganti dengan objectName untuk input Nama
        self.button1 = self.findChild(QPushButton, 'pushButton')  # Ganti dengan objectName untuk tombol pertama
        self.button2 = self.findChild(QPushButton, 'pushButton_2')  # Ganti dengan objectName untuk tombol kedua

        # Hubungkan tombol dengan fungsi
        self.button1.clicked.connect(self.show_data)
        self.button2.clicked.connect(self.clear_data)

    def show_data(self):
        nim = self.input_nim.text()
        nama = self.input_nama.text()
        print(f'NIM: {nim}\nNama: {nama}')

    def clear_data(self):
        self.input_nim.clear()
        self.input_nama.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
