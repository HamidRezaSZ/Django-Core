# Generated by Django 4.1.3 on 2023-05-16 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payments', '0001_initial'),
        ('products', '0005_product_description_en_product_description_fa_and_more'),
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created_date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified_date')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='title')),
                ('title_fa', models.CharField(max_length=200, null=True, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('description_en', models.TextField(null=True, verbose_name='description')),
                ('description_fa', models.TextField(null=True, verbose_name='description')),
                ('delivery_price', models.PositiveIntegerField(default=0, verbose_name='delivery_price')),
            ],
            options={
                'verbose_name': 'Delivery Type',
                'verbose_name_plural': 'Delivery Types',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_code', models.CharField(blank=True, max_length=200, null=True, verbose_name='coupon_code')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='price')),
                ('discount_amount', models.PositiveIntegerField(default=0, verbose_name='discount_amount')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.address', verbose_name='address')),
                ('delivery_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.deliverytype', verbose_name='delivery_type')),
                ('payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='payments.payment', verbose_name='payment')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created_date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified_date')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('status', models.CharField(max_length=200, verbose_name='status')),
                ('status_en', models.CharField(max_length=200, null=True, verbose_name='status')),
                ('status_fa', models.CharField(max_length=200, null=True, verbose_name='status')),
            ],
            options={
                'verbose_name': 'Order Status',
                'verbose_name_plural': 'Order Statuses',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='quantity')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='order')),
                ('product_quantity', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.productquantity', verbose_name='product_quantity')),
            ],
            options={
                'verbose_name': 'Order Item',
                'verbose_name_plural': 'Order Items',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.orderstatus', verbose_name='status'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
