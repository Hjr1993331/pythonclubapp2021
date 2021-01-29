from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('meetings/', views.meetings, name='meetings'),
    path('meetingminutes/', views.meetingminutes, name='meetingminutes'),
    path('resources/', views.resources, name='resources'),
]