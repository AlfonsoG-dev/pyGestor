# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfazQT.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GestorPassword(object):
    def setupUi(self, GestorPassword):
        GestorPassword.setObjectName("GestorPassword")
        GestorPassword.resize(510, 347)
        self.centralwidget = QtWidgets.QWidget(GestorPassword)
        self.centralwidget.setObjectName("centralwidget")
        self.lblUsuario = QtWidgets.QLabel(self.centralwidget)
        self.lblUsuario.setGeometry(QtCore.QRect(40, 90, 71, 21))
        self.lblUsuario.setObjectName("lblUsuario")
        self.lblPass = QtWidgets.QLabel(self.centralwidget)
        self.lblPass.setGeometry(QtCore.QRect(40, 150, 71, 21))
        self.lblPass.setObjectName("lblPass")
        self.lblid = QtWidgets.QLabel(self.centralwidget)
        self.lblid.setGeometry(QtCore.QRect(40, 30, 81, 21))
        self.lblid.setObjectName("lblid")
        self.txtId = QtWidgets.QLineEdit(self.centralwidget)
        self.txtId.setGeometry(QtCore.QRect(120, 30, 151, 20))
        self.txtId.setObjectName("txtId")
        self.btnBuscar = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscar.setGeometry(QtCore.QRect(290, 30, 75, 23))
        self.btnBuscar.setObjectName("btnBuscar")
        self.btnCambiar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCambiar.setGeometry(QtCore.QRect(290, 90, 75, 23))
        self.btnCambiar.setObjectName("btnCambiar")
        self.btnEliminar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEliminar.setGeometry(QtCore.QRect(400, 90, 75, 23))
        self.btnEliminar.setObjectName("btnEliminar")
        self.btnListar = QtWidgets.QPushButton(self.centralwidget)
        self.btnListar.setGeometry(QtCore.QRect(400, 30, 75, 23))
        self.btnListar.setObjectName("btnListar")
        self.btnLimpiar = QtWidgets.QPushButton(self.centralwidget)
        self.btnLimpiar.setGeometry(QtCore.QRect(290, 150, 181, 23))
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.txtUsuario = QtWidgets.QLineEdit(self.centralwidget)
        self.txtUsuario.setGeometry(QtCore.QRect(120, 90, 151, 20))
        self.txtUsuario.setObjectName("txtUsuario")
        self.txtPass = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPass.setGeometry(QtCore.QRect(120, 150, 151, 20))
        self.txtPass.setObjectName("txtPass")
        self.lblError = QtWidgets.QLabel(self.centralwidget)
        self.lblError.setGeometry(QtCore.QRect(170, 180, 171, 31))
        self.lblError.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lblError.setTextFormat(QtCore.Qt.RichText)
        self.lblError.setWordWrap(False)
        self.lblError.setObjectName("lblError")
        self.txtError = QtWidgets.QLineEdit(self.centralwidget)
        self.txtError.setGeometry(QtCore.QRect(50, 220, 401, 81))
        self.txtError.setText("")
        self.txtError.setObjectName("txtError")
        GestorPassword.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GestorPassword)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 21))
        self.menubar.setObjectName("menubar")
        GestorPassword.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GestorPassword)
        self.statusbar.setObjectName("statusbar")
        GestorPassword.setStatusBar(self.statusbar)

        self.retranslateUi(GestorPassword)
        QtCore.QMetaObject.connectSlotsByName(GestorPassword)

    def retranslateUi(self, GestorPassword):
        _translate = QtCore.QCoreApplication.translate
        GestorPassword.setWindowTitle(_translate("GestorPassword", "Gestor de password"))
        self.lblUsuario.setText(_translate("GestorPassword", "Usuario"))
        self.lblPass.setText(_translate("GestorPassword", "Password"))
        self.lblid.setText(_translate("GestorPassword", "Identificador"))
        self.btnBuscar.setText(_translate("GestorPassword", "Buscar"))
        self.btnCambiar.setText(_translate("GestorPassword", "Cambiar"))
        self.btnEliminar.setText(_translate("GestorPassword", "Eliminar"))
        self.btnListar.setText(_translate("GestorPassword", "Listar"))
        self.btnLimpiar.setText(_translate("GestorPassword", "Limpiar"))
        self.lblError.setText(_translate("GestorPassword", "<html><head/><body><p align=\"center\">Error Log</p></body></html>"))
        self.txtError.setToolTip(_translate("GestorPassword", "<html><head/><body><p align=\"center\"><span style=\" text-decoration: underline; color:#aaaaff;\">dddddd</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GestorPassword = QtWidgets.QMainWindow()
    ui = Ui_GestorPassword()
    ui.setupUi(GestorPassword)
    GestorPassword.show()
    sys.exit(app.exec_())

