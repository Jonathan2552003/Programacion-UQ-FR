#Tarea 

class Fuerza:
    def __init__(self, opcion):
        self.opcion = opcion
        if opcion == 1:
            self.masa = float(input("Ingrese la masa de la partícula en kg: "))
            self.fuerza = float(input("Ingrese la fuerza aplicada en N: "))
        elif opcion == 2:
            self.f1 = float(input("Ingrese la magnitud de la primera fuerza: "))
            self.f2 = float(input("Ingrese la magnitud de la segunda fuerza: "))
    
    def calcular_aceleracion(self):
        if self.opcion == 1:
            return self.fuerza / self.masa
        else:
            return None  # No se puede calcular la aceleración en este caso
    
    def calcular_ft(self):
        if self.opcion == 2:
            return self.f1 + self.f2
        else:
            return None  # No se puede calcular la fuerza total en este caso
    
    def calcular_velocidad(self, tiempo):
        aceleracion = self.calcular_aceleracion()
        if aceleracion is not None:
            return aceleracion * tiempo
        else:
            return None  # No se puede calcular la velocidad en este caso
    
    def __str__(self):
        if self.opcion == 1:
            return "Masa: " + str(self.masa) + " kg, Fuerza: " + str(self.fuerza) + " N"
        elif self.opcion == 2:
            return "Fuerza 1: " + str(self.f1) + " N, Fuerza 2: " + str(self.f2) + " N"
        else:
            return "Opción no válida"

opcion = int(input("¿Qué desea hacer?\n 1. Calcular aceleración\n 2. Sumar dos fuerzas\n"))
particula = Fuerza(opcion)

if opcion == 1:
    aceleracion = particula.calcular_aceleracion()
    if aceleracion is not None:
        print("Aceleración:", aceleracion)
    else:
        print("No se puede calcular la aceleración en esta opción.")
elif opcion == 2:
    fuerza_total = particula.calcular_ft()
    if fuerza_total is not None:
        print("La fuerza resultante es", fuerza_total)
    else:
        print("No se puede calcular la fuerza total en esta opción.")
else:
    print("Opción no válida")
