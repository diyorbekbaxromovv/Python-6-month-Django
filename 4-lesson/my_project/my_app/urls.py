from django.urls import path
from . import views 
urlpatterns = [
    path('index/', views.index),
    path('main/', views.main, name="main"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')
]
