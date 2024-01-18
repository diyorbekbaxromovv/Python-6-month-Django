from django.urls import path
from . import views
urlpatterns = [
    # path('index/', views.index),
    # path('main/',views.main ),
    # path('fn6/', views.fn6)
    path("<str:topic>/", views.pages)
]