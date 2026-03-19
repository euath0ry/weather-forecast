from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse
import uvicorn
from db import get_all_weather
from db import weather_create
from db import weather_delete
from db import weather_name_search




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
def search():
    return weather_name_search()

        


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 