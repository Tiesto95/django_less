from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Главная страница сайта!")


def categories(request):
    return HttpResponse("Страница категории 2")