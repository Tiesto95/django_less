from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


def index(request):
    return render(request, 'women\index.html')


def categories(request, ind_cat):
    return HttpResponse(f"Страница категории {ind_cat}")


def arhive(request, year):
    if year > 2025:
        return redirect('cat_str', 'music')
    return HttpResponse(f"Архив за {year} год")

def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена")

def about(request):
    return render(request, 'women/about.html')