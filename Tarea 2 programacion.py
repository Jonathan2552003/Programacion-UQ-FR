class ConversionUnidades:
    def __init__(self, longitud):
        self.l = longitud

    def calcular_longitud(self):
        respuesta = self.l * 100  # De metros a centímetros
        return respuesta

# Solicitar al usuario los datos
longitud = float(input("Ingrese la longitud en metros: "))

# Crear instancia de la clase ConversionUnidades
conversion = ConversionUnidades(longitud)

# Realizar cálculos
longitud_calculada = conversion.calcular_longitud()
print("La longitud en centímetros es:", longitud_calculada)
