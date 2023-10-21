from weather_api_service import Weather


def format_weather(weather: Weather) -> str:
    """Format weather data into string"""
    return (f"{weather.city}, температура {weather.temperature}°C, "
            f"{weather.weather_type.value}\n"
            f"Восход: {weather.sunrise.strftime('%H:%M')}\n"
            f"Закат: {weather.sunset.strftime('%H:%M')}\n"
            )

if __name__ == "__main__":
    from datetime import datetime
    from weather_api_service import WeatherType
    print(format_weather(Weather(
        temperature=25,
        weather_type=WeatherType.CLEAR,
        sunrise=datetime.fromisoformat("2023-10-25 07:00:00"),
        sunset=datetime.fromisoformat("2023-10-25 18:25:00"),
        city="Chelyabinsk"
    )))
