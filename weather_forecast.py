from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse
import uvicorn
from models import Weather



weather_db = [
    Weather(
        city="Москва",
        temperature=20.5,
        condition="облачно",
        humidity=65
    ),
    Weather(
        city="Санкт-Петербург", 
        temperature=18.0,
        condition="дождливо",
        humidity=80
    )
] 



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
def get_all_weather():
    return weather_db

@app.post("/weather")
def weather_create(weather:Weather):
    weather_db.append(weather)

@app.delete("/weather")
def weather_delete(weather:Weather):
    weather_db.remove(weather)

@app.get("/search")
def weather_name_search(city:str):
    for i in weather_db:
        if i.city.lower() == city.lower():
            return i
        



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 