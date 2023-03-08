from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name="welcomepage"),
    path('home/', views.home, name='home'),
    path('home/sem1/', views.sem1, name='sem1'),
    path('home/sem1/calc_sem1/', views.calc_sem1, name="calc_sem1"),
    path('home/sem2/', views.sem2, name="sem2"),
    path('home/sem2/calc_sem2/', views.calc_sem2, name="calc_sem2"),
    path('home/sem3/', views.sem3, name="sem3"),
    path('home/sem3/calc_sem3/', views.calc_sem3, name="calc_sem3"),
    path('home/sem4/', views.sem4, name="sem4"),
    path('home/sem4/calc_sem4/', views.calc_sem4, name="calc_sem4")
]