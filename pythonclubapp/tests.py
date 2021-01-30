from django.test import TestCase
from django.contrib.auth.models import User
from .models import MeetingMinute, Meeting, Resource
import datetime 

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

                   