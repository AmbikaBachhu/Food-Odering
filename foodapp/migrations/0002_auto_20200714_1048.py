# Generated by Django 3.0.7 on 2020-07-14 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='info',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='r_logo',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='delivery',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='menupic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='place',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='foodapp.Place'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='subcat',
            field=models.ManyToManyField(default='', to='foodapp.SubCategory'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='votes',
            field=models.IntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')], default=4),
        ),
        migrations.AlterField(
            model_name='food',
            name='rest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foodapp.Restaurant'),
        ),
        migrations.AlterField(
            model_name='order',
            name='r_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.Restaurant'),
        ),
        migrations.AlterField(
            model_name='orderhistory',
            name='rest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foodapp.Restaurant'),
        ),
        migrations.DeleteModel(
            name='newtype',
        ),
    ]
