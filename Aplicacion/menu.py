from PyQt5.QtWidgets import QMessageBox
from rich import print as pt
from Operacion import Operacion
from Cuenta import miCuenta
from InterfazMenu import *
class MainWindow(QtWidgets.QMainWindow, Ui_GestorPassword):
    """ 
    Clase para crear la relacion con la interfaz y el mundo
    Se importa la clase interfaz
    <pre>la clase interfaz se encuentra inicializada
    <post> se une el mundo con la interfaz
    crea la relacion """
    def __init__(self, *args, **kwargs):
        """ 
        Metodo constructor de la clase
        <pre> se importaron las librerias necesarias
        <post> se realizo la creacion de la ventana """
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        "Accion de limpiar las casillas de texto"
        self.btnLimpiar.clicked.connect(self.limpiar)
        "Accion de buscar usuario e informacion de la cuenta"
        self.btnBuscar.clicked.connect(self.buscar)
    def limpiar(self):
        """ 
        Metodo que limpia las casillas de texto
        <pre> la interfaz se encuentra inicializada
        <post> se limpian las casillas de texto """
        self.txtId.setText(None)
        self.txtPass.setText(None)
        self.txtUsuario.setText(None)

    def buscar(self):
        """ 
        Metodo que aplica acciones a los botones
        <pre>la interfaz ya se encuentra inicializada
        <post> se muestra en las casillas de texto el valor deseado"""
        cuentaBuscada = miCuenta(self.txtId.text(), self.txtUsuario.text(), self.txtPass.text())
        buscar = Operacion.consutlarCuenta(cuentaBuscada.getId)
        if buscar != None:
            for i in buscar:
                self.txtUsuario.setText(i[0])
                self.txtPass.setText(i[1])
            self.txtError.setText(f"La cuenta con id: {cuentaBuscada.getId} fue encontrada con exito")
        else:
            self.txtError.setText(f"La cuenta con id: {cuentaBuscada.getId} no existe, pruebe con otro id")
""" 
 Menu de inicio de la interfaz"""
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()