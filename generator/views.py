from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
   return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    thepassword = ''
    characters = list('abcawereertyiybfwqsdtuigioipuyr')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCEDEAETWOKXMWQZOIR'))
    if request.GET.get('special'):
        characters.extend(list('!@$%^&*()_!'))
    if request.GET.get('numbers'):
        characters.extend(list('12345678901231454657568769789'))

    length = int(request.GET.get('length'))
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})