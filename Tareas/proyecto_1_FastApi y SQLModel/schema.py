#Pydantic es una libreria que nos pide hacer una verificacion de libreria de datos
from pydantic import BaseModel, Field

#Validar los datos de entrada: 
class ParameterRequest(BaseModel):
    lambda_: float = Field(gt=0)
    distanceGrids: float = Field(gt=0)
    distanceScreen: float = Field(gt=0)
    NumberPoints: int = Field(gt=0)
