from django.shortcuts import render, redirect
from .models import *


def home1(request):
    return render(request, 'home1.html')

