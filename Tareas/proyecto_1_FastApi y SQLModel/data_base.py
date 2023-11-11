#Cadena de conexion
#Conexion de base de datos con python

from sqlmodel import create_engine #Importamos el "motor de iniciacion"
from sqlmodel.pool import StaticPool #Staticpool nos permite hacer varias peticiones o procesos al tiempo
#
#
#Cadena de base de datos
# Datos de conexión a MySQL
db_user = "root"  # Nombre de usuario de MySQL
db_password = ""  # Contraseña de MySQL (en blanco)
db_host = "localhost" #Esto indica que la base de datos esta en el pc, sino debo de colocar el link de la ubicacion
db_port = 3306
db_name = "ondas"

# Crear una cadena de conexión para MySQL (MySQL es la base de datos)
DATABASE_URL = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"


# para conectarnos motor de la base de datos
     #El engine es la que permite crear la coneccion con la base de datos
     #El StaticPool---> Nos permite hacer varias conexiones
     #El poolclass --->La que se encarga de configurar las conexiones
engine = create_engine(DATABASE_URL, poolclass=StaticPool)