from django.urls import path
from . import views


urlpatterns = [
    path("<str:topic>/", views.pages)
    
]