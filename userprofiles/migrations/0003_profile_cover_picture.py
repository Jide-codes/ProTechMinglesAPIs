# Generated by Django 4.2.7 on 2023-12-13 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0002_alter_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cover_picture',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]