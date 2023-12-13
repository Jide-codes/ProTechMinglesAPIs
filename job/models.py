from django.db import models

from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Job(models.Model):
    # tags = models.ManyToManyField(Tag, related_name='Job_tags', blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=150)
    description = models.TextField()
    location = models.CharField(max_length=200)
    salary = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    responsibities = models.TextField()
    benefits = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title