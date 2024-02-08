from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index, name='index'),
    path('cat/<slug:cat_slug>/', views.show_category, name='cat'),
    path('guruh/<slug:guruh_slug>/', views.show_group, name='group'),
    path('subpage/<slug:post_slug>/', views.subpage, name='subpage'),
]