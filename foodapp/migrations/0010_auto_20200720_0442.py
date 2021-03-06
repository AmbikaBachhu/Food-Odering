# Generated by Django 3.0.7 on 2020-07-20 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0009_food_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Waiting', 'Waiting'), ('Placed', 'Placed'), ('Accepted by Restaurant', 'Accepted by Restaurant'), ('Cooking', 'Cooking'), ('Cancelled', 'Cancelled'), ('Delivered', 'Delivered')], default='Waiting', max_length=50),
        ),
    ]
