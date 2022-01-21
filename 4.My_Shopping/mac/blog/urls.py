from django.urls import path
from. import views
urlpatterns = [
    path("",views.index,name="Shopblog")#go to index function in views.py of blog
]