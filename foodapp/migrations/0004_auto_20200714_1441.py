# Generated by Django 3.0.7 on 2020-07-14 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0003_auto_20200714_1439'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='orderedBy',
            new_name='customer',
        ),
    ]
