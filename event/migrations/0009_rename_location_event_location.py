# Generated by Django 4.2.7 on 2023-12-16 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_alter_event_end_date_alter_event_end_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='Location',
            new_name='location',
        ),
    ]
