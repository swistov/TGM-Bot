import pyowm
from aiohttp_socks.errors import SocksError, SocksConnectionError
from config import OPENWEATHERMAP_KEY, OPENWEATHERMAP_ID_CITY

owm = pyowm.OWM(OPENWEATHERMAP_KEY, language='ru')
obs = owm.weather_at_id(OPENWEATHERMAP_ID_CITY)
try:
    weather_now = obs.get_weather()
except SocksError as e:
    print(f'Ошибка сокета: {e}')
except SocksConnectionError:
    print('Ошибка подключения')
