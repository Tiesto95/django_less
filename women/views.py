from django.shortcuts import render
from django.http import HttpResponse




def index(request):
    return HttpResponse("Главная страница сайта!")


def categories(request, ind_cat):
    return HttpResponse(f"Страница категории {ind_cat}")

def arhive(request, year):
    return HttpResponse(f"Архив за {year} год")