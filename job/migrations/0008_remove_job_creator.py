# Generated by Django 4.2.7 on 2023-12-09 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_job_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='creator',
        ),
    ]