from django.urls import path, register_converter
from women import views
from women import converters

register_converter(converters.FourDigitYearConverter, 'year4')
 
urlpatterns = [
    path('', views.index),
    path('cats/<int:ind_cat>/', views.categories),
    path('cats/<str:ind_cat>/', views.categories, name='cat_str'),
    path('arhive/<year4:year>/', views.arhive),
    path('about/', views.about, name='about')
]

