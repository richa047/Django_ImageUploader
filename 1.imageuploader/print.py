https://www.youtube.com/watch?v=5TwCVOyYR4U

1.Create project imageuploader
2.Create app in project
3.In setting.py of imageuploader (inner proj) install app name and declare Dir[].
4.create template under myapp->template->myapp-home.html
5.create model
6.save migration and then migrate model
7.create superuser
8.open 127.0.0.1:8000/admin
9.create media folder by declaring it.
10.now write code in home.html
11.In myapp view.py function  write code
12.in myapp urls.py write the path.
--------------------------------------------
--------------------------------------------
setting.py(imageuploader main folder)
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0aasvnoig09t9gladbz@zs58e4yh0sui(78=#znrv&of8aam6n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'imageuploader.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': ['templates'],
        'DIRS':   [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'imageuploader.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL ='/media/' #to get output in admin panel
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

------------------------------------------------------------------------

url.py(imageuploader main folder)

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static  import static
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

----------------------------------------------------------------------------
media/myimage(for images)
----------------------------------------------------------------------------
myapp-(under applcation folder you have these files & folders)

migrations
templates/myapp/home.html
admin.py
forms.py
models.py
views.py

----------------------------------------------------------------------------

home.html
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <title>Image uploader</title>
  </head>
  <body>
  <div class = "container"> 
  <div class ="py-5 text-center bg-secondary text-white">
    <h1 class "mb-3"> DJ Image Uploader</h1>
     <form action ="" method ="post" enctype = "multipart/form-data"><!--enctype  att is used to work with images-->
      {% csrf_token %}
      {{form}}
      <input type ="submit" class= "btn btn-danger" value = "Upload">
    </form>
  </div>
   <div class="row">
   {% for x in img %}
    <div class= "col-sm-4">
    <div class ="card m-2">
       <img src ="{{x.photo.url}}" alt ="" class= "card-img-top" height ="200px">
    </div>
  </div>
   {%endfor%}
</div>

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

   
  </body>
</html>
-----------------------------------------------------------------------------------
views.py

from django.shortcuts import render
from .forms import ImageForm
from .models import Image
# Create your views here.

def home(request):
 if request.method == "POST":
  form = ImageForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
 form = ImageForm()
 img = Image.objects.all() # to show img on the screen
 return render(request, 'myapp/home.html', {'img':img, 'form':form})

------------------------------------
migration.py
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='myimage')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
----------------------------------------------------
admin.py
from django.contrib import admin
from .models import Image


# Register your models here.

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','photo','date']
---------------------------
forms.py
from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        labels ={ 'photo' :''}

-------------------------------------------------------
models.py
from django.db import models

# Create your models here.
class Image(models.Model):
    photo = models.ImageField(upload_to = "myimage")
    date = models.DateTimeField(auto_now_add=True)
