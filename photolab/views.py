from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

from .models import Image, Location, User, Category

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


