# Generated by Django 4.2.7 on 2023-12-14 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0004_education_skill_workexperience_profile_date_of_birth_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='skills',
        ),
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.ManyToManyField(blank=True, null=True, related_name='profileskill', to='userprofiles.skill'),
        ),
    ]