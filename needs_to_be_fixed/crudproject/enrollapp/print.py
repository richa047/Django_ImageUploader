1.create project crudproject
2.create app
install app name in an settings .py of crudproject(inner folder)
3.create static folder under enrollapp
download bootstrap and extract the file css->bootstrap.min ,js-.bootstrap.min and store the 2 files in static/enrollapp/css & static/enrollapp/js(rest u can delete)
3.create static folder under enrollapp
4.create template  folder to add hyml file under enrollapp.
5.create base.html to display common things in page 
then design rest 2 pages and inherit template base.html in other templates(addandshow.html,updatestudent.html)
6.enrollapp->view.py to render html pages on calling up of function.
7.crudproj(innerfolder) urls.py { flow goes urls--->view---->htmlfile}
NOTE 2 methods to create form  -----form api(form,model,using model class table will get created and d) or modal form(model class and using that u can build form u dont need to write field seperately)
8.modal form method
create class(user) in models.py and register it in admin.pys{u need to register modal with admin.py so that u can see the table on admin panel}
create model,migration,migrate,superuser 
9.in enrollapp>admin.py register the model so that you can access the table created  by this model
10.create form.py in enrollapp. and create class StudentRegistration in it,
11.go to views.py import form and check for POST method or GET method.
12.go to addandshow .html

 BE part 
now storing data in database once u have entered the data in form
flow-url->view->.html file


Status of proj: **edit function not working video last 10 mins left to do bec of error.


https://www.youtube.com/watch?v=OPc_oMgjhpM


---------------------------
main proj- CRUDPROJECT

app-enrollap
 -migration/initial_001.py
 -static/images
 -templates/enrollapp/addandshow.html,base.html,updatestudent.html
 -admin.py
 -forms.py
 -views.py

inner proj folder crudproject
-setting.py
-urls.py
------------------------------
addandshow.html

{% extends 'enrollapp/base.html' %}
{% block content %}
<div class="row">
  <div class="col-sm-4">
<h4 class="text-center alert alert-info"> Add New student </h4>
<form action ="" method ="POST">
  {% csrf_token %}
   {{form.as_p}}
   <input type="submit" class="btn btn-success" value ="Add">
   </form>
   </div>

   <div class ="col-sm-7 offset-1">
    <h4 class="text-center alert alert-info table table-hover">Show Student Information</h4>
    {% if stu %}
      <table class="table">
  <thead>
    <tr>
      <th scope="col">ID</th>
      <th scope="col">Name</th>
      <th scope="col">Email</th>
      <th scope="col">Password</th>
      <th scope="col">Action</th>
    </tr>
  </thead>
  <tbody>
   {% for  st in stu %}
    <tr>
      <th scope="row">{{st.id}}</th>
      <td>{{st.name}}</td>
      <td>{{st.email}}</td>
      <td>{{st.password}}</td>
      <td>
      <a href= "{% url 'updatedata' st.id  %}" class= "btn btn-warning btn-sm">Edit</a>
      
      <!--to get id in delete button make use of form tag-->
     <form action="{% url 'deletedata' st.id  %}" method="post" class="d-inline"><!--creation of dynamic url to capture id ofdeleted button row-->
     {% csrf_token %}
     <input type="submit" class="btn btn-danger" value="Delete">
     </form>
    </tr>
    {% endfor %}
   
   </tbody>
   </table>

       
   
    {% else %}
     <h4 class="text-center alert alert-warning">No Records</h4>
     {% endif %}
     </div>
     </div>
{% endblock content %}
--------------------------------------------------------------------------------------------------
base.html

<!DOCTYPE html>
{% load static %}
<html Lang ="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>CRUD -Project</title>
<link rel="stylesheet" href="{% static 'enrollapp/css/bootstrap.css'%}">
</head>
<body>
<div class= "container mt-5">
<h2 class="text-center alert alert-danger"> Function Based View ModelForm CRUD Project</h2>
{% block content  %}  {% endblock content %}
</div>

<script src="{% static 'enrollapp/js/jquery.js' %}"></script>
<script src="{% static 'enrollapp/js/popper.js' %}"></script>
<script src="{% static 'enrollapp/js/bootstrap.js' %}"></script>

</body>
</html>
---------------------------------------------------------------------------------------------------------------------
updatestudent.html

{% extends 'enrollapp/base.html' %}

{% block content %}
<div class="row">
<div class="col-sm-8 offset-2">
  <h4 class="alter alert-info" > Update student Information</h4>
   <form action="" method="post">
     {% csrf_token %}
     {{form.as_p}}
     <input type="submit" class="btn btn-success" value= "Update">
   </form>
  </div>
  </div>
{% endblock content %}
---------------------------------
views.py(enrollapp)
from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.
def add_show(request):
    if request.method == 'POST':
     fm = StudentRegistration(request.POST)
       #one way to save data in db
        #if fm.is_valid():
        # fm.save()
      # 2nd way to save data in db.

      #To access data & save data in db.
     if fm.is_valid():
      nm = fm.cleaned_data['name']
      em = fm.cleaned_data['email']
      pw = fm.cleaned_data['password']
      reg = User(name=nm, email=em, password=pw) 
      reg.save()
      # Clear the form after  submitted to the db
      fm = StudentRegistration()
             
    else:
      fm =StudentRegistration()
      #to call all the db data on the frontend page
    stud = User.objects.all()

    return render(request, 'enrollapp/addandshow.html',{'form':fm,'stu':stud})

    # This Function will Delete
def delete_data(request, id):
  if request.method == 'POST':
    pi = User.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect('/')

     # This Function will update and edit
def update_data(request, id):
    if request.method == 'POST':
     pi = User.objects.get(pk=id)
     fm = StudentRegistration(request.POST, instance = pi)
     if fm.is_valid():
        fm.save()
     else:
       pi = User.objects.get(pk= id)
       fm = StudentRegistration(instance=pi)
       console.log(fm)
     return render(request,'enrollapp/updatestudent.html' , {'form':fm})

-------------------------------
urls.py(crudproj inner folder)

from django.contrib import admin
from django.urls import path
from enrollapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.add_show, name ="addandshow"),
    path('delete/<int:id>/',views.delete_data, name="deletedata"),
     path('<int:id>/',views.update_data, name="updatedata"),
]
-------------------------
admin.py

from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','email', 'password')

------------------------
forms.py
from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
 class Meta:
     model = User
     fields = ['name','email','password']
     widgets = {
         'name': forms.TextInput(attrs={'class':'form-control'}),
         'email': forms.EmailInput(attrs={'class':'form-control'}),
         'password': forms.PasswordInput(attrs={'class':'form-control'}),
     }
-------------------
models.py
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length= 70)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length =100)

-----------------
settings.py(crudproj inner folder)
"""
Django settings for crudproject project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_ac-x*r*nc_3zyj*#&rdci=c7od5^(s_g58u(8%rlu@(cwu$o@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'enrollapp',
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
    },
]

WSGI_APPLICATION = 'crudproject.wsgi.application'


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

