import numpy as np 
#x: es el punto de la pantalla donde se va a evaluar
#d: Es la distancia entre las rejiLLAS
#D: Es la distancia que hay de las rejillas a la pantalla 
#lamda: Es de formula, longitud de onda de la luz incedida
def calcular_intensidad(x, d, D, lamda): #Lo dejamos como lamda porque sino nos lo coge como un apalabra definidad de pythn

    #Vamos a encontrar un theta
    teta = np.arcsin(x/D)

    #Intensidad maxima
    I0 = 1

    # Intensidad
    I = I0 * (np.cos(2 * np.pi * d * np.sin(teta) / lamda)) ** 2
    return I

#Calcular intensidad por puntos
     #Es decir le vamos a entregar todos los puntos, o mas bien, todos los x
def calcular_intensidad_por_puntos(d,D, lamda, N): #N va a ser el numero de puntos que va a tener la pantalla

    #Con linspace creamos un vector de puntos con un numero n de puntos
        #El 0.5 es porque queremos la mitad de la distancia entre la regilla y la pantalla pero podemos colocar cualquiero valor (va de -0.5D hasta 0.5D)
    x_puntos = np.linspace(-0.5*D, 0.5*D, N)

    #Vector donde vamos a guardar los valores de intensidad
    intensidad = []

    for x_1 in x_puntos:
        
        I = calcular_intensidad(x_1,d,D,lamda)

        if I<0:
            I=0
        intensidad.append(I)
    return x_puntos, intensidad


