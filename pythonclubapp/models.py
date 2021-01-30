from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MeetingMinute(models.Model):
    meetingname=models.CharField(max_length=255)
    minutesdescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.meetingname

    class Meta:
        db_table='meetingminute'

class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetinglocation=models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    meetingtype=models.ForeignKey(MeetingMinute, on_delete=models.DO_NOTHING)
    dateentered=models.DateField()
    meetingtime=models.TimeField()

    # def discountaAmount(self):
    #     self.discount = self.price * .05
    #     return self.discount

    # def discountPrice(self):  
    #     self.discountPrice = self.price - self.discount  

    def __str__(self):
        return self.meetingtitle

    class Meta:
        db_table='meeting'
    


class Resource(models.Model):
    name=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    meeting=models.ForeignKey(Meeting, on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    text=models.TextField()
    url=models.URLField()
    description=models.TextField() 

    def __str__(self):
        return self.name

    class Meta:
        db_table='resource'