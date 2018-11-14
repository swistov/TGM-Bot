import pyowm
from config import OPENWEATHERMAP_KEY, OPENWEATHERMAP_ID_CITY

owm = pyowm.OWM(OPENWEATHERMAP_KEY, language='ru')
obs = owm.weather_at_id(OPENWEATHERMAP_ID_CITY)
weather_now = obs.get_weather()
