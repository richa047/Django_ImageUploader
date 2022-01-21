proj structure
-WEATHERPROJECT(outer proj folder)
-weatherApp(App)
   -migration/001_initial.py
   -static/css,image,js
   -templates/main/index.html
   -admin.py
   -models.py
   -urls.py
   -views.py
-weatherProject(inner proj folder )
   -settings.py
    -urls.py

--------------------------------------------------------
weatherApp(App) templates/main/index.html

index.html

<!DOCTYPE html>
<html lang="en">
{% load static %}

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootswatch/4.5.3/cerulean/bootstrap.min.css"
    integrity="sha512-dQLT/B7byn2LjN/DN4zeBKpwGV6qbidV0XiMRWQOL7TGrV7FkZFldkGG+DGMU+CQnMTcRZlUI7GMWt1j6akNew=="
    crossorigin="anonymous" />
  <title>Weather App </title>
</head>

<body>
  <div class="navbar navbar-expand-lg fixed-top navbar-dark bg-dark">
    <div class="container">
      <a href="../" class="navbar-brand">Weather App <span style="color: rgb(39, 117, 161);"> <strong> - Django
            Framework</strong>
        </span> </a>
      <a href="https://openweathermap.org" class="navbar-tech">OpenWeather - Get Your API</a>
    </div>
  </div>

  <br /><br /> <br>
  <div id="jumbotron" class="jumbotron" style="text-align: center; margin-top:-50px">
    <h1 class="display-5">Weather Desktop App </h1>
    <h5>Using Python Language and Django Framework</h5>

    <img src="{% static 'images/weather.png' %}" class="image" style="width:100px; margin-bottom:-50px; ">
  </div>

  <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
    <form method="post" class="col-md"">
      {% csrf_token %}
      <div class=" input-group">

      <input type="text" class="form-control" name="city" placeholder="Choose Your City ...">
      <div class="input-group-btn">
        <button type="submit" class="btn btn-primary">Search</button>
      </div>
      </div>
      <form>
  </nav>
  <br> <br>
  <div class="row">
    {% if country_code and coordinate and temp and pressure and humidity %}
    <div class="col d-flex justify-content-center" ">
      <div class=" card text-white bg-light mb-6">
      <div class=" card-body">
        <h4><span class="badge badge-primary">Country Code :</span> {{country_code}}</h4>
        <h4><span class="badge badge-primary">Coordinates [X,Y] :</span> {{coordinate}}</h4>
        <h4><span class="badge badge-primary">Temperature in Celsius :</span> {{temp}}</h4>
        <h4><span class="badge badge-primary">Pressure :</span> {{pressure}} </h4>
        <h4><span class="badge badge-primary">Humidity : </span> {{humidity}}</h4>
        <h4><span class="badge badge-primary">Forecast : </span> {{main}} <img
            src="http://openweathermap.org/img/w/{{icon}}.png" alt="Image" style="width:70px"></h4>
        <h4><span class="badge badge-primary">Description : </span> {{description}}</h4>
      </div>
      {% endif %}
    </div>
</body>

</html>
------------------------------
weatherApp( urls.py)

from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
]

------------------
weatherApp(views.py)

import urllib.request
import json
from django.shortcuts import render


def index(request):

    if request.method == 'POST':
        city = request.POST['city']

        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                        city + '&units=metric&appid=70e1505475a310764d9a7868b2d180cc').read()
        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}
    return render(request, "main/index.html", data)

---------------------------------------------
weatherProject(inner folder)
1.settings.py

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'weatherApp'
]


ROOT_URLCONF = 'weatherProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'weatherProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL ='/images/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    ---------------------------------------------------------

    urls.py(weatherProject)
    
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('weatherApp.urls'))
] +static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
