from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('level2/', views.level2, name='level2'),
    path('towers/', views.towers, name='towers'),
    path('adder/', views.adder, name='adder'),
    path('adder/save/', views.adder_save, name='adder_save'),
    path('adder/history/', views.adder_history, name='adder_history'),
    path('wordle/', views.wordle, name='wordle'),
    path('wordle/save/', views.wordle_save, name='wordle_save'),
    path('wordle/history/', views.wordle_history, name='wordle_history'),
    path('wordle/word/', views.wordle_word, name='wordle_word'),
]
