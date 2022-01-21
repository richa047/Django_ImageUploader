from django.urls import path
from . import views

app_name ='blog'

urlpatterns = [
    
    # post views
    # function based view call
    #path('',views.post_list, name='post_list'),# function based view in urls.py
    #path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail,name='post_detail')'''

     #class based view call in i=url.py
    path('',views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    
]