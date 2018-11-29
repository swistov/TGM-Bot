import json
import time
import urllib.request
from config import ACCUWEATHER_ID, ACCUWEATHER_KEY


def get_weather(api, location_id):
    url = f'http://dataservice.accuweather.com/currentconditions/v1/{location_id}?apikey={api}&details=true&language=ru'
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
    # print(json.dumps(data, indent=4, sort_keys=True))
    print(data[0]['WeatherText'])
    return (data[0]['Temperature']['Imperial']['Value'],
            data[0]['RelativeHumidity'],
            data[0]['Wind']['Direction']['Degrees'],
            data[0]['Wind']['Speed']['Imperial']['Value'],
            data[0]['UVIndex'],
            data[0]['CloudCover'],
            data[0]['Pressure']['Metric']['Value'],
            data[0]['Precip1hr']['Metric']['Value'],
            data)


timestamp = time.time()

temperature, humidity, wind_bearing, wind_speed, uv_index, cloud_cover, pressure, precipitation, raw \
    = get_weather(ACCUWEATHER_KEY, ACCUWEATHER_ID)


