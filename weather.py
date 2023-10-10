from coordinates import get_gps_coordinates
from weather_api_service import get_weather
from weather_formatter import format_weather


def main():
    coordinates = get_gps_coordinates()
    wheather = get_weather()
    print(format_weather(wheather))


if __name__ == "__main__":
    main()
