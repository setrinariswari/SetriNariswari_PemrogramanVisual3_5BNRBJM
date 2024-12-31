from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import mysql.connector as mc


class Ui_Kategori(object):
    def setupUi(self, Kategori):
        Kategori.setObjectName("Kategori")
        Kategori.resize(400, 513)

        # Layout Tombol
        self.horizontalLayoutWidget = QtWidgets.QWidget(Kategori)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 140, 321, 31))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.pushButtonInsert = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonInsert.setObjectName("pushButtonInsert")
        self.horizontalLayout.addWidget(self.pushButtonInsert)

        self.pushButtonUpdate = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonUpdate.setObjectName("pushButtonUpdate")
        self.horizontalLayout.addWidget(self.pushButtonUpdate)

        self.pushButtonDelete = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.horizontalLayout.addWidget(self.pushButtonDelete)

        self.pushButtonLoad = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonLoad.setObjectName("pushButtonLoad")
        self.horizontalLayout.addWidget(self.pushButtonLoad)

        # Label Hasil
        self.labelResult = QtWidgets.QLabel(Kategori)
        self.labelResult.setGeometry(QtCore.QRect(30, 180, 300, 16))
        self.labelResult.setObjectName("labelResult")

        # Layout Input
        self.verticalLayoutWidget = QtWidgets.QWidget(Kategori)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 50, 111, 80))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.labelId = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelId.setObjectName("labelId")
        self.verticalLayout.addWidget(self.labelId)

        self.labelName = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelName.setObjectName("labelName")
        self.verticalLayout.addWidget(self.labelName)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Kategori)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(190, 50, 160, 80))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.lineEditId = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEditId.setObjectName("lineEditId")
        self.verticalLayout_2.addWidget(self.lineEditId)

        self.lineEditName = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEditName.setObjectName("lineEditName")
        self.verticalLayout_2.addWidget(self.lineEditName)

        # Tabel Data
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Kategori)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(40, 210, 321, 241))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget_3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["ID Kategori", "Nama Kategori"])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.verticalLayout_3.addWidget(self.tableWidget)

        # Tombol Search
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Kategori)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 460, 321, 31))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.lineEditSearch = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEditSearch.setObjectName("lineEditSearch")
        self.horizontalLayout_2.addWidget(self.lineEditSearch)

        self.pushButtonSearch = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.horizontalLayout_2.addWidget(self.pushButtonSearch)

        # Fungsi Tombol
        self.pushButtonInsert.clicked.connect(self.insert_data)
        self.pushButtonUpdate.clicked.connect(self.update_data)
        self.pushButtonDelete.clicked.connect(self.delete_data)
        self.pushButtonLoad.clicked.connect(self.load_data)
        self.pushButtonSearch.clicked.connect(self.search_data)

        self.retranslateUi(Kategori)
        QtCore.QMetaObject.connectSlotsByName(Kategori)

    def retranslateUi(self, Kategori):
        _translate = QtCore.QCoreApplication.translate
        Kategori.setWindowTitle(_translate("Kategori", "Form Kategori"))
        self.pushButtonInsert.setText(_translate("Kategori", "INSERT"))
        self.pushButtonUpdate.setText(_translate("Kategori", "UPDATE"))
        self.pushButtonDelete.setText(_translate("Kategori", "DELETE"))
        self.pushButtonLoad.setText(_translate("Kategori", "LOAD DATA"))
        self.labelResult.setText(_translate("Kategori", ""))
        self.labelId.setText(_translate("Kategori", "ID Kategori"))
        self.labelName.setText(_translate("Kategori", "Nama Kategori"))
        self.pushButtonSearch.setText(_translate("Kategori", "SEARCH"))

    # Database Operations
    def connect_to_database(self):
        return mc.connect(
            host="localhost",
            user="root",
            password="",
            database="db_penjualan"
        )

    def insert_data(self):
        try:
            mydb = self.connect_to_database()
            cursor = mydb.cursor()
            idkat = self.lineEditId.text()
            namekat = self.lineEditName.text()

            if not idkat or not namekat:
                self.labelResult.setText("ID dan Nama tidak boleh kosong")
                return

            sql = "INSERT INTO kategori (id, name) VALUES (%s, %s)"
            cursor.execute(sql, (idkat, namekat))
            mydb.commit()
            self.labelResult.setText("Data berhasil ditambahkan")
            self.load_data()
        except mc.Error as e:
            self.labelResult.setText(f"Error: {str(e)}")

    def update_data(self):
        try:
            mydb = self.connect_to_database()
            cursor = mydb.cursor()
            idkat = self.lineEditId.text()
            namekat = self.lineEditName.text()

            if not idkat or not namekat:
                self.labelResult.setText("ID dan Nama tidak boleh kosong")
                return

            sql = "UPDATE kategori SET name = %s WHERE id = %s"
            cursor.execute(sql, (namekat, idkat))
            mydb.commit()
            self.labelResult.setText("Data berhasil diperbarui")
            self.load_data()
        except mc.Error as e:
            self.labelResult.setText(f"Error: {str(e)}")

    def delete_data(self):
        try:
            mydb = self.connect_to_database()
            cursor = mydb.cursor()
            idkat = self.lineEditId.text()

            if not idkat:
                self.labelResult.setText("ID tidak boleh kosong")
                return

            sql = "DELETE FROM kategori WHERE id = %s"
            cursor.execute(sql, (idkat,))
            mydb.commit()
            self.labelResult.setText("Data berhasil dihapus")
            self.load_data()
        except mc.Error as e:
            self.labelResult.setText(f"Error: {str(e)}")

    def load_data(self):
        try:
            mydb = self.connect_to_database()
            cursor = mydb.cursor()
            cursor.execute("SELECT id, name FROM kategori")
            results = cursor.fetchall()

            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(results):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

            self.labelResult.setText("Data berhasil dimuat")
        except mc.Error as e:
            self.labelResult.setText(f"Error: {str(e)}")

    def search_data(self):
        try:
            mydb = self.connect_to_database()
            cursor = mydb.cursor()
            search_term = self.lineEditSearch.text()

            sql = "SELECT id, name FROM kategori WHERE name LIKE %s"
            cursor.execute(sql, (f"%{search_term}%",))
            results = cursor.fetchall()

            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(results):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

            self.labelResult.setText("Pencarian selesai")
        except mc.Error as e:
            self.labelResult.setText(f"Error: {str(e)}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Kategori = QtWidgets.QWidget()
    ui = Ui_Kategori()
    ui.setupUi(Kategori)
    Kategori.show()
    sys.exit(app.exec_())
