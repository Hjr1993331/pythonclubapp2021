from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinute, Resource
from django.urls import reverse_lazy
from .forms import MeetingForm
from .forms import ResourceForm
from .forms import MeetingMinuteForm
from django.contrib.auth.decorators import login_required
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



@login_required
def newMeeting(request):
    form = MeetingForm

    if request.method == 'POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post = form.save(commit = True)
            post.save()
            form = MeetingForm()
    else:
        form = MeetingForm()
    return render(request, 'pythonclubapp/newmeeting.html', {'form': form})  

def newMeetingMinute(request):
    form = MeetingMinuteForm

    if request.method == 'POST':
        form=MeetingMinuteForm(request.POST)
        if form.is_valid():
            post = form.save(commit = True)
            post.save()
            form = MeetingMinuteForm()
    else:
        form = MeetingMinuteForm()
    return render(request, 'pythonclubapp/newmeetingminute.html', {'form': form})       


def newResource(request):
    form = ResourceForm

    if request.method == 'POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post = form.save(commit = True)
            post.save()
            form = ResourceForm()
    else:
        form = ResourceForm()
    return render(request, 'pythonclubapp/newresource.html', {'form': form})    

    
def loginmessage(request):
    return render(request, 'pythonclubapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'pythonclubapp/logoutmessage.html')    
