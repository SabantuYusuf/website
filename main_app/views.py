from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'About.html')


def project(request):
    return render(request, 'project.html')


def contact(request):
    return render(request, 'contact.html')