"importar la vitacora"
from Vitacora import log
"importal la clase conexion"
from Conexion import Conexion
class CursorPool:
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
        log.debug("Inicio del metodo wih")
        self._conexion = Conexion.darConexion()
        self._cursor = self._conexion.cursor()
    
    def __exit__(self, tipoExepcion, valorExcepcion, detalleException):
        """ 
        se crea el metodo de salida
        <pre> las clases se encuentran inicializadas
        <post> se cierra el cursor """
        log.debug("Se ejecuta el cierre")
        if valorExcepcion:
            self._conexion.rollback()
            log.error(f"Ocurrio un error, se hace tollback {valorExcepcion} {tipoExepcion}")
        else:
            self._conexion.commit()
            log.debug("Commit de la transaccion")
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)