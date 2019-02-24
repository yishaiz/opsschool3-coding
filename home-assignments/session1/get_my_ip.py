import requests

get_my_ip_url = 'http://ip.42.pl/raw'


def get_public_ip_address():
    my_ip = requests.get(get_my_ip_url).text
    return my_ip
