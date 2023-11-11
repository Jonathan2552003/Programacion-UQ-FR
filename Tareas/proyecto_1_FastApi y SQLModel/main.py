#Archivo principal donde se arranca la aplicacion 

import uvicorn #Es el servidor de la aplicacion (Nos permite abrir la aplicacion en el navegador)
from fastapi import FastAPI, Depends, HTTPException, Path, status
from datetime import datetime #Nos permite trabajar con fechas
from data_base import engine
from sqlmodel import SQLModel
from sqlmodel import Session
from models import Parameter,Result, ImageResult
from sqlmodel.sql.expression import select #Nos permite hacer consultas en las bases de datos
from matplotlib import pyplot as plt
from schema import ParameterRequest
from common import calcular_intensidad_por_puntos



# app = FastAPI: es una clase, estamos creando un objeto de la clase FastApp, nos permite crear una rutas (links)
app=FastAPI() 
SQLModel.metadata.create_all(engine) #Paea conectarnos a la bse de datos 

#El get_sesio: es para iniciar secion en la base de datos y nos permita hacer modificaciones en ella
def get_session():
    with Session(engine) as session:
        yield session

#AHORA VAMOS A CREAR LAS RUTAS
# Ruta para obtener parámetros
@app.get("/", response_model=list[Parameter])
#db--> es database
#Session = Depends(get_session)---> Abre una sesion en la base de datos para poder operar en ella
#db.exect(selec(parameter)).all()
    #Donde:
        #exec es para elecutar una instruccion
        #select(parameter)---->Estamos seleccionar parametros y el .all se usa para que seleccione todos los parametros de la tabala parameter

def mostrar_todos_los_parametros(db: Session = Depends(get_session)): #sesion es la que nos permite hacer operaciones en la base de datos
    parameters = db.exec(select(Parameter)).all() #.exec es para elecutar una instruccion

    return parameters

# .get---> Para obtener informacion
@app.get("/{parameter_id}", response_model=Parameter, status_code=status.HTTP_200_OK)
#async, ejecuta la funcion en paralelo, para que no atasque la aplicacion  (ESTUDIAR FUNCIONES ASINCRONAS)
#Path---> Nos pone como las "condiciones" para que el parameter id sea mayor que cero
#Session = Depends(get_session)---> Abre una sesion en la base de datos para poder operar en ella
def leer_parametros_por_id(parameter_id: int = Path(..., gt=0), db: Session = Depends(get_session)):
    parameter = db.get(Parameter, parameter_id)
    if parameter:
        return parameter
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Parámetro no encontrado")
    

#ENVIAR INFORMACION
# Ruta para crear un nuevo parámetro
# el .post--->Crea informacion, crear informacion en base de datos(Como el ejemplo de crear un libro)
#response_model=list[dict]---> reponse_model es lo que vamos a recibir del metodo(en este caso una lista de diccionarios)
#satatus_code = satatus.HTTP_201_CREATER----> El mensaje que nos va a enviar si esta bien la informacion
@app.post("/parameter", response_model=list[dict], status_code=status.HTTP_201_CREATED)
#request: ParameterRequest-----> El ParameterRequest es una validacion de datos(Ejemeplo caundo nos sale rojito al meter una contraseña que no es en gmail))
#Session = Depends(get_session)--->Depend: es una inyeccion de dependencias(darle funcionalidad al get_session)---->y el get_session es para iniciar la sesion(lo estamos llamando al de arriba)
def crear_experimento(request: ParameterRequest, db: Session = Depends(get_session)):
    #El request lo que hace es recibir los parametros al darle ejecutar y lo convertimos en un parameter
    #con el, dic()--->Convierte los elementos ingreados de request a los atributos de la case
    parameter = Parameter(**request.dict()) #Son los datos que le envio a la app
    #Convertimos los json en algo que conocemos, en parameter
    
    #Retornamos las dos variables de la funcion que tenemos en common
    x_puntos, intensidad = calcular_intensidad_por_puntos(parameter.distanceGrids, parameter.distanceScreen,parameter.lambda_,parameter.NumberPoints)

    # plt.plot---> Realiza una grafica del valor de intensidad en el punto x(grafica x,y)
    plt.plot(x_puntos, intensidad)
    # .xlaber---> Son los nombres de los ejes
    plt.xlabel("Posicion en la pantalla (Metros)")
    plt.ylabel("Luminosidad de intensidad")
    #plt.title---> Es el titulo de la grafica
    plt.title("Patrón de interferencia de doble rendija")

    # datatime.utcnow---->Me crea la fecha en el formato de python
    nueva_fecha = datetime.utcnow() # utcnow()---> Esto es lo que permite crear la fecha actual}
    #Luego creamos una imagen por cada vez que creamos un parametro (cada fecha)
    nueva_imagen = nueva_fecha.strftime("%Y-%m-%d_%H-%M-%S") + ".png"   #strftime---->Es para indicarle ene que formatoo va a entrar la fecha

    # Construccion de la URL (link) del archivo
    direccion_del_archivo = f"C:/Users/HP/OneDrive - uqvirtual.edu.co/Escritorio/progra/Proyectos/proyecto_1/image/{nueva_imagen}"

    # Guardar las graficas en el disco local
    plt.savefig(direccion_del_archivo)
    lista_puntos_intensidad = [{"img": direccion_del_archivo}]

    # add()----> Añade el parametro a la base de datos
    db.add(parameter)

    #Vamos a agregar clave, valor de cada punto (x_punto, intensidad)
    #lista_puntos_intensidad = [(x_punto, intensidad)]
    for i in range(0, len(x_puntos)):
        lista_puntos_intensidad.append({"X": x_puntos[i], "I": intensidad[i]})
        nuevo_resultado = Result(intensity=intensidad[i], PointX=x_puntos[i], parameter=parameter)
        db.add(nuevo_resultado)

    # Despues de haber creado todos los puntos y toda la intensidad crea una nueva imagen con esos puntos
    nueva_imagen = ImageResult(urlImagen=direccion_del_archivo, parameter=parameter)
    db.add(nueva_imagen) #Agrega los cambios

    # Ahora guardamos los cambios y cerramos la conexion
    db.commit() #Guardar cambios
    db.close() #Cerrar coneccion con base de datos

    # Esta es para limpiar la grafica 
    plt.clf()
    return lista_puntos_intensidad

