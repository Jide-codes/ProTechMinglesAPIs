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
    description = models.TextField(blank=True)
    type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    virtual_address = models.URLField(max_length=250, null=True, blank=True)
    physical_address = models.CharField(max_length=225, blank=True, null=True)
    cover_picture = models.ImageField(upload_to='img', blank=True, null=True)
    ticket_fee = models.CharField(max_length=100, null=True, blank=True)
    is_ticket =models.BooleanField(default=False)
    registration_site = models.URLField(max_length=250, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    event_date = models.DateField()
    event_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title