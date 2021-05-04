from django.shortcuts import render

# Create your views here.

from django.http import HttpRequest
from django.http import HttpResponse


# hope consumer input 172.0.0.1:8000/index/
# to visit views
def index(request):
    return HttpResponse('OK!')
