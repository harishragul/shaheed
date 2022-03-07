from django.shortcuts import render
from .models import *

# Create your views here.
def media(request):
    return render(request, 'media/media.html')