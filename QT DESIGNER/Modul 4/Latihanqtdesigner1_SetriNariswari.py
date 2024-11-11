import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Mahasiswa")
        self.setGeometry(100, 100, 500, 400)

        # Widget Utama
        widget = QWidget()
        self.setCentralWidget(widget)

        # Layout Utama
        main_layout = QVBoxLayout()

        # Layout Form
        form_layout = QGridLayout()

        # Label dan Input
        labels = ["NIM", "NAMA", "KELAS", "TEMPAT LAHIR", "TANGGAL LAHIR", "TELEPON", "ALAMAT"]
        self.inputs = {}

        for i, label in enumerate(labels):
            lbl = QLabel(label)
            inp = QLineEdit()
            form_layout.addWidget(lbl, i, 0)
            form_layout.addWidget(inp, i, 1)
            self.inputs[label] = inp

        main_layout.addLayout(form_layout)

        # Layout Tombol
        button_layout = QHBoxLayout()
        
        # Tombol Simpan
        btn_simpan = QPushButton("SIMPAN")
        btn_simpan.setStyleSheet("background-color: green; color: white;")
        button_layout.addWidget(btn_simpan)

        # Tombol Edit
        btn_edit = QPushButton("EDIT")
        btn_edit.setStyleSheet("background-color: yellow; color: black;")
        button_layout.addWidget(btn_edit)

        # Tombol Hapus
        btn_hapus = QPushButton("HAPUS")
        btn_hapus.setStyleSheet("background-color: red; color: white;")
        button_layout.addWidget(btn_hapus)

        # Tombol Batal
        btn_batal = QPushButton("BATAL")
        btn_batal.setStyleSheet("background-color: yellow; color: black;")
        button_layout.addWidget(btn_batal)

        main_layout.addLayout(button_layout)

        # Set Layout Utama ke Widget
        widget.setLayout(main_layout)

        # Menambahkan fungsi aksi tombol (opsional)
        btn_simpan.clicked.connect(self.simpan_data)
        btn_edit.clicked.connect(self.edit_data)
        btn_hapus.clicked.connect(self.hapus_data)
        btn_batal.clicked.connect(self.batal_aksi)

    def simpan_data(self):
        # Fungsi untuk aksi tombol SIMPAN
        print("Data disimpan")

    def edit_data(self):
        # Fungsi untuk aksi tombol EDIT
        print("Data diedit")

    def hapus_data(self):
        # Fungsi untuk aksi tombol HAPUS
        print("Data dihapus")

    def batal_aksi(self):
        # Fungsi untuk aksi tombol BATAL
        for inp in self.inputs.values():
            inp.clear()
        print("Input dibersihkan")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
