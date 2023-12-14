from django.db import models
from django.contrib.auth.models import User


class Skill(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='img', blank=True, null=True)
    cover_picture = models.ImageField(upload_to="img", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=60, null=True, blank=True)
    mobile_number = models.CharField(max_length=13, null=True, blank=True)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    skills = models.ManyToManyField(Skill, related_name='profileskill', blank=True)
    date_of_birth = models.DateField(null=True)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class WorkExperience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile_exp")
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    is_currently_working = models.BooleanField(default=False)
    responsibilty = models.TextField()
    
    
    def __str__(self):
        return self.title


class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile_edu")
    school_name = models.CharField(max_length=200)
    qualification = models.CharField(max_length=250)
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    
    def __str__(self):
        return self.school_name