from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('level2/', views.level2, name='level2'),
    path('towers/', views.towers, name='towers'),
    path('adder/', views.adder, name='adder'),
    path('adder/save/', views.adder_save, name='adder_save'),
    path('adder/history/', views.adder_history, name='adder_history'),
]
