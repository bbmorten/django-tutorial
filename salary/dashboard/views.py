from django.http.response import HttpResponse
from django.shortcuts import render

from django.template import loader

# Create your views here.


def index(request):
    return render(request, 'dashboard/index.html')
    #return HttpResponse("Hello, world. You're at the polls index.")
def dom(request):
    return render(request, 'dashboard/dom.html')

def home(request):
  context = {"name": "Spot"}
  template = loader.get_template("dashboard/home.html")
  return HttpResponse(template.render(context))

def home(request):
  context = {"name": "Junior"}
  return render(request, "dashboard/home.html", context)