from django.shortcuts import render
from .models import Meeting, MeetingMinute, Resource

# Create your views here.


def index(request):
    return render(request, 'pythonclubapp/index.html')

def meetings(request):
    meeting_list = Meeting.objects.all()
    return render(request, 'pythonclubapp/meetings.html', {'meeting_list': meeting_list})

def meetingminutes(request):
    meetingminute_list = MeetingMinute.objects.all()
    return render(request, 'pythonclubapp/meetingminutes.html', {'meetingminute_list': meetingminute_list})

def resources(request):
    resource_list = Resource.objects.all()
    return render(request, 'pythonclubapp/resources.html', {'resource_list': resource_list})        