import sys
import sqlite3
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.baglanti_olustur()
        self.init_ui()
    def baglanti_olustur(self):
        self.con=sqlite3.connect("kendiminki.db")
        self.cursor=self.con.cursor()
        self.cursor.execute("Create Table If not Exists üyelerim (kullanici_adi TEXT,parola TEXT)")
        self.con.commit()
    def init_ui(self):
        self.kullanici_adi=QtWidgets.QLineEdit()
        self.parola=QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris=QtWidgets.QPushButton("Giriş")
        self.kayit_olma=QtWidgets.QPushButton("Kayıt olunuz")
        self.yazi_alani=QtWidgets.QLabel("")

        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris)
        v_box.addWidget(self.kayit_olma)

        h_box=QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)
        self.setWindowTitle("Kullanici Girişi")
        self.giris.clicked.connect(self.login)
        self.kayit_olma.clicked.connect(self.kayit)
        self.show()

    def login(self):
        adi=self.kullanici_adi.text()
        par=self.parola.text()
        self.cursor.execute("Select * From üyelerim where kullanici_adi=? and parola=?",(adi,par))
        data=self.cursor.fetchall()

        if len(data)==0:
            self.yazi_alani.setText("Yanlış Parola veya kullanıcı adı\n Lütfen tekrar deneyiniz...")
        else:
            self.yazi_alani.setText("Hoşgeldiniz"+adi)
    def kayit(self):
        ad_ekle=input("Adınız: ")
        parola_ekle=input("Parolanız: ")

        self.cursor.execute("Insert into üyelerim Values(?,?)",(ad_ekle,parola_ekle))

        self.con.commit()
app=QtWidgets.QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())
