# Generated by Django 3.0.7 on 2020-07-13 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admins', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CityModel',
        ),
        migrations.DeleteModel(
            name='StateModel',
        ),
    ]