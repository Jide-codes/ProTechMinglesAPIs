# Generated by Django 4.2.7 on 2023-12-14 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0006_alter_profile_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='profile_edu', to='userprofiles.profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workexperience',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='profile_exp', to='userprofiles.profile'),
            preserve_default=False,
        ),
    ]
