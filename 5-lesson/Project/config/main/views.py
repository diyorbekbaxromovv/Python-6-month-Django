from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    categories = ["Python", "Data science", "Mobile dev", "Machine learning"]
    data = {"numbers": list(range(1,11)),  "categories": categories  }
    return render(request, 'index.html', context= data)
        