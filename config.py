import os


USE_ROUNDED_COORDS = True
OPENWEATHER_API: str = str(os.getenv('OpenWeather_API'))
OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    + "lat={latitude}&lon={longitude}&"
    + "appid=" + OPENWEATHER_API + "&lang=ru&"
    + "units=metric"
    )
IPINFO_API = os.getenv('ipinfo_api')
