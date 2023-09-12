from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import HomeGrid

# Create your views here.
def home(request):
    homegrid = HomeGrid.objects.all()
    return render(request, 'index.html')

def single(request):
    return render(request, 'single-post.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def category(request):
    return render(request, 'category.html')