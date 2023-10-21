from pathlib import Path

from get_coordinates import get_coordinates
from weather_api_service import get_weather
from weather_formatter import format_weather
from exceptions import CantGetCoordinates, ApiServiceError
from history import save_weather, JSONWeatherStorage

def main():
    try:
        coordinates = get_coordinates()
    except CantGetCoordinates:
        print("Не удалось получить координаты")
        exit(1)
    try:
        weather = get_weather(coordinates)
    except ApiServiceError:
        print(f"Не удалось получить погоду по координатам {coordinates}")
        exit(1)
    print(format_weather(weather))

    save_weather(
        weather,
        JSONWeatherStorage(Path.cwd() / "history.json")
    )

if __name__ == "__main__":
    main()
