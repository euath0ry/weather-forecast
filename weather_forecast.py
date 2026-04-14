from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse
import uvicorn
from db import get_all_weather
from db import weather_create
from db import weather_delete
from db import weather_name_search
import requests



app = FastAPI(
    title="Todo API",
    description="Простой API для задач",
    version="1.0.0"
)

@app.get("/")
def root():
    """Главная страница"""
    return {"message": "Добро пожаловать в API погоды!", 
            "docs": "Перейдите на /docs для документации"}

@app.get("/weather")
def get_all():
    return get_all_weather()

@app.post("/weather")
def create():
    return weather_create()

@app.delete("/weather")
def delete():
    return weather_delete()


@app.get("/search")
def search(name:str):
    
    api_link = f"https://api.weatherapi.com/v1/current.json?key=d09e269427a84aaebd4152802262603&q={name}"

    response = requests.get(api_link)
    data = response.json() 
    
    return data


        


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)