1. create project  miniblog
    django-admin startproject miniblog.
2.create app in project - python3 manage.py startapp blog.
3.install application 'blog' in miniblog(inner folder)-.setting.py
4.create templates\blog folder in blog(application) folder for html files.
5.create static\blog folder in blog(application) folder for css,js,images files.
6.download bootstrap from https://getbootstrap.com/ -> unzip it -->,
from css folder ->copy only bootstrap.css file  to static/blog/css folder
from js folder -> copy only bootstrap.js to static/blog/js folder
7. for dependency like  popper & jquery[create 2 files named jquery.js & popper.js file under static/blog/static]
jquery.js- https://code.jquery.com/jquery-3.6.0.js   (copy the code from here and paste it in static/blog/static/js/jquery.js)
popper.js-  https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js (copy the code from here and paste it in static/blog/static/js/popper.js)

------------------------------template design------------
8.create basic.html(making  skeleton esign that will be common in all pages )
9.in basic.html write code 
10.write code for home.html then render in view.py and give path in urls.py
11.after front end work create model in model.py ie blog/model.py  ie name post and field title and desc.
12.make migration ,migrate,superuser.then register model with blog/admin.py
----------------------
MINIBLOG(project outer folder)
blog(app)
-static/images
-templates/blog/about,addpost,base,contact,dashboard,home,login,navbar,signup
-admin.py
-forms.py
-models.py
-views.py
miniblog
-settings.py
-urls.py
----------------------------------
about.html
{% extends 'blog/base.html' %}
{% load static %}
   {% block content %}

   <div class= "col-sm-10">
    <h3 class= "text-white my-5">About Page</h3>
    <p>lorem Lorem Ipsum is simply dummy text of the printing and typesetting industry.
     Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
      when an unknown printer took a galley of type and scrambled it to make a 
      type specimen book. It has survived not only five centuries, but also the leap into 
      ctronic typesetting, remaining essentially unchanged.</p>
      <p>It was popularised in the
       1960s with the release of Letraset sheets containing Lorem Ipsum passages,
        and more recently with desktop publishing 
       software like Aldus PageMaker including versions of Lorem Ipsum. </p>
       </div>
   {% endblock content %}
   ----------------------------
   addpost
{% extends 'blog/base.html'%}
{% load static %}
{% block content %}
<div class="col-sm-10">
<h3 class="text-white my-5"> Dashboard/Add Post</h3>
<form actiom="" method="post" novalidate>
 {% csrf_token %}
 {{form.as_p}}
 <input type ="submit" value="Add" class="btn btn-sucess">
<a href="{% url 'dashboard' %}" class="btn btn-danger">Cancel</a>
</form>
</div>
{% endblock content %}

   ----------------------
   base
   <!DOCTYPE html>
{% load  static %}

<html Lang="en">
<head>
<meta charset="UTF-8">
<meta name ="viewport" content ="width=device-width,initial-scale=1.0">
<link rel="stylesheet" href="{% static 'blog/css/bootstrap.css' %}">
<link rel ="stylesheet" href = "{% static 'blog/css/style.css' %}">
<title> Document</title>
</head>
<body> 
<div class="container-fluid bg-dark">
{% include 'blog/navbar.html' %}
</div>

<div class= "container">
 
  <div class="row">
    <div class="col-sm-12">
     {% block msg %}
     {% endblock msg %}
    </div>
  </div>

  <div class="row">
    {% block side %}
    {% endblock side %}
  
    {% block content %}
    {% endblock content %}
 </div>

</div>

<script src="{% static 'blog/js/jquery.js' %}"></script>
<script src="{% static 'blog/js/popper.js' %}"></script>
<script src="{% static 'blog/js/bootstrap.js' %}"></script>

