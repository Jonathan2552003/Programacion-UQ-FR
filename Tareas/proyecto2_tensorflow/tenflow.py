import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
tensor_constante = tf.constant([1,2,3])
print("Tensor constante")
print(tensor_constante.numpy())

tensor_ceros = tf.zeros([3,2,5])
print("Tensor de ceros")
print(tensor_ceros)

tensor_unos = tf.ones([5,6,9])
print("Tensor de unos")
print(tensor_unos.numpy())

tensores_aleatorios = tf.random.normal([3,2], mean=0)
print(tensores_aleatorios)
#Operaciones con tensores
tensor_a = tf.constant([1, 2, 3])
tensor_b = tf.constant([4, 5, 6])
suma = tensor_a + tensor_b
multiplicacion=tensor_a * tensor_b
division= tensor_a/tensor_b
resta=tensor_a-tensor_b
print("suma")
print(suma.numpy())
print("multiplicación")

print(multiplicacion.numpy())
print("división")

print(division.numpy())
print("resta")

print(resta.numpy())

#
# el cálculo de la velocidad final de un objeto que cae libremente
# debido a la gravedad. Supongamos que tienes un objeto que cae desde
# una cierta altura y deseas calcular su velocidad final al tocar el suelo.
# Utilizaremos la ecuación de movimiento uniformemente acelerado:

# vf = raiz cuadrada de velocodad inicial al cuadrado +2*g*h

# Donde:


# vf  es la velocidad final.
# vi  es la velocidad inicial (en este caso, 0, ya que el objeto parte del reposo).
# g es la aceleración debida a la gravedad (aproximadamente -9.81 m/s² en la Tierra).
# h es la altura desde la cual el objeto cae.

import tensorflow as tf

# Datos de entrada
altura = tf.constant(10.0)  # Altura en metros
gravedad = tf.constant(9.81)  # Aceleración debida a la gravedad en m/s^2
velocidad_inicial = tf.constant(0.0)  # Velocidad inicial en m/s
#suponiniendo que en nuestro eje de referencia la posicion inicial es cero

# Cálculos usando tensores
velocidad_final = tf.sqrt((velocidad_inicial**2)+2 * gravedad * altura)
print("Calculo de velocidad final")
print(velocidad_final.numpy())


#Operaciones matematicas

print("Promedio")

temperaturas = tf.constant([25.0, 26.5, 24.8, 27.2, 25.9])  # Mediciones de temperatura en grados Celsius

temperatura_promedio = tf.reduce_mean(temperaturas)

print(temperatura_promedio.numpy())


#Matrices
R = tf.constant([[0.1, -0.5],
                [0.5,3]])  # Matriz de rotación 2x2

R_transpuesta = tf.transpose(R)
print("Original")
print(R.numpy())
print("Transpuestas")
print(R_transpuesta.numpy())

R = tf.constant([[0.866, -0.5],
                [0.5, 0.866]])  # Matriz de rotación 2x2
T_ejemplo = tf.constant([[1.0, 2.0],
                           [3.0, 4.0]])  # Matriz de traslación 2x2

T = tf.matmul(R, T_ejemplo)  # Multiplicacion matricial
print("Original")
print(R.numpy())
print(T_ejemplo.numpy())
print("resultado multiplicacion matricial")

print(T.numpy())



#AQUI VAN LAS DERIVADAS
# Definir una variable
x = tf.Variable(2.0)

# Definir una función
def funcion(x):
    return tf.sin(x) + x**2


# Calcular la primera derivada
with tf.GradientTape() as tape1:
    with tf.GradientTape() as tape2:
        y = funcion(x)
    primera_derivada = tape2.gradient(y, x)
segunda_derivada = tape1.gradient(primera_derivada, x)

# Imprimir la segunda derivada
print("Derivadas")
print(f"Primera derivada de la función con respecto a x en x=2.0: {primera_derivada}")
print(f"Segunda derivada de la función con respecto a x en x=2.0: {segunda_derivada}")



