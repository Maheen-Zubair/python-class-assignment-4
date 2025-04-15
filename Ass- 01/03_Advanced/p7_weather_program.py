import requests   #internet se data fetch krne keleye
from pprint import pprint   #for pretty print

API_KEY = "931551918dede09001c2a15e8581b111"

def weather_app():
 city = input("Enter the city name: ")
 base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_KEY + "&q=" + city
 weather_data = requests.get(base_url).json()
 pprint(weather_data)
weather_app()