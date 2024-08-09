from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


def home_page(request):
    return render(request, 'main.html')

