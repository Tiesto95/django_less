from django.urls import path, register_converter
from women import views
from women import converters

register_converter(converters.FourDigitYearConverter, 'year4')
 
urlpatterns = [
    path('', views.index),
    path('cats/<int:ind_cat>/', views.categories),
    path('cats/<str:ind_cat>/', views.categories),
    path('arhive/<year4:year>/', views.arhive)
]

