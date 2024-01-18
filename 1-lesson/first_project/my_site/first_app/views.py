from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404
# Create your views here.

articles = {
    "index": "Hello",
    "main": "Salom Najot Ta'lim",
    "fn6": "Salom fn6"
}

def pages(request, topic):
    try:

        return HttpResponse(articles[topic])
    
    except :
        raise Http404("404 Generic Error")

# def index(request):
#     return HttpResponse("Hello")

# def main(request):
#     return HttpResponse("Salom Najot Ta'lim")

# def fn6(request):
#     return HttpResponse("Salom fn6")