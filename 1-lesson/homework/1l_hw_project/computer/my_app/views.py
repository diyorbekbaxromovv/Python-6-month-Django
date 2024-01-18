from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404

# try:
#     def index(request):
#         return HttpResponse("")
#     def najot(request):
#         return HttpResponse("")
#     def murodjon(request):
#         return HttpResponse("")
#     def akmal(request):
#         return HttpResponse(" ")
#     def islom(request):
#         return HttpResponse("")
#     def sherzod(request):
#         return HttpResponse("")
#     def diyorbek(request):
#         return HttpResponse("")
    
# except:
#     raise Http404("Bu Page mavjud emas")



articles = {
    "index": "Salom bu index file",
    "najot": "Na'jot ta'limda",
    "murodjon": "Murodjon Tokhirov 1997",
    "akmal":"Akmaljon ulanov 1988",
    "islom":"Islom G'aniyev 1999",
    "sherzod":"Sherzod G'ayratov 2008",
    "diyorbek":"Bakhromov Diyorbek 2007",
    
}

def pages(request, topic):
    try:

        return HttpResponse(articles[topic])
    
    except :
        raise Http404("BU PAGE MAVJUD EMAS")