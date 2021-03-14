

from django.http import HttpResponse
from django.shortcuts import render
from catalog.models import Category

# Create your views here.


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')