</body>
</html>
   -----------------------
   contact
   {% extends 'blog/base.html' %}
{% load static %}
   {% block content %}

   <div class= "col-sm-10">
    <h3 class= "text-white my-5">Contact Page</h3>
  
  <form>
   <div class="form-row">    
   
    <div class="form-group col-md-6">
    <label for="inputName" >Name</label>
    <input type="text" class="form-control" id="inputName" >
    </div>
    
    <div class="form-group col-md-6">
    <label for="inputEmail1" >Email </label>
    <input type="email" class="form-control" id="inputEmail1" >
     </div>   
    </div>
   
   <div class="form-group ">
    <label for="inputAddress" >Address</label>
    <input type="text" class="form-control" id="inputAddress">
  </div>

   <div class="form-group ">
    <label for="message" >Message</label>
    <textarea type="text" class="form-control" id="message" rows="3">
    </textarea>
  </div>
  <button type="submit" class="btn btn-primary">Send</button>
</form>
</div>
   {% endblock content %}
   --------------
   dashboard
   {% extends 'blog/base.html' %}
{% load static %}
{% block msg %}
  {% if messages %}
  {% for message in messages %}
   <div {% if message.tags %} class="alert alert-{{message.tags}} alert-dismissible fade show" {% endif %}>
   <strong>{{message}}</strong>
   <button type="button" class="close" data-dismiss="alert" aria-label ="Close">
    <span aria-hidden="true"> &times;</span>
   </button> 
   </div>
   {% endfor %}
   {% endif %}
 {% endblock msg %}
   
   {% block content %}
 
   <div class= "col-sm-10">
    <h3 class= "text-white my-5">Dashboard Page</h3>
    <a href="{% url 'addpost' %}" class= "btn btn-success">Add Post</a>
    <h4 class="text-center alert alert-info mt-3">Show Post Information</h4>
   {% if posts %}
    <table class="table table-hover bg-white">
     <thead>
      <tr class= "text-center">
       <th scope="col" style="width:2%">ID</th>
       <th scope="col" style="width:28%">Title</th>
       <th scope="col" style="width:28%">Description</th>
       <th scope="col" style="width:28%">Action</th>
      </tr>
      </thead>
      <tbody>
       {% for post in posts %}
        <tr>
          <th scope="row">{{post.id}}</th>
          <td>{{post.title}}</td>
          <td>{{post.desc}}</td>
          <td class="text-center">
           <a href="{% url 'updatepost' post.id %}" class= "btn btn-warning btn-sm">Edit </a>
           <form action="{% url 'deletepost' post.id%}" method="post" class="d-inline"> 
           {% csrf_token %}
           <input type ="submit" class= "btn btn-danger btn-sm" value="Delete">
           </form>
           </td>
         </tr>
         {% endfor %}
         </tbody>
         </table>

         {% else %}
         <h4  class="text-center alert alert-warning"> No records</h4>
         {% endif %}
   </div>
   {% endblock content %}
   
   ----------------------
   home
   {% extends 'blog/base.html' %}
{% load static %}
   {% block content %}

   <div class= "col-sm-10">
    <h3 class= "text-white my-5">Home Page</h3>
   {% for post in posts %}
   <div class="jumbotron jumbotron-fluid  jumbo-color">
   <div class="container">
  <h1 class="display-4 font-weight-bold">{{posts.title}}</h1>
  <p class="lead">{{post.desc}}</p> 
  </div>
  </div>
  {% endfor %}
  </div>
{% endblock content %}
   ----------------------
   login
   {% extends 'blog/base.html' %}
 {% load static %}  
 {% block content %}
 
 <div class= "col-sm-10">
<h3 class= "text-white my-5">Login Page</h3>
<form action ="" method="post" novalidate>
   {% csrf_token %}
   {% for fm in form %}
     <div class ="form-group">
     {{fm.label_tag}} {{fm}} <small class ="text-warning">{{fm.errors|striptags}}</small>
     </div>
   {% endfor %}

   <input type="submit" class= "btn btn-primary" value="Login" />
   {% if form.non_field_errors %}
    {% for error in form.non_field_errors %}
      <p class="alert alert-danger my-3">{{error}}</p>
    {% endfor %} 
   {% endif %}
