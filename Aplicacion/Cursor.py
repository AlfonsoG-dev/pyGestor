"importar la vitacora"
"from Vitacora import log"
"importal la clase conexion"
from Conexion import Conexion as cn
class CursorDelPool:
    """ 
    Crear el cursor de las conexiones
    <pre>la clase conexion se encuentra inicializada 
    <post> se crea el cursor de la conexion
    """
    def __init__(self) :
        """ 
        Metodo consturctor
        <pre> los atributos ya se encuentran inicializados
        <post> se crea el constructor
        """
        self._conexion = None
        self._cursor = None
    def __enter__(self):
        """ 
        Metodo para crear el cursor y obtenerlo
        <pre>la clase conexion se encuentra inicializada
        <post> se obtiene el cursor """
        self._conexion = cn.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    
    def __exit__(self, tipoExepcion, valorExcepcion, detalleException):
        """ 
        se crea el metodo de salida
        <pre> las clases se encuentran inicializadas
        <post> se cierra el cursor """
        if valorExcepcion:
            self._conexion.rollback()
        else:
            self._conexion.commit()
        self._cursor.close()
        cn.liberarConexion(self._conexion)
