# Generated by Django 4.2.7 on 2023-12-09 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_job_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='tags',
        ),
    ]