#El .get es para obtener informacion de los resultados
@app.get("/results/", response_model=list[Result], status_code=status.HTTP_200_OK)
def mostrar_todos_los_resultados_de_los_puntos(db: Session = Depends(get_session)):
    results = db.query(Result).all()
    db.close()
    return results


# Ruta para obtener un resultado por ID
#{result_id}---> Es un parametro para obtener el resultado con el identificador (if)
#response_model----> lo que se recibe del modelo
@app.get("/results/{result_id}", response_model=Result, status_code=status.HTTP_200_OK)
def leer_resultados_por_id(result_id: int = Path(..., gt=0), db: Session = Depends(get_session)): #Path(..., gt=0)----> Los puntos dicen que el id es obligatorio
    result = db.get(Result, result_id)
    if result:
        return result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resultado no encontrado")
##NOTA: Una inyeccionde dependencia es darle a una clase o una funcion o una funcionalidad que viene de otras clases(esta se da por parte de SQL model en este ejemplo)

# Ruta para obtener resultados por ID de parámetro
#/results/parameter/ -----> de result que obtenga la informacion relacionado con la tabla parameter (Eso es la URL)
@app.get("/results/parameter/{parameter_id}", response_model=list[Result], status_code=status.HTTP_200_OK)
def Leer_resultados_por_parametro_id(parameter_id: int = Path(..., gt=0), db: Session = Depends(get_session)): #En el db se pueden hacer consultas, agregar datos, eliminar infor, gracias al Depends(get_session), pero no porque es una base de datos sino porque se conecta a la base de datos
    #.filtrer(Result.parameter_id==parameter_id)----> Esto me va a filtrar los datos de result con el mismo id
    # .all()---> Este es para que me muestre todos los que cumplan con la condicion anterior
    results = db.query(Result).filter(Result.parameter_id == parameter_id).all() #Esto terminaria siendo una lista de resultados
        #query---->Realizar una colsulta en la base de datos
    if results:
        return results
    else:
        #Sino restorne el error, no encontro que esl 404
        #rise---->Esto se usa para demostrar un error(Es un return para errores)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No se encontraron resultados para este parámetro") #Sale un Json con esta informacion extra al error 404


# Ruta para obtener todas las imágenes de resultados
#Aqui la /images/----> No recibe parametros porque no vamos a filtrar, sino que me va a mostrar todas la informacion de la tabla image/results (Imagenes en este caso)
#response_model=list[ImageResult]-----> Aqui nos entrega las URL de donde se guardan las imagenes, pero no nos muestra las imagenes
@app.get("/images/", response_model=list[ImageResult], status_code=status.HTTP_200_OK)
def mostrar_imagenes(db: Session = Depends(get_session)):
    images = db.query(ImageResult).all() #Aqui me muestra la imagen, como tenemos el .all() nos muestra todas las imagenes

    if images:
        return images
    else: 
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron imagenes")
    



# Ruta para obtener una imagen de resultado por ID
#{image_id}---->Nos va a entregar una id de la imagen
@app.get("/images/{image_id}", response_model=ImageResult, status_code=status.HTTP_200_OK)
def mostrar_imagenes_por_id(image_id: int = Path(..., gt=0), db: Session = Depends(get_session)):
    image = db.get(ImageResult, image_id) #Obtener una image_result por id donde image_id sea == ImageResult.id
    if image:
        return image
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Imagen no encontrada")

#El __name__ == "__main__" permite tener la aplicacion abierta
if __name__ == "__main__":

    #Ahora iniciamos el servidor para aplicion FastApi con uvicorn.run("", port=9004, reload=True. Uvicor.run nos crea un puerto
        #"main:app": main--->archivo principal de la aplicacion y app---> Es la instancia de fastApi (linea 8)
        #-----> Port=9004:(nos abre un puerto)   ----->reload=True: Para que la pagina actualice en la pagina, los cambios echos en el codigo
    uvicorn.run("main:app", port=9056, reload=True) #Crea la ruta



