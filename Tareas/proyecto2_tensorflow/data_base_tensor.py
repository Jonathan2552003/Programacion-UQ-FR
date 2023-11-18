import tensorflow as tf
import numpy as np
import mysql.connector

# Datos de conexión a MySQL
db_connection = mysql.connector.connect(
# db_user = "root"  # Nombre de usuario de MySQL
# db_password = ""  # Contraseña de MySQL (en blanco)
host = "localhost",
user="root",
password="",
port = 3306,
database = "MRU",
)
# Consulta SQL para obtener datos de tiempo y posición
query = "SELECT tiempo, posicion FROM tiempo"
cursor = db_connection.cursor()
cursor.execute(query)

# Recopilar datos de tiempo y posición desde la base de datos
tiempo2 = []
posicion2=[]

for (t, x) in cursor:
    tiempo2.append(t)
    posicion2.append(x)

cursor.close()

print(tiempo2)
print(posicion2)

#Ahora convertimos las listas en datos de numpy
# Datos de entrada: tiempo
tiempo = np.array(tiempo2, dtype=float)
# Datos de salida: posición del objeto
posicion = np.array(posicion2,dtype=float)


#VAMOS A CREAR EL MODELO 
#Creamos 3 capas
modelo = tf.keras.Sequential([
    #unists = numero de nodos(relaciones) que se crean entre los datos
    #activation = modo en el que queremos que se ejecute el algoritmo de aprendizaje
    #input_shape =[datos a predecir]---->Metemos tiempo nos entrega posicion
    tf.keras.layers.Dense(units=64, activation='relu', input_shape=[1]), #Esto es una capa
    tf.keras.layers.Dense(units=64, activation='relu'), #Capa intermedia
    tf.keras.layers.Dense(units=1) #Capa de salida, nos devuelve una unidad de posicion
])


#Ahora lo vamos a entrenar
#Vamos a usar el metodo de optimizacion
#loss: Metodos de manejo de reduccion de error
modelo.compile(optimizer='adam', loss='mean_squared_error')
modelo.fit(tiempo, posicion, epochs=10000) #Tiene 10mil repeticiones



#Ahora que empiece a hacer las predicciones 
tiempo_predicho = np.array([50], dtype=float)
posicion_predicha = modelo.predict(tiempo_predicho)
print("Posición predicha:", posicion_predicha[0][0])