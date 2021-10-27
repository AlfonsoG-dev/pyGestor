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
        "Accion de buscar cuenta e informacion de la cuenta"
        self.btnBuscar.clicked.connect(self.buscar)
        "Acciopn de registrar una cuenta en la base de datos"
        self.btnListar.clicked.connect(self.registrar)
        "Accion de actualizar la información de la cuenta"
        self.btnCambiar.clicked.connect(self.cambiar)
        "Accion de eliminar la información de la cuenta"
        self.btnEliminar.clicked.connect(self.eliminar)
    def limpiar(self):
        """ 
        Metodo que limpia las casillas de texto
        <pre> la interfaz se encuentra inicializada
        <post> se limpian las casillas de texto """
        self.txtId.setText(None)
        self.txtPass.setText(None)
        self.txtUsuario.setText(None)
        self.txtError.setText(None)

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
    def registrar(self):
        """ 
        Metodo que permite registrar una cuentra en la base de datos
        <pre> la base de datos se encuentra inicializada
        <pre> se registra el cuenta en la base de datos
        """
        cuentaRegistrar= miCuenta(self.txtId.text(), self.txtUsuario.text(), self.txtPass.text())
        busqueda = Operacion.consutlarCuenta(cuentaRegistrar.getId)
        if busqueda == None:
            Operacion.registrarCuenta(cuentaRegistrar)
            self.txtError.setText(f"La cuenta con id: {cuentaRegistrar.getId} fue registrada con exito")
        else:
            self.txtError.setText(f"La cuenta con id: {cuentaRegistrar.getId} ya existe, pruebe con otro id")
    def cambiar(self):
        """ 
        Metodo que permite cambiar los valores de la cuenta
        <pre> la lista de atributos de interfaz se encuentran inicializados
        <post> se cambia la informacion de la cuenta """
        cuentaActualizar= miCuenta(self.txtId.text(), self.txtUsuario.text(), self.txtPass.text())
        busqueda = Operacion.consutlarCuenta(cuentaActualizar.getId)
        if busqueda != None:
            Operacion.actualizarCuenta(cuentaActualizar)
            self.txtError.setText(f"La información de la cuenta con id: {cuentaActualizar.getId} y usuario : {cuentaActualizar.getUsuario} fue actualizada con exito con exito")
        else:
            self.txtError.setText(f"La cuenta con id: {cuentaActualizar.getId} No existe, pruebe con otro id")
    def eliminar(self):
        """ 
        metodo que permite eliminar una cuenta de la base de datos
        <pre> la interfaz donde se realiza la accion se encuentra inicializada
        <post> se elimina la cuenta de la base de datos """
        cuentaEliminar= miCuenta(self.txtId.text(), self.txtUsuario.text(), self.txtPass.text())
        busqueda = Operacion.consutlarCuenta(cuentaEliminar.getId)
        if busqueda != None:
            Operacion.eliminarCuenta(cuentaEliminar.getId)
            self.txtError.setText(f"La cuenta con id: {cuentaEliminar.getId} y usuario : {cuentaEliminar.getUsuario} fue eliminada con exito")
        else:
            self.txtError.setText(f"La cuenta con id: {cuentaEliminar.getId} y usuario : {cuentaEliminar.getUsuario} no existe, pruebe con otro id")
            pt(f"Error al tratar de eliminar la cuenta con el id: {cuentaEliminar.getId} tratar de consultar si la cuenta esta en la base de datos")
""" 
 Menu de inicio de la interfaz"""
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
