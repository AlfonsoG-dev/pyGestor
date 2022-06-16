"importar la vitacora de registros"
"from Vitacora import log"
"importar el moduo de conexion a la base de datos postgres SQL"
from psycopg2 import pool
"importar sys"
import sys
"Inicializar la clase"
class Conexion:
    "Nombre de la base de datos"
    _DATABASE = 'GestorP'
    "Nombre del usuario de la base de datos"
    _USERNAME = 'postgres'
    "Contraseña de la base de datos"
    _PASSWORD = '5x5W12'
    "Puerto de la base de datos o el gestor?"
    _DBPORT = '5432'
    "Host o equipo de la base de datos"
    _HOST = 'localHost'
    "Minimo de conexiones"
    _MIN = '1'
    "Maximo de conexiones"
    _MAX = '5'
    "lista o pool de conexiones"
    _POOL = None

    @classmethod
    def obtenerPool(cls):
        """ 
        Metodo para asignar la conexion a los usuarios de la aplicacion 
        <pre>los atributos  database, user, password, port y host se encuentran declarados
        <post> se crean las conexiones
        """
        if cls._POOL is None:
            try:
                cls._POOL = pool.SimpleConnectionPool(cls._MIN, cls._MAX, 
                host = cls._HOST,
                user = cls._USERNAME,
                password = cls._PASSWORD,
                port = cls._DBPORT,
                database = cls._DATABASE)
                return cls._POOL
            except Exception as e:
                print(e)
                sys.exit()
        else:
            return cls._POOL
    @classmethod
    def obtenerConexion(cls):
        """ 
        Metodo para obtener la conexion del pool
        <pre> el pool ya se encuentra inicializado 
        <post> se obtine la conexion del pool
        """
        conexion = cls.obtenerPool().getconn()
        return conexion
    @classmethod
    def liberarConexion(cls, conexion):
        """ 
        Metodo que libera la conexion de las conexiones asignadas
        <pre> se asigno una conexion 
        <post> se libero la conexion asignada
        """
        cls.obtenerPool().putconn(conexion)        
    @classmethod
    def cerrarConexion(cls):
        """ 
        metodo para cerrar la conexion con la base de datos
        <pre> la conexion se encuentra inicializada 
        <post> se cerro la conexion
        """
        cls.obtenerPool().closeall()
