from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'my_app/index.html')

def main(request):
    return render(request, 'my_app/main.html')
