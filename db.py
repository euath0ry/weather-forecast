from models import Weather
from fastapi import FastAPI, HTTPException, Query
import requests







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

def get_all_weather():
    return weather_db

def weather_create(weather:Weather):
    weather_db.append(weather)

def weather_delete(weather:Weather):
    weather_db.remove(weather)

def weather_name_search(city:str):
    for i in weather_db:
        if i.city.lower() == city.lower():
            return i
    