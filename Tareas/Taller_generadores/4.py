#4. Exportacion de datos 
#Programa que generre una lista de diccionarios 
#cada diccionario representa informacion como nombre y salario y departamento
#Exportar todos los datos en una archivo Json

#Vamos a por ello. Lo vamos a hacer inspirado en los personajes de bob esponja para darle un toque divertido

#Lo primero que debemos hacer importar json

import json

#Ahora creamos una lista con la informacion de los empelados
#La informacion de los empleados estara representada en diccionarios

empleos_en_crustaeo_cascarudo = [{"Nombre":"Bob Esponja", "Salario" : 100000, "Departamento": "Cocina"}, 
                                 {"Nombre": "Calamardo", "Salario": 80000, "Departamento": "Caja"}, 
                                 {"Nombre": "Patricio estrella", "Salario":50000, "Departamento": "Meseros"}]

#Ahora exportamos los datos en un archivo json
with open("crustaseo.json", "w") as archivos_json:
    json.dump(empleos_en_crustaeo_cascarudo, archivos_json)
