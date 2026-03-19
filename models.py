from pydantic import BaseModel 

class Weather(BaseModel):
    city: str
    temperature: float
    condition:str
    humidity:int