# Generated by Django 3.1.6 on 2021-02-12 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeslot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeslot',
            name='name',
        ),
    ]
