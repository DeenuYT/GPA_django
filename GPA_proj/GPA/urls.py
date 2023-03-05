from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name="welcomepage"),
    path('home/', views.home, name='home'),
    path('home/sem1/', views.sem1, name='sem1'),
    path('home/sem1/calc_sem1/', views.calc_sem1, name="calc_sem1")
]