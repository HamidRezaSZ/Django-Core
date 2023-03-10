# Generated by Django 4.1.3 on 2023-02-15 18:22

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('about', models.CharField(max_length=200, verbose_name='درباره من')),
                ('avater', models.FileField(upload_to='', verbose_name='آواتار')),
                ('avater_alt', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'نویسنده',
                'verbose_name_plural': 'نویسنده ها',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='blog.category', verbose_name='دسته بندی والد')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('title', models.CharField(max_length=256, verbose_name='عنوان')),
                ('thumbnail', models.ImageField(upload_to='post-images', verbose_name='تصویر شاخص')),
                ('description', models.TextField(verbose_name='توضیحات مختصر')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='محتوای پست')),
                ('show_in_home_page', models.BooleanField(default=False, verbose_name='نمایش در صفحه اصلی')),
                ('meta_title', models.CharField(blank=True, max_length=128, null=True, verbose_name='عنوان سئو')),
                ('meta_description', models.TextField(blank=True, null=True, verbose_name='توضیحات سئو')),
                ('authors', models.ManyToManyField(to='blog.author', verbose_name='نویسنده ها')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'پست',
                'verbose_name_plural': 'پست ها',
                'ordering': ('-created_date',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('title', models.CharField(max_length=200, verbose_name='تایتل')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='پست')),
            ],
            options={
                'verbose_name': 'تگ',
                'verbose_name_plural': 'تگ ها',
            },
        ),
        migrations.CreateModel(
            name='RelatedPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='related_post_post', to='blog.post', verbose_name='پست')),
                ('related_posts', models.ManyToManyField(to='blog.post', verbose_name='پست')),
            ],
            options={
                'verbose_name': 'پست مرتبط',
                'verbose_name_plural': 'پست های مرتبط',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('image', models.FileField(upload_to='', verbose_name='عکس')),
                ('image_alt', models.CharField(max_length=200, verbose_name='alt')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='پست')),
            ],
            options={
                'verbose_name': 'گالری',
                'verbose_name_plural': 'گالری ها',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('full_name', models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')),
                ('content', models.TextField(verbose_name='متن')),
                ('rate', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1, verbose_name='امتیاز')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('is_accepted', models.BooleanField(default=False, verbose_name='تایید شده')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='blog.comment', verbose_name='کامنت والد')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='پست')),
            ],
            options={
                'verbose_name': 'کامنت پست',
                'verbose_name_plural': 'کامنت های پست',
                'ordering': ('created_date',),
            },
        ),
    ]
