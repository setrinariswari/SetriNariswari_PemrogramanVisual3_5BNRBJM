from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc

class Ui_Kategori(object):
    def setupUi(self, Kategori):
        Kategori.setObjectName("Kategori")
        Kategori.resize(478, 249)

        # Widget Layout Horizontal
        self.horizontalLayoutWidget = QtWidgets.QWidget(Kategori)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 160, 441, 51))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        # Tombol Insert Data
        self.pushButtonInsert = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonInsert.setFont(font)
        self.pushButtonInsert.setObjectName("pushButtonInsert")
        self.horizontalLayout.addWidget(self.pushButtonInsert)

        # Layout Vertikal (Input Fields)
        self.verticalLayoutWidget = QtWidgets.QWidget(Kategori)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(170, 10, 281, 80))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        # Input ID Kategori
        self.lineEditId = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font.setPointSize(12)
        self.lineEditId.setFont(font)
        self.lineEditId.setObjectName("lineEditId")
        self.verticalLayout.addWidget(self.lineEditId)

        # Input Nama Kategori
        self.lineEditName = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditName.setFont(font)
        self.lineEditName.setObjectName("lineEditName")
        self.verticalLayout.addWidget(self.lineEditName)

        # Label Field Names
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Kategori)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 151, 80))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.labelId = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font.setPointSize(12)
        self.labelId.setFont(font)
        self.labelId.setObjectName("labelId")
        self.verticalLayout_2.addWidget(self.labelId)

        self.labelName = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelName.setFont(font)
        self.labelName.setObjectName("labelName")
        self.verticalLayout_2.addWidget(self.labelName)

        # Label Result
        self.labelResult = QtWidgets.QLabel(Kategori)
        self.labelResult.setGeometry(QtCore.QRect(10, 220, 441, 21))
        font.setBold(True)
        font.setWeight(75)
        self.labelResult.setFont(font)
        self.labelResult.setObjectName("labelResult")

        # Connect Button to Function
        self.pushButtonInsert.clicked.connect(self.insertkategori)

        self.retranslateUi(Kategori)
        QtCore.QMetaObject.connectSlotsByName(Kategori)

    def insertkategori(self):
        try:
            # Koneksi ke Database
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="db_penjualan"
            )
            cursor = mydb.cursor()

            # Ambil Data dari Input
            idkat = self.lineEditId.text()
            namekat = self.lineEditName.text()

            # Query Insert
            sql = "INSERT INTO kategori (id, name) VALUES (%s, %s)"
            val = (idkat, namekat)
            cursor.execute(sql, val)
            mydb.commit()

            # Tampilkan Pesan Sukses
            self.labelResult.setText("Data Kategori Berhasil Disimpan")
            self.lineEditId.setText("")
            self.lineEditName.setText("")
        except mc.Error as e:
            # Tampilkan Pesan Error
            self.labelResult.setText(f"Data Kategori Gagal Disimpan: {e}")

    def retranslateUi(self, Kategori):
        _translate = QtCore.QCoreApplication.translate
        Kategori.setWindowTitle(_translate("Kategori", "Form Kategori"))
        self.pushButtonInsert.setText(_translate("Kategori", "INSERT DATA"))
        self.labelId.setText(_translate("Kategori", "ID Kategori"))
        self.labelName.setText(_translate("Kategori", "Nama Kategori"))
        self.labelResult.setText(_translate("Kategori", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Kategori = QtWidgets.QWidget()
    ui = Ui_Kategori()
    ui.setupUi(Kategori)
    Kategori.show()
    sys.exit(app.exec_())
