from decouple import config

OPENWEATHER_API_KEY = config("SECRET_KEY")
  # Get this from OpenWeatherMap

INSTALLED_APPS = [
    # ...
    'myapp',
] 