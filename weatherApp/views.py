from django.shortcuts import render
from .models import City
from .forms import CityForm
import requests
def index(request):
    appId = 'f606492804b0b0ce2bbacda73575d621'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appId=' + appId
    if request.method == "POST":
        form=CityForm(request.POST)
        form.save()
    form = CityForm()
    cities = City.objects.all()
    all_cities=[]
    for city in cities:
        response = requests.get(url.format(city.name)).json()
        info= {
            'city':city.name,
            'temp':response['main']['temp'],
            'icon':response['weather'][0]['icon']
        }
        all_cities.append(info)
    context={'all_info':all_cities,'form':form}
    return render(request ,'weather/index.html',context)
