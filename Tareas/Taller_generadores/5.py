#Manipulacion de datos
#lee un archivo de texto con una lista de numeros separados por comas.
#Escribe un generador que lea estos numeros y produzca su suma acumulativa.
#Sin usar librerias

#Una vez que importamos el archivo procedemos a abrirlo

with open("Talleres programacion/Generadores_gestion_datos/Manipulacion de datos numericos.txt") as archivo:
    leer = archivo.read()
    
    for numero in leer:
        lista = leer.split(",") #Aqui estamos pasando la "Cadena" de texto a una lista
        lista = [int(num) for num in lista] #Aqui convierte los elementos que python los esta tomando como cadena a numeros enteros
        suma = sum(lista) #Sumammos los elementos de la lista

print()
print("Este es el contenido del archivo: ", leer)
print()
print("El resultado de la suma de los elementos del archivo de texto es:", suma)
print()
