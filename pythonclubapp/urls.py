from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('meetings/', views.meetings, name='meetings'),
    path('meetingminutes/', views.meetingminutes, name='meetingminutes'),
    path('resources/', views.resources, name='resources'),
    path('meetingDetail/<int:id>', views.meetingDetail, name='detail'),
    path('meetingminuteDetail/<int:id>', views.meetingminuteDetail, name='detail1'),
    path('resourceDetail/<int:id>', views.resourceDetail, name='detail2'),
    path('newmeetings/', views.newMeeting, name = 'newmeetings'),
    path('newmeetingminutes/', views.newMeetingMinute, name = 'newmeetingminutes'),
    path('newresources/', views.newResource, name = 'newresources'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]