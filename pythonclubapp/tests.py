from django.test import TestCase
from django.contrib.auth.models import User
from .models import MeetingMinute, Meeting, Resource
import datetime 
from .forms import MeetingForm, MeetingMinuteForm, ResourceForm 
from django.urls import reverse_lazy, reverse
# Create your tests here.

class MeetingMinuteTest(TestCase):
    def setUp(self):
        self.type = MeetingMinute(meetingname = 'Django Class')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Django Class')

    def test_tablename(self):
        self.assertEqual(str(MeetingMinute._meta.db_table), 'meetingminute')  


class MeetingTest(TestCase):
    def setUp(self):
        self.type = MeetingMinute(meetingname = 'Django Super Class')
        self.user = User(username = 'user1')
        self.meeting = Meeting(meetingtitle = 'Django Class', meetingtype = self.type, user = self.user, dateentered = datetime.date(2021,1,29), meetinglocation = 'Seattle', meetingtime = datetime.time(22,55,29))

    def test_string(self):
        self.assertEqual(str(self.meeting), 'Django Class')

       



class ResourceTest(TestCase):
    def setUp(self):
        self.type = MeetingMinute(meetingname = 'Django Super Class')
        self.user = User(username = 'user1')
        self.meeting = Meeting(meetingtitle = 'Django Super Fun Class', meetingtype = self.type, user = self.user, dateentered = datetime.date(2021,1,29), meetinglocation = 'Seattle', meetingtime = datetime.time(22,55,29))
        self.resource = Resource(name = 'Django Super Class', location = 'Seattle', user = self.user, meeting = self.meeting, date = datetime.date(2021,1,29), time = datetime.time(22,55,29), text = 'Have Fun!', url='http://www.meeting.com', description="Meeting is so much fun!")

    def test_string(self):
        self.assertEqual(str(self.resource), 'Django Super Class')


class NewMeetingForm(TestCase):
    def test_meetingform(self):
        data = {
                'meetingtitle':'django class',  'meetinglocation':'seattle', 
                'user':'hijiri', 
                'meetingtype':'django fun class',
                'dateentered': '2021-1-30',
                'meetingtime': '22:55:29'  
            }   
        form = MeetingForm (data) 
        self.assertTrue(form.is_valid)

    # def test_Meetingform_Invalid(self): 
    #     data = {
    #             'meetingtitle':'django class',  'meetinglocation':'Seattle',
    #             'use':'Hijiri', 
    #             'meetingtype':'django fun class',
    #             'datentered': 'Jan 2021'
                 
    #         }  
    #     form = MeetingForm (data) 
    #     self.assertFalse(form.is_valid)     


class NewMeetingMinuteForm(TestCase):
    def test_meetingminuteform(self):
        data = {
               'meetingname':'django fun class',
               'minutedescription':'Have fun!'   
            }   
        form = MeetingMinuteForm (data) 
        self.assertTrue(form.is_valid)


class NewResourceForm(TestCase):
    def test_resourceform(self):
        data = {
               'name':'django fun class meeting',
               'location':'seattle',
               'user':'hijiri', 
               'meeting':'fun class', 
               'date':'2021-1-30', 
               'time':'22:55:29', 
               'text':'Fun meeting',   
               'url':'https://stackoverflow.com/questions/20723646/form-is-valid-returns-false-django', 
               'description':'Meeting is fun!'
            }   
        form = ResourceForm (data) 
        self.assertTrue(form.is_valid)        

class New_Meeting_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username = 'testuser1', password =  'P@ssw0rd!')
        self.type = MeetingMinute.objects.create(meetingname = 'Meeting Class')
        self.meeting = Meeting.objects.create(meetingtitle = 'Django Super Fun Class', meetingtype = self.type, user = self.test_user, dateentered = datetime.date(2021,1,29), meetinglocation = 'Seattle', meetingtime = datetime.time(22,55,29))

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newmeetings'))    
        self.assertRedirects(response, '/accounts/login/?next=/pythonclubapp/newmeetings/')


class New_MeetingMinute_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username = 'testuser1', password =  'P@ssw0rd!')
        self.type = MeetingMinute.objects.create(meetingname = 'Meeting Class')
        self.meeting = Meeting.objects.create(meetingtitle = 'Django Super Fun Class', meetingtype = self.type, user = self.test_user, dateentered = datetime.date(2021,1,29), meetinglocation = 'Seattle', meetingtime = datetime.time(22,55,29))
        self.meetingminute = MeetingMinute.objects.create(minutesdescription = 'Have fun!')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newmeetingminutes'))    
        self.assertRedirects(response, '/accounts/login/?next=/pythonclubapp/newmeetingminutes/')


class New_Resource_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username = 'testuser1', password =  'P@ssw0rd!')
        self.type = MeetingMinute.objects.create(meetingname = 'Meeting Class')
        self.meetingminute = MeetingMinute.objects.create(minutesdescription = 'Have fun!')
        self.meeting = Meeting.objects.create(meetingtitle = 'Django Super Fun Class', meetingtype = self.type, user = self.test_user, dateentered = datetime.date(2021,1,29), meetinglocation = 'Seattle', meetingtime = datetime.time(22,55,29))
        self.resource = Resource.objects.create(name = 'Django Super Class', location = 'Seattle', user = self.test_user, meeting = self.meeting, date = datetime.date(2021,1,29), time = datetime.time(22,55,29), text = 'Have Fun!', url='http://www.meeting.com', description="Meeting is so much fun!")

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newresources'))    
        self.assertRedirects(response, '/accounts/login/?next=/pythonclubapp/newresources/')

           