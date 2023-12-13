from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class EventType(models.Model):
    title = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=50)
    type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    virtual_address = models.CharField(max_length=200, blank=True, null=True)
    physical_address = models.CharField(max_length=225, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    event_date = models.DateField()
    event_time = models.TimeField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title