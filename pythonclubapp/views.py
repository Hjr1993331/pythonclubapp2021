from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinute, Resource
from django.urls import reverse_lazy

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

def meetingDetail(request, id):
    meeting = get_object_or_404(Meeting, pk = id)
    return render(request, 'pythonclubapp/meetingdetail.html', {'meeting' : meeting})


def meetingminuteDetail(request, id):
    meetingminute = get_object_or_404(MeetingMinute, pk = id)
    return render(request, 'pythonclubapp/meetingminutedetail.html', {'meetingminute' : meetingminute})    

def resourceDetail(request, id):
    resource = get_object_or_404(Resource, pk = id)
    return render(request, 'pythonclubapp/resourcedetail.html', {'resource' : resource})             