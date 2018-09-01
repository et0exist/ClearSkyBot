import requests

with open('weather_API_key') as key:
    api_key = key.read()
base_url = 'https://api.weather.yandex.ru/v1/'
url = base_url + 'forecast'


def req(lat, lon):
    weather = requests.get(
        url,
        params={
            'lat': lat,
            'lon': lon,
        },
        headers={
            'X-Yandex-API-Key': api_key,
        }
    )
    return weather.json()
