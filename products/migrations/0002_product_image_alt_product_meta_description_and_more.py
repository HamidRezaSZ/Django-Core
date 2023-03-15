# Generated by Django 4.1.3 on 2023-03-14 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_alt',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='meta_description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات سئو'),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_title',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='عنوان سئو'),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('tag', models.CharField(max_length=50, verbose_name='تگ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='کالا')),
            ],
            options={
                'verbose_name': 'تگ محصول',
                'verbose_name_plural': 'تگ های محصول',
            },
        ),
    ]