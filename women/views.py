from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

lst_news =  [
            {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
            {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
            {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
        ]


def index(request):
    data = {
        'menu' : menu,
        'content': lst_news,
        'title': 'Главная страница'
    }
    return render(request, 'women/index.html', data)

def about(request):
    return render(request, 'women/about.html')

def addpage(request):
    return HttpResponse("Добавление статьи")
 
def contact(request):
    return HttpResponse("Обратная связь")
 
def login(request):
    return HttpResponse("Авторизация")

def show_post(request, post_id):
    return HttpResponse(f"Пост с номером {post_id}")

def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена")

