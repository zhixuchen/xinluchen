# Generated by Django 3.2.11 on 2022-01-09 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Staff_info', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='address',
        ),
    ]