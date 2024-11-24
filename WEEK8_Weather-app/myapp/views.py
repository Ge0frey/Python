import requests
from django.shortcuts import render, redirect
from django.conf import settings
from .models import City
from .forms import CityForm

def weather_view(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('weather')
    
    form = CityForm()
    cities = City.objects.all()
    weather_data = []

    for city in cities:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city.name},{city.country_code}&units=metric&appid={settings.OPENWEATHER_API_KEY}'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            city_weather = {
                'city': city.name,
                'temperature': round(data['main']['temp']),
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            }
            weather_data.append(city_weather)

    context = {
        'weather_data': weather_data,
        'form': form
    }
    return render(request, 'weather.html', context) 