# Generated by Django 4.1.3 on 2023-02-01 11:23

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
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('name', models.CharField(max_length=200, verbose_name='نام')),
                ('upc', models.CharField(max_length=200, verbose_name='شناسه محصول')),
                ('image', models.FileField(upload_to='products', verbose_name='عکس شاخص')),
                ('short_description', models.TextField(verbose_name='توضیح مختصر')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='محتوا')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'ویژگی محصول',
                'verbose_name_plural': 'ویژگی های محصول',
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'فروشنده',
                'verbose_name_plural': 'فروشنده ها',
            },
        ),
        migrations.CreateModel(
            name='RelatedProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='محصول')),
                ('related_products', models.ManyToManyField(related_name='related_products', to='products.product', verbose_name='محصولات مرتبط')),
            ],
            options={
                'verbose_name': 'محصول مرتبط',
                'verbose_name_plural': 'محصول های مرتبط',
            },
        ),
        migrations.CreateModel(
            name='ProductQuantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='مبلغ')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='تعداد')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='کالا')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.seller', verbose_name='فروشنده')),
            ],
            options={
                'verbose_name': 'موجودی کالا',
                'verbose_name_plural': 'موجودی های کالا',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('image', models.FileField(upload_to='', verbose_name='عکس')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='کالا')),
            ],
            options={
                'verbose_name': 'عکس محصول',
                'verbose_name_plural': 'عکس های محصول',
            },
        ),
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('full_name', models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')),
                ('content', models.TextField(verbose_name='متن')),
                ('rate', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1, verbose_name='امتیاز')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('is_accepted', models.BooleanField(default=False, verbose_name='تایید شده')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='products.productcomment', verbose_name='کامنت والد')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='محصولات')),
            ],
            options={
                'verbose_name': 'کامنت پست',
                'verbose_name_plural': 'کامنت های پست',
                'ordering': ('created_date',),
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('title', models.CharField(max_length=200, verbose_name='تایتل')),
                ('icon', models.FileField(blank=True, null=True, upload_to='product-category-icon', verbose_name='آیکون')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.productcategory', verbose_name='دسته بندی والد')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='ProductCatalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('catalog', models.FileField(upload_to='product-catalogs', verbose_name='کاتالوگ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='کالا')),
            ],
            options={
                'verbose_name': 'کاتالوگ محصول',
                'verbose_name_plural': 'کاتالوگ های محصول',
            },
        ),
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('title', models.CharField(max_length=200, verbose_name='تایتل')),
                ('icon', models.FileField(blank=True, null=True, upload_to='product-brand-icon', verbose_name='آیکون')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.productbrand', verbose_name='برند والد')),
            ],
            options={
                'verbose_name': 'برند',
                'verbose_name_plural': 'برند ها',
            },
        ),
        migrations.CreateModel(
            name='ProductAttributeValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=200, verbose_name='مقدار')),
                ('product_attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productattribute', verbose_name='دسته بندی ویژگی')),
                ('products', models.ManyToManyField(to='products.product', verbose_name='محصولات')),
            ],
            options={
                'verbose_name': 'مقدار ویژگی محصول',
                'verbose_name_plural': 'مقادیر ویژگی محصول',
            },
        ),
        migrations.AddField(
            model_name='productattribute',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productcategory', verbose_name='دسته بندی'),
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productbrand', verbose_name='برند'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productcategory', verbose_name='دسته بندی'),
        ),
        migrations.AddField(
            model_name='product',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='کالای پدر'),
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('discount_percent', models.PositiveIntegerField(default=0, verbose_name='درصد تخفیف (%):')),
                ('discount_amount', models.PositiveIntegerField(default=0, verbose_name='مبلغ تخفیف (ریال):')),
                ('discount_code', models.CharField(max_length=200, verbose_name='کد تخفیف')),
                ('expired_date', models.DateField(null=True, verbose_name='تاریخ انقضا')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر مربوطه')),
            ],
            options={
                'verbose_name': 'کد تخفیف',
                'verbose_name_plural': 'کد های تخفیف',
            },
        ),
    ]
