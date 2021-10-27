"mejorar presentacion"
from rich import print as pt
"importar conexion"
from Conexion import Conexion
"importar cursor"
from Cursor import CursorDelPool
"importar la clase cuenta"
from Cuenta import miCuenta
"importar vitacora"
from Vitacora import log
class Operacion:
    """ 
    Clase que permite el desarrollo de las consultas sql y mas
    <pre> la clase Cuenta ya se encuentra inicializada 
    <post> se crean las operaciones con las base de datos y la clase contra
    Crear los metodos y funciones con las sentencias sql
    importar las clases y modulos necesarios
    """
    "seleccionar las cuentas desde la base de datos"
    _TODO = 'select * from cuenta order by id'
    "seleccionar usuario dado el nombre de la cuenta o usuario"
    _SELECT = 'select usuario, contra from cuenta where id =%s'
    "registrar una cuenta en la base de datos"
    _INSERT = 'insert into cuenta (id, usuario, contra) values (%s, %s, %s)'
    "actualizar la informacion de la cuenta"
    _UPDATE = 'update cuenta set usuario =%s, contra =%s where id =%s'
    "eliminar una cuenta de la base de datos"
    _DELETE = 'delete from cuenta where id =%s'
    @classmethod
    def listarCuenta(cls):
        """ 
        Metodo que permite listar los usuarios de la base de datos 
        <pre> la base de datos se encuentra inicializada
        <post> se listan las cuentas de la base de datos
        <return> la lista de cuentas en la base de datos """
        with CursorDelPool() as cursor:
            cursor.execute(cls._TODO)
            registros = cursor.fetchall()
            cuentas = []
            for x in registros:
                cuenta = miCuenta(x[0], x[1], x[2])
                cuentas.append(cuenta)
            return cuentas
    @classmethod
    def consutlarCuenta(cls, nId):
        """ 
        Metodo para consultar la cuenta dado el id
        <pre> la base de datos se encuentra inicializada
        <post> se consulta la informacion de la cuenta 
        nId, es el id de la cuenta. nId != "" && nId != None
        <return> se retorna la cuenta correspondiente"""
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECT, (nId,))
            registro = cursor.fetchone()
            cuentas = []
            if registro != None:
                cuentas.append(registro)
                return cuentas
            else:
                pt(f"Error al momento de cunsultar el usuario: {nId}")
    @classmethod
    def registrarCuenta(cls, cuenta):
        """ 
        Metodo para registrar una cuenta nueva en el sistema
        <pre> la base de datos seencuentra inicializada
        <post> se registra una nueva cuenta en la base de datos
        cuenta, es la cuenta a registrar. cuenta != "" && cuenta != None
        <return> mensaje de registro con el id de la cuenta """
        with CursorDelPool() as cursor:
            valores = (cuenta.getId, cuenta.getUsuario, cuenta.getContraseña)
            cursor.execute(cls._INSERT, valores)
            pt(f"Se registro la cuenta: {cuenta.getId}")
            return cursor.rowcount
    @classmethod
    def actualizarCuenta(cls, cuenta):
        """ 
        Metodo para cambiar la informacion de la cuenta
        <pre> la base de datos se encuentra inicializada
        <post> se actualiza la informacion de la cuenta
        cuenta, es la cuenta a actualizar. cuenta != "" && cuenta != None
        <return> mensaje de actualizacion con el id de la cuenta """
        with CursorDelPool() as cursor:
            valores = (cuenta.getUsuario, cuenta.getContraseña, cuenta.getId)
            cursor.execute(cls._UPDATE, valores)
            pt(f"Se actualizo la informacion de lacuenta: {cuenta.getId}")
            return cursor.rowcount
    @classmethod
    def eliminarCuenta(cls, nId):
        """ 
        Metodo para eliminar la cuenta de la base de datos dado el Id
        <pre> la base de datos se encuentra inicializada
        <post> se elimino la cuenta de la base de datos
        nId, es el id  de la cuenta a eliminar. nIde != None && nIde != ""
        <return> mensaje de eliminacion con el id de la cuenta """
        with CursorDelPool() as cursor:
            cursor.execute(cls._DELETE, (nId,))
            pt(f"Se elimino la cuenta: {nId}")
            return cursor.rowcount