from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

from .models import Image, Location, User, Category

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def photolab(request):
    # imports photos and save it in database
    location = Location.objects.all()
    photolab = Image.objects.all()
    date=dt.date.today()
    users=User.objects.all()
    category=Category.objects.all()
    return render(request, 'all-photos/photolab.html',{'photolab':photolab,'location':location, 'date':date,'category':category,})


