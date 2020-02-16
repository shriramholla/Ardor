from django.shortcuts import render
from django.urls import include, path

from . import views

from django.http import StreamingHttpResponse

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/<str:movie>/', views.movies, name='movies'),
    path('movies/bad/<str:movie>', views.related_movies, name='related_movies'),
    path('forms', views.forms, name='forms'),
    path('test', views.test, name='test'),
    path('history', views.history, name='history'),
    path('closeCam', views.closeCam, name='closeCam'),
    path('addNewMusic', views.addNewMusic, name='addNewMusic'),
    path('music/<str:artist>', views.music, name='music'),
]
