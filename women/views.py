from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return HttpResponse("Главная страница сайта!")


def categories(request, ind_cat):
    return HttpResponse(f"Страница категории {ind_cat}")


def arhive(request, year):
    return HttpResponse(f"Архив за {year} год")


def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена")

def news(request):
    data = {
        'title': 'Страница новостей',
        'menu': ["О сайте", "Добавить статью", "Обратная связь", "Войти"],
        'lst_news': [
            {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
            {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
            {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
        ]
    }
    return render(request, 'women/index.html', data)