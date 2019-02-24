import requests

api_key = 'b6907d289e10d714a6e88b30761fae22'

get_weather_by_location_url = 'https://openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}'
get_weather_by_city_url = 'https://openweathermap.org/data/2.5/weather?q={},{}&appid={}'


def get_weather_by_coordinates(coordinates):
    url = get_weather_by_location_url.format(
        coordinates['latitude'],
        coordinates['longitude'],
        api_key
    )

    weather = requests.get(url).text
    return weather


def get_weather_by_city(country, city):
    url = get_weather_by_city_url.format(
        city,
        country,
        api_key
    )

    weather = requests.get(url).json()

    degree = weather['main']['temp']
    return degree
