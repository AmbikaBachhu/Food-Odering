# Generated by Django 3.0.7 on 2020-07-14 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0002_auto_20200714_1048'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Address',
            new_name='Addresss',
        ),
        migrations.AlterField(
            model_name='addresss',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='foodapp.Customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.Customer'),
        ),
        migrations.AlterField(
            model_name='orderhistory',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foodapp.Customer'),
        ),
    ]