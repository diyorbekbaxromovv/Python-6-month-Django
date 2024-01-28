from django.shortcuts import render
from .models import Slider, About
# Create your views here.
def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def furniture(request):
    return render(request, 'furniture.html')

def index(request):
    
    slider = Slider.objects.get(pk=1)
    about = About.objects.get(pk=1)
    
    return render(request, 'index.html', context={'slider':slider, 'about':about})