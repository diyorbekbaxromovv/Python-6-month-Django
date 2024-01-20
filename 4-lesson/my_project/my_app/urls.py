from django.urls import path
from . import views 
urlpatterns = [
    path('index/', views.index),
    path('main/', views.main, name="main")
]
