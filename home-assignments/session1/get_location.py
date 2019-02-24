import requests

get_location_description_url = 'https://ipinfo.io/{}/geo'


def get_location_coordinates(location):
    coordinates_arr = location.replace(' ', '').split(',')

    coordinates = {
        "latitude": coordinates_arr[0],
        "longitude": coordinates_arr[1]
    }

    return coordinates


def get_coordinates_by_ip_address(ip_address):
    url = get_location_description_url.format(ip_address)

    response = requests.get(url).json()

    location = response['loc']

    coordinates = get_location_coordinates(location)

    return coordinates
