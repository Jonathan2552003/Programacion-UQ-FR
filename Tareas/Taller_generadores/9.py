#Manipulacoin de datos Json
#Lee un archivo Json que contiene informacion de productos(nombre, precio,cantidad en stok)
#Escribe un generador que produzca solo los productos que tienen un precio superior al umbral

import json

def filtrar_productos_por_precio(archivo_json, umbral):
    with open(archivo_json) as frutas:
        datos_frutas = json.load(frutas)
        for producto in datos_frutas:
            if producto.get('precio_por_unidad') > umbral:
                yield producto


w = "Talleres programacion/Generadores_gestion_datos/frutas.json" 
x = 3500  # Aqui definiremos el umbral de precio

print(f"Productos con un precio superior a {x}:")
for producto in filtrar_productos_por_precio(w, x):
    print(f"Nombre: {producto['Nombre']}")  
    print(f"Precio por unidad: {producto['precio_por_unidad']}") 
    if 'Cantidad en stock' in producto:
        print(f"Cantidad en stock: {producto['Cantidad en stock']}")
    else:
        print("Cantidad en stock: No especificada")
    print()
