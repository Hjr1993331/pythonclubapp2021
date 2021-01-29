from django.contrib import admin
from .models import MeetingMinute, Meeting, Resource
# Register your models here.
admin.site.register(MeetingMinute)
admin.site.register(Meeting)
admin.site.register(Resource)