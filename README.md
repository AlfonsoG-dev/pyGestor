# <h1> GestorPassword </h1>
Proyecto en python para la creacion de un gestor de contraseñas.</p> 
Instrucciones </b>. 
1. Instalar el interprete de python</p>
    - Se recomienda instalar desde winStore o desde la pagina oficial</p>
2. Instalar postgresSQl</p>
    - intalar la ultima version de postgres desde la pagina oficial. </b>
3. Instalar el conector de python para postgresSQL.</p>
    - pip install psycopg2 <b>
Intrucciones para la base de datos</b>.
1. Ir a la clase Conexion e intercambiar los siguientes valores.</p>
    - DATABASE: nombre de la base de datos</b>
    - USERNAME: usuario de la base de datos</b>
    - PASSWORD: contraseña de la base de datos</b>
    - DBPORT: puerto donde opera la base de datos</b>
    - HOST: maquina host de la base de datos</b>
    - MIN: valor minimo de conexiones</b>
    - MAX: valor maximo de conexiones</b>
    - POOL: pool de conexiones</b>
2. utilizar postgres SQl con pgAdmin como gestor de base de datos</p>
    - Crear una base de datos con el nombre de GestorP</b>
    - Crear una tabla en la base de datos con el nombre de cuenta</b>
    - Crear las columnas (id, usuario, contra)</b>
        - id: es el pk de la tabla</b>
        - usuario: es el correo o usuario de una cuenta</b>
        - contra: es la contraseña del correo o cuenta</b>
3. Utilizar Qt designer para el desarrollo de la interfaz grafica</p>
    - Cargar el archivo <interfazQT.ui> y editar si es que se quiere</b>
    - El archivo con extension ui se debe renderizar para python </b>
    - Una ves renderizado lo pasas al directorio de aplicacion y reemplazas por <InterfazMenu.py> que es lo mismo</b>
