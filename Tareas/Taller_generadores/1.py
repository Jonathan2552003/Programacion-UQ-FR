#Escribir la susecion de fibonacci usando un generador y luego comprension de generadores para obtener los numeros pares de esta
#La secuencia de binoacci es la suma de los dos anteriores numeros
#n = (n-1)+(n-2)
def fibonacci_generador(n):
    a, b= 0, 1  #Definimos los primeros numeros de la secuencia
    while a <= n: #Iniciamos el ciclo 
        yield a  #Este es nuestro generador
        a, b =b, a+b #En este punto actualizamos la variable a como b
         #Y aqui el b como a 
         #Lo anterior lo hicimos para que a pase a ser el n-2 y el b n-1, asi obtenemos la suma de los dos anteriores numeros
w = 1000000
fibonacci = fibonacci_generador(w)

for numero in fibonacci: #Como es una funcion perezosa usamos for para obligar a que nos de los valores
    print(numero) #Por ultimo nos imprime el numero







