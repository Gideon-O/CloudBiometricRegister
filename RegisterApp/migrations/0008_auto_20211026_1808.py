# Generated by Django 3.2.7 on 2021-10-26 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegisterApp', '0007_auto_20211025_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activitie',
            name='session_when',
        ),
        migrations.AddField(
            model_name='activitie',
            name='session_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='activitie',
            name='session_time',
            field=models.TimeField(null=True),
        ),
    ]