# Generated by Django 4.1.3 on 2023-04-04 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_orderstatus_alter_deliverytype_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverytype',
            name='description_en',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='deliverytype',
            name='description_fa',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='deliverytype',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='deliverytype',
            name='title_fa',
            field=models.CharField(max_length=200, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='orderstatus',
            name='status_en',
            field=models.CharField(max_length=200, null=True, verbose_name='status'),
        ),
        migrations.AddField(
            model_name='orderstatus',
            name='status_fa',
            field=models.CharField(max_length=200, null=True, verbose_name='status'),
        ),
    ]
