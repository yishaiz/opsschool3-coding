from get_my_ip import get_public_ip_address
from get_location import get_coordinates_by_ip_address
from get_weather import get_weather_by_coordinates, get_weather_by_city
from file_writer import write_result_to_file
from get_cities import get_cities_list


def get_current_location_weather():
    result_file_name = "weather-result.json"

    my_ip = get_public_ip_address()
    coordinates = get_coordinates_by_ip_address(my_ip)
    weather = get_weather_by_coordinates(coordinates)
    write_result_to_file(result_file_name, weather)


def display_weather_for_cities_list(cities):
    for city in cities:
        weather_for_city = get_weather_by_city(city['country'], city['name'])

        print("The weather in {}, {} is {} degrees.".format(
            city['name'],
            city['country-name'],
            weather_for_city
        ))


def print_cities_weather():
    cities = get_cities_list()
    display_weather_for_cities_list(cities)


def main():
    try:
        get_current_location_weather()

        print_cities_weather()

    except Exception as ex:
        print("There is an error. {0}".format(ex))


if __name__ == '__main__':
    main()
