from datetime import datetime
from sqlmodel import Field, SQLModel, Relationship
from typing import List

#Cada clase que vamos a crear va a ser una tabla
    #SQL MODEL:
        #Nos crea las tablas
            #en este caso las calses son las tablas, cada clase representa una tabla
        #Nos permite definir las columnas de las tablas
        #Nos permite definir los tipos de datos de las columnas
        #Nos permite definir las relaciones entre las tablas
        #Nos permite hacer validacion de datos
#
#
class ImageResult(SQLModel, table=True):
    id: int = Field(primary_key=True)
    urlImagen: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    parameter_id: int = Field(foreign_key="parameter.id") #Esta es la columna que permite la relacion entre las tablas (clave foranea)

#NO ES UNA COLUMNA, ES UNA RELACION CON LA TABLA PARAMETER
    parameter: "Parameter" = Relationship(back_populates="image_result") #Relacion de 1<---->1 con parameter

#SQLModel:Esta calse esta recibiendo toda la funcionalidad de SQLModel
#table = True: le indica a SQL model que tome esa clase como una tabla para la base de datos
class Parameter(SQLModel, table=True):
    id: int = Field(primary_key=True)
    lambda_: float
    distanceGrids: float
    distanceScreen: float
    NumberPoints: int
    created_at: datetime = Field(default_factory=datetime.utcnow)
#

#NO SON COLUMNAS EMPIEZAN A SER OPERACIONES DESDE python CON SQLmodel QUE SE HACEN ENTRE LAS TABLAS (Todo lo que tenga relation)
    # Define una relación uno a uno con ImageResult
    #back_populates = "paramter": 
    #Por cada parametro creado va a crear una umahen, eso es una relacion de uno a uno
    image_result: "ImageResult" = Relationship(back_populates="parameter") #Relacion 1<-->1 (uno a uno)

    # Define una relación uno a muchos con Result
    results: List["Result"] = Relationship(back_populates="parameter") #RELACION 1<--->MUCHOS
    ##results: List["Result"]--->Obtiene los resultados de un parametro


class Result(SQLModel, table=True):
    id: int = Field(primary_key=True) #Nos permite identificar cada tabla
    intensity: float 
    PointX: float
    created_at: datetime = Field(default_factory=datetime.utcnow)
    parameter_id: int = Field(foreign_key="parameter.id")  # Clave foránea es la que nos permite hacer las relaciones entre las tablas

    # Define una relación muchos a uno con Parameter
    parameter: "Parameter" = Relationship(back_populates="results")