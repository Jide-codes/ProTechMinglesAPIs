# Generated by Django 4.2.7 on 2023-12-08 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_job_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='Job_tag', to='job.tag'),
        ),
    ]