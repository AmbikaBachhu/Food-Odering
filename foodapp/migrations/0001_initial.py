# Generated by Django 3.0.7 on 2020-07-14 09:19

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_customer', models.BooleanField(default=False)),
                ('is_restaurant', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('digital', models.BooleanField(blank=True, default=False, null=True)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Food_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=225, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='newtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rname', models.CharField(max_length=100)),
                ('min_ord', models.IntegerField()),
                ('location', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('delivery', models.IntegerField(default=0)),
                ('menupic', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('votes', models.IntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')], default=4)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total_amount', models.IntegerField(default=0)),
                ('door_no', models.CharField(blank=True, max_length=200)),
                ('landmark', models.CharField(blank=True, max_length=200)),
                ('complete', models.BooleanField(default=False)),
                ('transaction_id', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(choices=[('Waiting', 'Waiting'), ('Placed', 'Placed'), ('Acknowledged', 'Acknowledged'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Dispatched', 'Dispatched')], default='Waiting', max_length=50)),
                ('orderedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('r_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.newtype')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.IntegerField(blank=True, default=None, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default=None, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.IntegerField(blank=True, default=None, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default=None, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rname', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=40)),
                ('min_ord', models.CharField(max_length=5)),
                ('location', models.CharField(max_length=40)),
                ('r_logo', models.FileField(upload_to='')),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed')], default='Open', max_length=50)),
                ('approved', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('food', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='foodapp.Food')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='foodapp.Order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(null=True)),
                ('order_id', models.IntegerField(null=True)),
                ('status', models.CharField(max_length=20, null=True)),
                ('order_timestamp', models.DateTimeField(null=True)),
                ('food', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foodapp.Food')),
                ('rest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foodapp.newtype')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='newtype',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.Place'),
        ),
        migrations.AddField(
            model_name='newtype',
            name='subcat',
            field=models.ManyToManyField(default='', to='foodapp.SubCategory'),
        ),
        migrations.AddField(
            model_name='food',
            name='food_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foodapp.Food_type'),
        ),
        migrations.AddField(
            model_name='food',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.Place'),
        ),
        migrations.AddField(
            model_name='food',
            name='rest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foodapp.newtype'),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=20)),
                ('l_name', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('door_no', models.CharField(max_length=200)),
                ('landmark', models.CharField(max_length=200)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='foodapp.Order')),
            ],
        ),
    ]