#Problema de fisica 
@tf.function #Realiza los procesos mas rapido
def calcular_trayectoria(tiempo, velocidad_inicial, angulo, k, m):
    # Aceleración debida a la gravedad en m/s^2
    g = 9.81

    # Convertir el ángulo de grados a radianes
    angulo_rad = tf.constant(np.deg2rad(angulo), dtype=tf.float32)

    # Inicializar TensorArrays para las coordenadas X e Y
    x = tf.TensorArray(tf.float32, size=0, dynamic_size=True, clear_after_read=False)
    y = tf.TensorArray(tf.float32, size=0, dynamic_size=True, clear_after_read=False)

    # Establecer las coordenadas iniciales en el origen
    x = x.write(0, tf.constant(0.0))
    y = y.write(0, tf.constant(0.0))

    # Calcular el intervalo de tiempo
    dt = tiempo[1] - tiempo[0]

    # Calcular las componentes de la velocidad inicial
    v_x = velocidad_inicial * tf.cos(angulo_rad)
    v_y = velocidad_inicial * tf.sin(angulo_rad)

    # Bucle para calcular la trayectoria
    for i in tf.range(1, tiempo.shape[0]):
        # Calcular la magnitud de la velocidad
        v = tf.sqrt(v_x*2 + v_y*2)

        # Calcular las aceleraciones en X e Y
        a_x = -k * v_x * v / m
        a_y = -g - k * v_y * v / m

        # Actualizar las componentes de la velocidad
        v_x = v_x + a_x * dt
        v_y = v_y + a_y * dt

        # Actualizar las coordenadas X e Y
        x = x.write(i, x.read(i - 1) + v_x * dt)
        y = y.write(i, y.read(i - 1) + v_y * dt)

    # Devolver las trayectorias en forma de tensores
    return x.stack(), y.stack() #Convierte el tensor array en un tensor normal (matriz)

# Datos de entrada
tiempo = tf.linspace(0.0, 10.0, 1000)  # Vector de tiempo
velocidad_inicial = 50.0  # Velocidad inicial en m/s
angulo = 45  # Ángulo de 45 grados
k = 0.01  # Constante de resistencia al aire
m = 12  # Masa del proyectil en kg

# Calcular la trayectoria del proyectil
trayectoria_x, trayectoria_y = calcular_trayectoria(tiempo, velocidad_inicial, angulo, k, m)

# Visualizar la trayectoria en un gráfico
plt.plot(trayectoria_x.numpy(), trayectoria_y.numpy())
plt.xlabel('Posición en X (metros)')
plt.ylabel('Posición en Y (metros)')
plt.title('Trayectoria de un Proyectil')
plt.show()










#Problema de una aprticula
# Supongamos que tienes una partícula que se mueve a lo largo de una línea recta y su posición
# x(t) en función del tiempo está dada por:
#
# x(t)=3*t*3 -2*t*2 + 4*t+1
class Particula:
    def _init_(self, posicion_inicial, velocidad_inicial):
        self.posicion = tf.Variable(posicion_inicial, dtype=tf.float32)
        self.velocidad = tf.Variable(velocidad_inicial, dtype=tf.float32)

    def actualizar(self, tiempo, aceleracion):
        # Calcular la nueva velocidad y posición
        velocidad = self.velocidad + aceleracion * tiempo
        posicion = self.posicion + self.velocidad * tiempo + 0.5 * aceleracion * tiempo**2

        # Actualizar los valores de la partícula
        self.velocidad.assign(velocidad)
        self.posicion.assign(posicion)

# Crear una partícula
particula = Particula(posicion_inicial=0.0, velocidad_inicial=2.0)

# Definir aceleración constante
aceleracion = tf.constant(3.0, dtype=tf.float32)

# Actualizar la partícula en un intervalo de tiempo
tiempo_transcurrido = tf.constant(1.0, dtype=tf.float32)
particula.actualizar(tiempo_transcurrido, aceleracion)

# Imprimir la nueva posición y velocidad de la partícula
print(f"Posición de la partícula: {particula.posicion.numpy()} unidades de longitud")
print(f"Velocidad de la partícula: {particula.velocidad.numpy()} unidades de longitud por unidad de tiempo")