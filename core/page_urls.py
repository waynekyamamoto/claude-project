from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('level2/', views.level2, name='level2'),
]
