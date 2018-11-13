import pyowm
from config import OPENWEATHERMAP_KEY, OPENWEATHERMAP_ID_CITY

owm = pyowm.OWM(OPENWEATHERMAP_KEY)
observation = owm.weather_at_id(OPENWEATHERMAP_ID_CITY)
w = observation.get_weather()

# print(w.get_temperature('celsius')['temp'])
