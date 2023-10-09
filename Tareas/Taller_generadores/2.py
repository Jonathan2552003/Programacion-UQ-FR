import pandas as pd

df = pd.read_csv("Talleres programacion/Generadores_gestion_datos/Calificaciones_vecindad.csv", sep=";")

#Ahora vamos a calcular el promedio de edad
promedio_de_edad = df["EDAD"].mean()

#Ahora vamos a por el promedio de notas
promedio_de_notas = df["CALIFICIACIONES"].mean()

#Ahora vamos por a seleccinar quieres perdieron la asignatuda
perdieron = df[df["CALIFICIACIONES"]<30]

#Ahora vamos a sacar el 10% mejor
#Para esto primero ordenamos a los estudiantes de mayor a menor
datos_ordenados = df.sort_values(by="CALIFICIACIONES", ascending=False)
num_estudiantes = len(datos_ordenados)
num_10_por_ciento = int(0.10*num_estudiantes)

#Ahora escogemos a los estudiantes que estan en el 10% mejor
mejores_estudiantes = datos_ordenados.head(num_10_por_ciento)



print(df)
print()
print(promedio_de_edad)
print()
print(promedio_de_notas)
print()
print(perdieron)
print()
print(mejores_estudiantes) #NOTA: Solo funciona la pregunta del 10% si este poercentaje de estudiantes es un numero entero
#En resumen, si el numero de estudiantes no es multiplo del 10 no funciona el 10%

