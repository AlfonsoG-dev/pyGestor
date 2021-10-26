from rich import print as pt
class Operacion:
    """ 
    Clase que permite el desarrollo de las consultas sql y mas
    <pre> la clase Password ya se encuentra inicializada 
    <post> se crean las operaciones con las base de datos y la clase Password
    Crear los metodos y funciones con las sentencias sql
    importar las clases y modulos necesarios
    """
    "seleccionar las cuentas desde la base de datos"
    _TODO = 'select * from cuenta order by identificador'
    "seleccionar usuario dado el nombre de la cuenta o usuario"
    _SELECT = 'select usuario, password from cuenta where identificador = %s'
    "registrar una cuenta en la base de datos"
    _INSERT = 'insert into cuenta (identificador, usuario, password) values (%s, %s, %s)'
    "actualizar la informacion de la cuenta"
    _UPDATE = 'update cuenta set usuario = %s, password = %s where identificador = %s'
    "eliminar una cuenta de la base de datos"
    _DELETE = 'delete from cuenta where identificador = %s'

