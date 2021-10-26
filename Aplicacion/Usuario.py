class Usuario:
    """
    metodo que representa la inicialización de la clase usuario
    el usuario se encuentra en la base de datos este solo es una clase vacia
    recibe como valores la cuenta y contraseña del usuario; no se utiliza un id para la tabla
    Como es una clase para una cuenta personal no es necesario estructurara la base de datos
    """
    def __init__(self, nUsuario, nContraseña):
        """
        Metodo constructor de la clase Usuario
        los usuarios ya se encuentran en la base de datos
        nUsuario, es el usuario de la base de datos. nUsuario != None && nUsuario != ""
        nContraseña, es la contraseña del usurario. nContraseña != None && nContraseña != ""
        asigna los valores por parametro a las varibles del constructor
        """
        self._usuario = nUsuario
        self._password = nContraseña
    @property
    def getUsuario(self):
        """
        Metodo para obtener el usuario
        <pre>los usuarios ya se encuentran inicializados
        <post>se toma el usuario de la cuenta
        <return> el usuario de la cuenta 
        """
        return self._usuario
    @getUsuario.setter
    def setUsuario(self, nUsuairo):
        """
        Método para cambiar el nombre del usuario por el que llega por parametro
        <pre> los usuarios ya se encuentran inicilizados
        <post> se cambio el usuario por el usuario digitado
        nUsuario, es el usuario nuevo. nUsuario != None && nUsuario != ""
        """
        self._usuario = nUsuairo
    @property
    def getContraseña(self):
        """
        Método para obtener la contraseña
        <pre> la contraseña se encuentra inicializada 
        <post> se toma la contraseña de la cuenta
        <retur> la contraseña de la cuenta
        """
        return self._password
    @getContraseña.setter
    def setContraseña(self, nContraseña):
        """
        Metodo que permite cambiar la contraseña del usuario por parametro
        <pre>los usurios ya se encuentran inicializados
        <post> se cambio la contraseña por la que llega por parametro
        nContraseña, es la contrasela del usuario. nContraseña > 0 && nContraseña != None
        """
        self._password = nContraseña