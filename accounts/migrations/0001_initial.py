# Generated by Django 4.1.3 on 2023-02-07 09:52

import accounts.validators
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('cell_phone', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='Start with 09/9 and it must 9 digits after that. For example: 09120000000 or 9120000000', regex='^(09|9)\\d{9}$')], verbose_name='شماره موبایل')),
                ('avatar', models.ImageField(default='', upload_to='user-avatars', verbose_name='آواتار')),
                ('gender', models.CharField(blank=True, choices=[('Female', 'خانم'), ('Male', 'آقا')], default=None, max_length=10, null=True, verbose_name='جنسیت')),
                ('national_id', models.CharField(blank=True, max_length=10, null=True, validators=[accounts.validators.validate_national_code], verbose_name='کد ملی')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربرها',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_birth', models.DateField(blank=True, null=True, verbose_name='تاریخ تولد')),
                ('marital_status', models.CharField(blank=True, choices=[('Single', 'مجرد'), ('Married', 'متاهل')], max_length=10, null=True, verbose_name='وضعیت تاهل')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.city', verbose_name='شهر مربوطه')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'پروفایل',
                'verbose_name_plural': 'پروفایل',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='نام')),
                ('last_name', models.CharField(max_length=200, verbose_name='نام خانوادگی')),
                ('phone_number', models.CharField(max_length=20, verbose_name='تلفن ثابت')),
                ('telephone_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Start with 09/9 and it must 9 digits after that. For example: 09120000000 or 9120000000', regex='^(09|9)\\d{9}$')], verbose_name='تلفن همراه')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('address', models.TextField(verbose_name='آدرس')),
                ('zip_code', models.CharField(max_length=30, verbose_name='کد پستی')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.city', verbose_name='شهر')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر مربوطه')),
            ],
            options={
                'verbose_name': 'آدرس',
                'verbose_name_plural': 'آدرس ها',
            },
        ),
    ]
