# Generated by Django 3.0.7 on 2020-07-14 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0004_auto_20200714_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='r_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foodapp.Restaurant'),
        ),
    ]
