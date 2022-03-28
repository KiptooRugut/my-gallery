from django.urls import path
from . import views

urlpatterns=[
    path('', views.photolab, name='photolab'),
    path('search/', views.search_results, name='search_results'),
    path('photos/(\d+)',views.photo,name ='photo')
]