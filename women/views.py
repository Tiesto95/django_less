from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

lst_news =  [
	        {'id': 1, 'title': 'Анджелина Джоли', 'content': '''<h1>Анджелина Джоли</h1> (англ. Angelina Jolie[7], при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН.
    Обладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».''',
     'is_published': True},
            {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
            {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
        ]

cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},
]

def index(request):
    data = {
        'menu' : menu,
        'posts': lst_news,
        'cat_selected': 0,
        'title': 'Главная страница'
    }
    return render(request, 'women/index.html', data)

def about(request):
    data = {
        'title': 'О сайте',
        'menu': menu
    }
    return render(request, 'women/about.html', data)

def addpage(request):
    return HttpResponse("Добавление статьи")
 
def contact(request):
    return HttpResponse("Обратная связь")
 
def login(request):
    return HttpResponse("Авторизация")

def show_post(request, post_id):
    return HttpResponse(f"Пост с номером {post_id}")

def show_category(request, cat_id):
    data = {
        'menu': menu,
        'cat_selected': cat_id, 
        'title': 'Страница категорий'
    }
    return render(request, 'women/index.html', data)

def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена")