</form>
</div>
{% endblock content %}

   -------------------
   navbar
 

<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Mini Blog</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="/">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href= "{% url 'about' %}">About</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'contact' %}">Contact</a>
        </li>
        
       {% if request.user.is_authenticated %} 
         <li class="nav-item">
          <a class="nav-link" href="{% url 'dashboard' %}">Dashboard</a>
        </li>
         <li class="nav-item">
          <a class="nav-link" href="{% url 'logout' %}">Logout</a>
        </li>

       {% else %}
         <li class="nav-item">
          <a class="nav-link" href="{% url 'signup' %}">Signup</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'login' %}">Login</a>
        </li>
       {% endif %}

      </ul>
    </div>
  </div>
</nav>
--------------------------------------
view.py(blog/)
from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm , PostForm, LoginForm
from django.contrib.auth import authenticate, login, logout 
#from .forms import LoginForm
from.models import Post
from django import forms



from django.contrib import messages

# Home
def home(request):
 posts =Post.objects.all()
 return render(request,'blog/home.html',{'posts':posts})

#About
def about(request):
 return render(request,'blog/about.html')

 #Contact
def contact(request):
 return render(request,'blog/contact.html')

 #Dashboard
def dashboard(request):
  if request.user.is_authenticated:
    posts = Post.objects.all()
    return render(request,'blog/dashboard.html', {'posts':posts})
  else:
    return HttpResponseRedirect('/login/')

def user_logout(request):
 logout(request)
 return HttpResponseRedirect('/')

# Signup
def user_signup(request):
   if request.method == "POST":
     form = SignUpForm(request.POST)
     if form.is_valid():
        messages.success(request, 'Congratulations!! you have become an an author')
        form.save()
   else:
        form = SignUpForm()
   return render(request,'blog/signup.html', {'form':form})

#Login
def user_login(request):
 if not request.user.is_authenticated:
  if request.method == "POST":
   form = LoginForm(request=request, data=request.POST)
   if form.is_valid():
    uname = form.cleaned_data['username']
    upass = form.cleaned_data['password']
    user  = authenticate(username=uname, password=upass)
    if user is not None:
        login(request, user)
        messages.success(request,'Logged in Successfully')
        return HttpResponseRedirect('/dashboard/')
  else:     
   form = LoginForm()
   return render(request,'blog/login.html', {'form':form})
 else:
   return HttpResponseRedirect('/dashboard/')
    


 # Add New Post
def add_post(request):
  if request.user.is_authenticated:
    if request.method == 'POST':
      form = PostForm(request.POST)
      if form.is_valid():
        title = form.cleaned_data['title']
        desc = form.cleaned_data['desc']
        pst = Post(title=title, desc=desc)
        pst.save()
        form = PostForm()
         #form.save()
    else:
      form = PostForm()
      return render(request, 'blog/addpost.html', {'form': form})
  else:
   return HttpResponseRedirect('/login/')

    # Update  Post
def update_post(request, id):
  if request.user.is_authenticated:
   return render(request, 'blog/updatepost.html')
  else:
   return HttpResponseRedirect('/login/')

    # Delete  Post
def delete_post(request, id):
  if request.user.is_authenticated:
   return HttpResponseRedirect('/dashboard/')
  else:
   return HttpResponseRedirect('/login/')
------------------------------------------------------------
   urls.py(miniblog)

   from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('signup/',views.user_signup, name='signup'),
    path('login/',views.user_login, name='login'),
    path('logout/',views.user_logout, name='logout'),
    path('addpost/',views.add_post , name ='addpost'),
    path('updatepost/<int:id>/',views.update_post, name='updatepost'),
    path('delete/<int:id>/',views.delete_post, name='deletepost'),

---------------------------------------------------------------
settings.py(miniblog)
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
    'blog',
]

ROOT_URLCONF = 'miniblog.urls'

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

WSGI_APPLICATION = 'miniblog.wsgi.application'

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
---------------------------------------------------------------------------
