from django.urls import path,include
from . import views

urlpatterns = [
    path('login/', views.login),
    path('login/register/', views.register),
    path('register/login/', views.login),
    path('register/', views.register)
]
