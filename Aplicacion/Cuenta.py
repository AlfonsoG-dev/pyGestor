class miCuenta:
    """
    clase que representa la cuenta de la base de datos
    la cuenta se encuentra en la base de datos esta solo es una clase local
    recibe como valores el id de la cuenta, usuario y contraseña    
    Como es una clase para una cuenta personal no es necesario estructurar la base de datos
    """
    def __init__(self, nIdentificador, nUsuario, nContraseña):
        """
        Metodo constructor de la clase cuenta
        la cuenta se encuentran en la base de datos
        nIdentificador, es el tipo de cuenta. nIdentificador != "" && nIdentificador != None
        nUsuario, es el usuario de la cuentan. Usuario != None && nUsuario != ""
        nContraseña, es la contraseña de la cuenta. nContraseña != None && nContraseña != ""
        asigna los valores por parametro a las varibles del constructor
        """
        self._id = nIdentificador
        self._usuario = nUsuario
        self._pasword = nContraseña
    def __str__(self):
        return f'''
        Id Cuenta: {self._id},
        Nombre: {self._usuario},
        Contraseña: {self._pasword}
        '''
    @property
    def getId(self):
        """ 
        Metodo para obtenre la identificacion de la cuenta
        <pre> la cuenta se encuentra inicializada
        <post> se toma el identificador de la cuenta"""
        return self._id
    @getId.setter
    def setId(self, nIde):
        """ 
        Metodo para cambiar el valor de la identificacion
        <pre> la cuenta se encuentran inicializada
        <post> se cambia el valor del Id
        nIde, es el identificador de la base de datos. nIde != None && nIde != "" """
        self._id = nIde
    @property
    def getUsuario(self):
        """
        Metodo para obtener el usuario de la cuenta  
        <pre>la cuenta se encuentra inicializada
        <post>se toma el usuario de la cuenta
        <return> el usuario de la cuenta 
        """
        return self._usuario
    @getUsuario.setter
    def setUsuario(self, nUsuairo):
        """
        Método para cambiar el usuario de la cuenta por el que llega por parametro
        <pre> la cuenta ya se encuentra inicilizada
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
        return self._pasword
    @getContraseña.setter
    def setContraseña(self, nContraseña):
        """
        Metodo que permite cambiar la contraseña del usuario por parametro
        <pre>los usurios ya se encuentran inicializados
        <post> se cambio la contraseña por la que llega por parametro
        nContraseña, es la contrasela del usuario. nContraseña > 0 && nContraseña != None
        """
        self._pasword = nContraseña
