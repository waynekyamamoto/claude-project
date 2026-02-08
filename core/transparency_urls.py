from django.urls import path

from . import views

urlpatterns = [
    path('', views.transparency_home, name='transparency_home'),
    path('recent-ratings/', views.transparency_ratings, name='transparency_ratings'),
    path('team/', views.transparency_team, name='transparency_team'),
    path('insights/', views.transparency_insights, name='transparency_insights'),
    path('insights/<slug:slug>/', views.transparency_insight_detail, name='transparency_insight_detail'),
    path('contact/', views.transparency_contact, name='transparency_contact'),
    path('portal/', views.transparency_portal, name='transparency_portal'),
    path('portal/submit/', views.transparency_submit, name='transparency_submit'),
    path('portal/request/<int:pk>/', views.transparency_request_detail, name='transparency_request_detail'),
]
