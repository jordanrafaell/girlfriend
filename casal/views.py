from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(requests):
    return render(requests, template_name="index.html")
