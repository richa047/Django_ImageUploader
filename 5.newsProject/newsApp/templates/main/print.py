create project
create app
in settings.py declare the app
create urls.py in app.
create static folder(image) under app.
create template under app for .html files
install news api so that u can use it
install pillow  so that u can use it.
proj name=NewsProject(main folder)
app name=newsApp
newsProject(inner proj folder)

https://www.youtube.com/watch?v=Mh69OwfeDkA

----------------------------------------------------------
structure of proj

newsApp(application folder)
1.migrations
2.static/images
3.templates/main/index.html
4.admin.py
5.model.py
6.urls.py
7.views.py

newsProject(inner proj folder)
settings.py
urls.py
---------------------------------------------------------
index.html
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootswatch/4.5.3/cyborg/bootstrap.min.css"
    integrity="sha512-QzwqVdCfEIUhmovYlJ/ET11Uh4MLuvEpwVpTVTRhChwzgfkrQH9BMcDvgwFpi5fMUGVLJAPsEXJVHuODuhmctg=="
    crossorigin="anonymous" />
  <title>News App</title>
</head>

<div class="navbar fixed-top navbar-dark bg-dark">
  <div class="container">
    <h4 style="color:rgb(255, 255, 255)">News App <h4 style="color: rgb(154, 255, 0);">New's Today...</h4>
    </h4>
    <img src="{% static 'images/dj.png' %}" class="image" style="width:90px; ">
  </div>
</div>

<!-- Card for header -->
<div class="jumbotron" style="text-align: center; margin-top:40px">
  <h2>Latest News using<a href="https://newsapi.org" style="text-decoration: none" ;> news API</a></h2>
  <img src="{% static 'images/news.png' %}" class="image" style="width:150px; margin-bottom:-50px; ">
</div>

<!-- Main -->
<div class="container">
  {% for hl, des, img in mylist %}

  <div class="card border-primary mb-3">
    <img src="{{ img }}" alt="image">
  </div>
  <div class="card border-primary mb-3">
    <h4><span class="badge badge-primary">Headline:</span></h4>
    <h5>{{ hl }}{{ value|linebreaks }}</h5>
    <h4> <span class="badge badge-success">Description:</span></h4>
    <h5>{{ des }}{{ value|linebreaks }}</h5>
  </div>
  {% endfor %}

  </body>

</html>
----------------------------
urls.py(newsApp)
from django.urls import path
from . import views

urlpatterns =[
    path('',views.index),
]
-------------------------------------------------------------
views.py
from django.shortcuts import render
from newsapi import NewsApiClient
# Create your views here.


def index(request):
    newsApi = NewsApiClient(api_key='17af1b67e52a44fa85a60b1f052df07d')
    headLines = newsApi.get_top_headlines(sources='ign, cnn')
    articles = headLines['articles']
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        
        mylist = zip(news, desc, img)

    return render(request, "main/index.html", context={"mylist": mylist})
----------------------------------------------------------------------------
newsProject
settings.py

import os
from pathlib import Path

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
    'newsApp',
]

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
    }


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
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

---------------------------------------------------------------------------
urls.py(newsProject)
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('newsApp.urls')),
] + static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
------------------------------------------------------------------------
