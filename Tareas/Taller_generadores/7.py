#Procesamiento de texto
#Escribir una clase, debe recibir un txt largo y lo va a leer
#Genere una lista de tuplas de cada parrafo y su longitud
#Otro metodo que reciba un nunmero N y retorne los N parrafos mas largos

class ProcesadorDeTexto:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.parrafos = self.leer_archivo()

    def leer_archivo(self):
        try:
            with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:  # Especifica 'utf-8' como el conjunto de caracteres
                contenido = archivo.read()
                parrafos = contenido.split('\n')
                return parrafos
        except FileNotFoundError:
            print()
            print(f"El archivo {self.ruta_archivo} no se encontró.")
            return []

    # ... el resto del código sigue igual


    def generar_lista_de_tuplas(self):
        # Genera una lista de tuplas con cada párrafo y su longitud
        lista_de_tuplas = [(parrafo, len(parrafo)) for parrafo in self.parrafos]
        return lista_de_tuplas

    def parrafos_mas_largos(self, N):
        # Retorna los N párrafos más largos
        lista_de_tuplas = self.generar_lista_de_tuplas()
        # Ordenamos la lista por longitud de párrafo en orden descendente
        lista_ordenada = sorted(lista_de_tuplas, key=lambda x: x[1], reverse=True)
        return lista_ordenada[:N]

# Ejemplo de uso:
ruta_del_archivo = "Talleres programacion/Generadores_gestion_datos/EL CORAZON DELATOR .txt"  # Reemplaza con la ruta de tu archivo
procesador = ProcesadorDeTexto(ruta_del_archivo)

# Generar la lista de tuplas con párrafos y longitudes
lista_de_tuplas = procesador.generar_lista_de_tuplas()

# Obtener los N párrafos más largos (por ejemplo, los 5 más largos)
N = 5
parrafos_largos = procesador.parrafos_mas_largos(N)

