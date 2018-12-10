import json
import urllib.request


class Accu(object):
    def __init__(self):
        pass

    def api_connect(self, key, id):
        try:
            url = f'http://dataservice.accuweather.com/currentconditions/v1/{id}?' \
                f'apikey={key}&details=true&language=ru'
        except:
            return 'Ошибка в API'

        try:
            with urllib.request.urlopen(url) as url:
                data = json.loads(url.read().decode())
        except urllib.error.HTTPError as httpe:
            return httpe

        return data

    def weather_now(self, accu_key, accu_id):
        # print(json.dumps(data, indent=4, sort_keys=True))
        data = self.api_connect(accu_key, accu_id)

        if type(data) == urllib.error.HTTPError:
            return data

        return f"Погода на: {''.join(data[0]['LocalObservationDateTime'].split('T')[1].split('+')[0])}" \
            f" {'-'.join(data[0]['LocalObservationDateTime'].split('T')[0].split('-')[::-1])}\n" \
            f"За окном: {data[0]['WeatherText']}\n" \
            f"Температура: {data[0]['Temperature']['Metric']['Value']} ℃\n" \
            f"По ощущению: {data[0]['RealFeelTemperature']['Metric']['Value']} ℃\n" \
            f"Влажность: {data[0]['RelativeHumidity']}%\n" \
            f"Облачность: {data[0]['CloudCover']}%\n" \
            f"Скорость ветра: {data[0]['Wind']['Speed']['Metric']['Value']} км/ч\n" \
            f"Давление: {data[0]['Pressure']['Metric']['Value'] // 1.333} мм. рт. ст."

    def weather_today(self):
        return 'На данный момент сервис не доступен'

    def weather_tomorrow(self):
        return 'На данный момент сервис не доступен'
